/* Exercise the real engine + bundled Three/OrbitControls without requiring WebGL. */
const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const ROOT = path.resolve(__dirname, '../..');
const read = file => fs.readFileSync(path.join(ROOT, file), 'utf8');

function eventTarget() {
    const listeners = new Map();
    return {
        listeners,
        addEventListener(type, fn) {
            if (!listeners.has(type)) listeners.set(type, new Set());
            listeners.get(type).add(fn);
        },
        removeEventListener(type, fn) { listeners.get(type)?.delete(fn); },
        emit(type, event = {}) {
            for (const fn of listeners.get(type) || []) fn({ type, ...event });
        }
    };
}

function makeStudio(loadThree = true) {
    const elements = new Map();
    const document = Object.assign(eventTarget(), {
        readyState: 'complete', hidden: false,
        getElementById: id => elements.get(id) || null,
        querySelectorAll: () => []
    });
    document.body = {
        style: { overflow: 'auto' },
        insertAdjacentHTML(position, html) {
            for (const [, id] of html.matchAll(/\bid="([^"]+)"/g)) {
                const classes = new Set();
                elements.set(id, Object.assign(eventTarget(), {
                    style: {}, ownerDocument: document,
                    clientWidth: 550, clientHeight: 450,
                    classList: {
                        add: value => classes.add(value),
                        remove: value => classes.delete(value),
                        contains: value => classes.has(value),
                        toggle(value, force = !classes.has(value)) {
                            if (force) classes.add(value);
                            else classes.delete(value);
                        }
                    }
                }));
            }
        }
    };
    let now = 0;
    let nextFrame = 0; // 0 is a valid requestAnimationFrame handle.
    let nextTimer = 0;
    const frames = new Map();
    const timers = new Map();
    const context = Object.assign(eventTarget(), {
        document, console, devicePixelRatio: 1,
        performance: { now: () => now },
        requestAnimationFrame(fn) { const id = nextFrame++; frames.set(id, fn); return id; },
        cancelAnimationFrame(id) { frames.delete(id); },
        setTimeout(fn) { const id = nextTimer++; timers.set(id, fn); return id; },
        clearTimeout(id) { timers.delete(id); },
        VOCAB_DATA: [
            { jp: 'かばん', kanji: '鞄', kana: 'かばん', vi: 'Vali' },
            { jp: 'でんしゃ', kanji: '電車', kana: 'でんしゃ', vi: 'Tàu' }
        ]
    });
    context.window = context;
    vm.createContext(context);
    const renderers = [];
    const orbitControls = [];
    const disposals = new Map();
    if (loadThree) {
        vm.runInContext(read('assets/js/vendor/three.min.js'), context);
        vm.runInContext(read('assets/js/vendor/OrbitControls.js'), context);
        const { THREE } = context;
        for (const type of [THREE.BufferGeometry, THREE.Material, THREE.Texture]) {
            const dispose = type.prototype.dispose;
            type.prototype.dispose = function () {
                disposals.set(this, (disposals.get(this) || 0) + 1);
                return dispose.call(this);
            };
        }
        const OrbitControls = THREE.OrbitControls;
        THREE.OrbitControls = class extends OrbitControls {
            constructor(...args) { super(...args); orbitControls.push(this); }
        };
        THREE.WebGLRenderer = class {
            constructor({ canvas }) {
                this.domElement = canvas;
                this.shadowMap = {};
                this.renders = 0;
                this.renderListDisposals = 0;
                this.renderLists = { dispose: () => this.renderListDisposals++ };
                renderers.push(this);
            }
            setSize(width, height) { this.size = [width, height]; }
            setPixelRatio() {}
            render(scene, camera) {
                assert(scene.isScene && camera.isPerspectiveCamera);
                this.scene = scene;
                this.camera = camera;
                this.renders++;
            }
        };
    }
    vm.runInContext(read('assets/js/vocab-3d-engine.js'), context);
    return {
        context, document, elements, frames, timers, renderers, orbitControls, disposals,
        step() {
            const pending = Array.from(frames.values());
            frames.clear();
            now += 16;
            pending.forEach(fn => fn(now));
        },
        visibility(hidden) {
            document.hidden = hidden;
            document.emit('visibilitychange');
        }
    };
}

function assertDisposedOnce(studio, model) {
    let meshes = 0;
    model.traverse(child => {
        if (!child.isMesh) return;
        meshes++;
        assert.strictEqual(studio.disposals.get(child.geometry), 1, 'geometry disposed once, including shared geometry');
        assert.strictEqual(studio.disposals.get(child.material), 1, 'material disposed once, including shared materials');
    });
    assert(meshes > 1, 'test must exercise actual generated meshes, not an empty model');
}

const studio = makeStudio();
const api = studio.context;
api.openVocab3D(0);
const renderer = studio.renderers[0];
assert(renderer?.renders > 0, 'opening must actually render, without a visibility-change workaround');
assert.strictEqual(studio.frames.size, 1);
assert(studio.frames.has(0));
assert.strictEqual(studio.elements.get('v3dCounter').textContent, '1 / 2');
let model = renderer.scene.children.find(child => child.isGroup);
api.closeVocab3DModal();
assert.strictEqual(studio.frames.size, 0, 'close must cancel even RAF handle 0');
assert.strictEqual(studio.timers.size, 0, 'no delayed opener may survive closing');
assert.strictEqual(studio.document.body.style.overflow, 'auto');
assert.strictEqual(studio.orbitControls[0].enabled, false);
assertDisposedOnce(studio, model);

api.openVocab3D();
model = renderer.scene.children.find(child => child.isGroup);
const oldRotation = model.rotation.y;
const oldCamera = renderer.camera.position.clone();
studio.step();
assert(model.rotation.y > oldRotation, 'the active procedural model must animate');
assert(oldCamera.distanceTo(renderer.camera.position) > 0, 'bundled OrbitControls must update');
api.openVocab3D(1);
assertDisposedOnce(studio, model);
assert.strictEqual(studio.frames.size, 1, 'repeated open must not double the render loop');
assert.strictEqual(studio.renderers.length, 1, 'reuse the renderer/context across opens');
assert.strictEqual(studio.orbitControls.length, 1, 'do not install duplicate controls');
assert.strictEqual(renderer.scene.children.filter(child => child.isGroup).length, 1);
studio.step();
assert.strictEqual(studio.elements.get('v3dCounter').textContent, '2 / 2');
model = renderer.scene.children.find(child => child.isGroup);
api.prev3DVocab();
assertDisposedOnce(studio, model);
studio.step();
assert.strictEqual(studio.elements.get('v3dCounter').textContent, '1 / 2');

model = renderer.scene.children.find(child => child.isGroup);
studio.visibility(true);
const pausedRenders = renderer.renders;
assert.strictEqual(studio.frames.size, 0, 'hidden tabs must pause');
studio.step();
assert.strictEqual(renderer.renders, pausedRenders);
assert.strictEqual(studio.disposals.has(model.children[0].geometry), false, 'pause must retain the current model');
studio.visibility(false);
studio.visibility(false);
assert.strictEqual(studio.frames.size, 1, 'resume must start exactly one loop');
assert(renderer.renders > pausedRenders);
studio.visibility(true);
api.closeVocab3DModal();
assertDisposedOnce(studio, model);
studio.visibility(false);
assert.strictEqual(studio.frames.size, 0, 'a closed modal must not resume');
assert.strictEqual(renderer.scene.children.filter(child => child.isGroup).length, 0);
assert(renderer.renderListDisposals >= 2, 'close must release references to disposed meshes');

studio.visibility(true);
const beforeHiddenOpen = renderer.renders;
api.openVocab3D(1);
assert.strictEqual(studio.frames.size, 0, 'opening in a hidden tab must not start rendering');
assert.strictEqual(renderer.renders, beforeHiddenOpen);
studio.visibility(false);
assert.strictEqual(studio.frames.size, 1);
studio.step();
assert.strictEqual(studio.elements.get('v3dCounter').textContent, '2 / 2');
const viewport = studio.elements.get('v3dViewport');
viewport.clientWidth = 720;
viewport.clientHeight = 360;
api.emit('resize');
assert.deepStrictEqual(renderer.size, [720, 360]);
assert.strictEqual(renderer.camera.aspect, 2);
viewport.clientHeight = 0;
api.emit('resize');
assert.strictEqual(renderer.camera.aspect, 2, 'zero-size resize must not corrupt the camera');
assert.strictEqual(studio.document.listeners.get('visibilitychange').size, 1);
assert.strictEqual(api.listeners.get('resize').size, 1);
api.closeVocab3DModal();
api.closeVocab3DModal();
assert.strictEqual(studio.frames.size, 0);
assert.strictEqual(studio.document.body.style.overflow, 'auto');

const empty = makeStudio();
empty.context.VOCAB_DATA = [];
empty.context.openVocab3D(0);
assert.strictEqual(empty.renderers.length, 0, 'empty data must not allocate a renderer');
const missingThree = makeStudio(false);
missingThree.context.openVocab3D(0);
assert.strictEqual(missingThree.frames.size, 0);
assert.strictEqual(missingThree.document.body.style.overflow, 'auto', 'missing Three must not trap page scrolling');
console.log('3D lifecycle checks passed: real Three/OrbitControls, render, close, pause/resume, one loop, mesh disposal and resize.');
