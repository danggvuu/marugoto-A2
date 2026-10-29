/**
 * ==========================================================================
 * MARUGOTO VOCABULARY 3D INTERACTIVE STUDIO & PROCEDURAL MODEL ENGINE
 * ==========================================================================
 * - Renders Interactive 3D Animated Models for 100% of Vocabulary Words
 * - Powered by Three.js (r128) + OrbitControls with Studio Lighting & Shadows
 * - 360° Free Touch/Mouse Orbit Rotation, Pinch Zoom, Auto-Rotation & Pulse
 * - Synchronized Dual-Engine Tokyo Native Voice Pronunciation
 * - Universal Category-Aware Procedural 3D Geometry Generator
 * ==========================================================================
 */

(function (window, document) {
    'use strict';

    let scene, camera, renderer, controls;
    let currentModelGroup = null;
    let animFrameId = null;
    let isAutoRotating = true;
    let animMode = 'float'; // 'float', 'spin', 'pulse', 'wireframe'
    let currentVocabList = [];
    let currentVocabIndex = 0;
    let isInitialized = false;

    // --- 1. PROCEDURAL 3D MESH GENERATORS ---
    const ModelGenerators = {
        // A. Food & Drinks
        apple: () => {
            const group = new THREE.Group();
            const bodyGeo = new THREE.SphereGeometry(1.2, 32, 32);
            bodyGeo.scale(1, 0.95, 1);
            const bodyMat = new THREE.MeshStandardMaterial({
                color: 0xef4444,
                roughness: 0.25,
                metalness: 0.1,
                clearcoat: 0.6
            });
            const body = new THREE.Mesh(bodyGeo, bodyMat);
            body.castShadow = true;
            group.add(body);

            // Stem
            const stemGeo = new THREE.CylinderGeometry(0.06, 0.04, 0.6, 12);
            const stemMat = new THREE.MeshStandardMaterial({ color: 0x5c3d2e, roughness: 0.8 });
            const stem = new THREE.Mesh(stemGeo, stemMat);
            stem.position.set(0, 1.25, 0);
            stem.rotation.z = 0.2;
            group.add(stem);

            // Leaf
            const leafGeo = new THREE.SphereGeometry(0.35, 16, 16);
            leafGeo.scale(1, 0.15, 0.6);
            const leafMat = new THREE.MeshStandardMaterial({ color: 0x22c55e, roughness: 0.4 });
            const leaf = new THREE.Mesh(leafGeo, leafMat);
            leaf.position.set(0.25, 1.3, 0);
            leaf.rotation.z = -0.4;
            group.add(leaf);
            return group;
        },

        strawberry: () => {
            const group = new THREE.Group();
            const coneGeo = new THREE.ConeGeometry(1.0, 1.6, 32);
            const berryMat = new THREE.MeshStandardMaterial({ color: 0xe11d48, roughness: 0.35 });
            const berry = new THREE.Mesh(coneGeo, berryMat);
            berry.rotation.x = Math.PI;
            berry.position.y = 0.3;
            group.add(berry);

            // Green Calyx / Leaves
            for (let i = 0; i < 5; i++) {
                const angle = (i / 5) * Math.PI * 2;
                const calyxGeo = new THREE.ConeGeometry(0.2, 0.6, 8);
                const calyxMat = new THREE.MeshStandardMaterial({ color: 0x16a34a, roughness: 0.5 });
                const calyx = new THREE.Mesh(calyxGeo, calyxMat);
                calyx.position.set(Math.cos(angle) * 0.4, 1.1, Math.sin(angle) * 0.4);
                calyx.rotation.z = Math.cos(angle) * 0.7;
                calyx.rotation.x = Math.sin(angle) * 0.7;
                group.add(calyx);
            }
            return group;
        },

        onigiri: () => {
            const group = new THREE.Group();
            // Triangular Rice Prism
            const prismGeo = new THREE.CylinderGeometry(1.2, 1.2, 0.9, 3);
            const riceMat = new THREE.MeshStandardMaterial({
                color: 0xf8fafc,
                roughness: 0.9,
                bumpScale: 0.05
            });
            const rice = new THREE.Mesh(prismGeo, riceMat);
            rice.rotation.x = Math.PI / 2;
            rice.rotation.z = Math.PI;
            group.add(rice);

            // Nori Band
            const noriGeo = new THREE.BoxGeometry(0.85, 0.92, 0.45);
            const noriMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.95 });
            const nori = new THREE.Mesh(noriGeo, noriMat);
            nori.position.set(0, -0.4, 0);
            group.add(nori);
            return group;
        },

        sandwich: () => {
            const group = new THREE.Group();
            // Bread 1
            const breadMat = new THREE.MeshStandardMaterial({ color: 0xfde047, roughness: 0.7 });
            const b1 = new THREE.Mesh(new THREE.CylinderGeometry(1.3, 1.3, 0.25, 3), breadMat);
            b1.position.y = -0.4;
            b1.rotation.y = Math.PI / 6;
            group.add(b1);

            // Lettuce
            const lettuceMat = new THREE.MeshStandardMaterial({ color: 0x22c55e, roughness: 0.5 });
            const lettuce = new THREE.Mesh(new THREE.CylinderGeometry(1.35, 1.35, 0.15, 3), lettuceMat);
            lettuce.position.y = -0.15;
            lettuce.rotation.y = Math.PI / 5;
            group.add(lettuce);

            // Cheese & Ham
            const hamMat = new THREE.MeshStandardMaterial({ color: 0xf43f5e, roughness: 0.6 });
            const ham = new THREE.Mesh(new THREE.CylinderGeometry(1.25, 1.25, 0.15, 3), hamMat);
            ham.position.y = 0.05;
            ham.rotation.y = Math.PI / 7;
            group.add(ham);

            // Bread 2
            const b2 = new THREE.Mesh(new THREE.CylinderGeometry(1.3, 1.3, 0.25, 3), breadMat);
            b2.position.y = 0.35;
            b2.rotation.y = Math.PI / 6;
            group.add(b2);
            return group;
        },

        sakeBottle: () => {
            const group = new THREE.Group();
            // Ceramic Tokkuri Body
            const bodyGeo = new THREE.SphereGeometry(0.9, 32, 32);
            bodyGeo.scale(1, 1.3, 1);
            const mat = new THREE.MeshStandardMaterial({
                color: 0xf1f5f9,
                roughness: 0.15,
                metalness: 0.05,
                clearcoat: 0.8
            });
            const body = new THREE.Mesh(bodyGeo, mat);
            group.add(body);

            // Neck
            const neckGeo = new THREE.CylinderGeometry(0.32, 0.42, 0.8, 24);
            const neck = new THREE.Mesh(neckGeo, mat);
            neck.position.y = 1.2;
            group.add(neck);

            // Blue Band Ring
            const ringGeo = new THREE.CylinderGeometry(0.33, 0.35, 0.12, 24);
            const ringMat = new THREE.MeshStandardMaterial({ color: 0x1d4ed8, roughness: 0.3 });
            const ring = new THREE.Mesh(ringGeo, ringMat);
            ring.position.y = 1.35;
            group.add(ring);

            // Sake Ochoko Cup
            const cupGeo = new THREE.CylinderGeometry(0.5, 0.35, 0.45, 20);
            const cup = new THREE.Mesh(cupGeo, mat);
            cup.position.set(1.2, -0.65, 0.3);
            group.add(cup);
            return group;
        },

        ramenBowl: () => {
            const group = new THREE.Group();
            // Ceramic Bowl
            const bowlGeo = new THREE.CylinderGeometry(1.4, 0.7, 1.0, 32, 1, true);
            const bowlMat = new THREE.MeshStandardMaterial({
                color: 0xdc2626,
                roughness: 0.2,
                side: THREE.DoubleSide
            });
            const bowl = new THREE.Mesh(bowlGeo, bowlMat);
            group.add(bowl);

            // Soup Broth
            const soupGeo = new THREE.CircleGeometry(1.25, 32);
            const soupMat = new THREE.MeshStandardMaterial({ color: 0xb45309, roughness: 0.1 });
            const soup = new THREE.Mesh(soupGeo, soupMat);
            soup.rotation.x = -Math.PI / 2;
            soup.position.y = 0.35;
            group.add(soup);

            // Narutomaki Fish Cake
            const narutoGeo = new THREE.CylinderGeometry(0.35, 0.35, 0.08, 16);
            const narutoMat = new THREE.MeshStandardMaterial({ color: 0xffffff });
            const naruto = new THREE.Mesh(narutoGeo, narutoMat);
            naruto.position.set(0.3, 0.4, 0.2);
            group.add(naruto);

            // Chopsticks
            const stickGeo = new THREE.CylinderGeometry(0.04, 0.03, 2.2, 8);
            const stickMat = new THREE.MeshStandardMaterial({ color: 0x78350f, roughness: 0.7 });
            const stick1 = new THREE.Mesh(stickGeo, stickMat);
            stick1.position.set(0, 0.6, 0);
            stick1.rotation.z = Math.PI / 2.8;
            group.add(stick1);
            return group;
        },

        friedChicken: () => {
            const group = new THREE.Group();
            // Meat
            const meatGeo = new THREE.SphereGeometry(0.85, 20, 20);
            meatGeo.scale(1.2, 0.9, 0.9);
            const meatMat = new THREE.MeshStandardMaterial({
                color: 0xc2410c,
                roughness: 0.9,
                bumpScale: 0.1
            });
            const meat = new THREE.Mesh(meatGeo, meatMat);
            group.add(meat);

            // Bone
            const boneGeo = new THREE.CylinderGeometry(0.12, 0.12, 0.9, 12);
            const boneMat = new THREE.MeshStandardMaterial({ color: 0xf1f5f9, roughness: 0.4 });
            const bone = new THREE.Mesh(boneGeo, boneMat);
            bone.position.set(0.9, -0.3, 0);
            bone.rotation.z = Math.PI / 3;
            group.add(bone);
            return group;
        },

        saladBowl: () => {
            const group = new THREE.Group();
            const bowlGeo = new THREE.SphereGeometry(1.3, 24, 16, 0, Math.PI * 2, Math.PI / 2, Math.PI / 2);
            const bowlMat = new THREE.MeshStandardMaterial({ color: 0x78350f, roughness: 0.7, side: THREE.DoubleSide });
            const bowl = new THREE.Mesh(bowlGeo, bowlMat);
            bowl.rotation.x = Math.PI;
            group.add(bowl);

            // Greens
            for (let i = 0; i < 7; i++) {
                const angle = (i / 7) * Math.PI * 2;
                const leaf = new THREE.Mesh(
                    new THREE.DodecahedronGeometry(0.4),
                    new THREE.MeshStandardMaterial({ color: i % 2 === 0 ? 0x22c55e : 0x16a34a, roughness: 0.8 })
                );
                leaf.position.set(Math.cos(angle) * 0.65, 0.15, Math.sin(angle) * 0.65);
                group.add(leaf);
            }
            // Tomato cubes
            const tom = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.3, 0.3), new THREE.MeshStandardMaterial({ color: 0xef4444 }));
            tom.position.set(0.1, 0.3, 0.2);
            group.add(tom);
            return group;
        },

        // B. Travel & Transport
        airplane: () => {
            const group = new THREE.Group();
            // Fuselage
            const fuseGeo = new THREE.CylinderGeometry(0.35, 0.35, 2.8, 24);
            const whiteMat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.25, metalness: 0.2 });
            const fuse = new THREE.Mesh(fuseGeo, whiteMat);
            fuse.rotation.x = Math.PI / 2;
            group.add(fuse);

            // Nose cone
            const noseGeo = new THREE.ConeGeometry(0.35, 0.8, 24);
            const nose = new THREE.Mesh(noseGeo, whiteMat);
            nose.position.z = 1.8;
            nose.rotation.x = Math.PI / 2;
            group.add(nose);

            // Wings
            const wingGeo = new THREE.BoxGeometry(3.6, 0.06, 0.8);
            const blueMat = new THREE.MeshStandardMaterial({ color: 0x0284c7, roughness: 0.3 });
            const wings = new THREE.Mesh(wingGeo, blueMat);
            wings.position.set(0, 0, 0.2);
            group.add(wings);

            // Tail Fin
            const finGeo = new THREE.BoxGeometry(0.06, 0.8, 0.5);
            const fin = new THREE.Mesh(finGeo, blueMat);
            fin.position.set(0, 0.55, -1.2);
            group.add(fin);
            return group;
        },

        suitcase: () => {
            const group = new THREE.Group();
            // Main Body
            const bodyGeo = new THREE.BoxGeometry(1.4, 1.8, 0.7);
            const bodyMat = new THREE.MeshStandardMaterial({
                color: 0x6366f1,
                roughness: 0.2,
                metalness: 0.3
            });
            const body = new THREE.Mesh(bodyGeo, bodyMat);
            group.add(body);

            // Handle
            const handleGeo = new THREE.TorusGeometry(0.3, 0.05, 12, 24, Math.PI);
            const handleMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, metalness: 0.8 });
            const handle = new THREE.Mesh(handleGeo, handleMat);
            handle.position.set(0, 1.05, 0);
            group.add(handle);

            // 4 Wheels
            const wheelGeo = new THREE.CylinderGeometry(0.12, 0.12, 0.1, 16);
            const wheelMat = new THREE.MeshStandardMaterial({ color: 0x0f172a, roughness: 0.9 });
            [[-0.5, -1.0, 0.25], [0.5, -1.0, 0.25], [-0.5, -1.0, -0.25], [0.5, -1.0, -0.25]].forEach(pos => {
                const w = new THREE.Mesh(wheelGeo, wheelMat);
                w.rotation.z = Math.PI / 2;
                w.position.set(...pos);
                group.add(w);
            });
            return group;
        },

        train: () => {
            const group = new THREE.Group();
            // Shinkansen Bullet Body
            const bodyGeo = new THREE.BoxGeometry(1.1, 1.0, 3.2);
            const bodyMat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.2 });
            const body = new THREE.Mesh(bodyGeo, bodyMat);
            group.add(body);

            // Nose
            const noseGeo = new THREE.ConeGeometry(0.7, 1.2, 16);
            const nose = new THREE.Mesh(noseGeo, bodyMat);
            nose.position.set(0, -0.1, 2.0);
            nose.rotation.x = Math.PI / 2;
            group.add(nose);

            // Blue Speed Stripe
            const stripeGeo = new THREE.BoxGeometry(1.12, 0.14, 3.8);
            const stripeMat = new THREE.MeshStandardMaterial({ color: 0x1d4ed8, roughness: 0.3 });
            const stripe = new THREE.Mesh(stripeGeo, stripeMat);
            stripe.position.set(0, -0.15, 0.3);
            group.add(stripe);
            return group;
        },

        hotelBuilding: () => {
            const group = new THREE.Group();
            // Tower
            const towerGeo = new THREE.BoxGeometry(1.5, 2.6, 1.2);
            const towerMat = new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.4, metalness: 0.6 });
            const tower = new THREE.Mesh(towerGeo, towerMat);
            group.add(tower);

            // Glowing Windows Grid
            for (let y = -0.9; y <= 0.9; y += 0.45) {
                for (let x = -0.5; x <= 0.5; x += 0.35) {
                    const winGeo = new THREE.PlaneGeometry(0.18, 0.25);
                    const winMat = new THREE.MeshBasicMaterial({ color: 0xfef08a });
                    const win = new THREE.Mesh(winGeo, winMat);
                    win.position.set(x, y, 0.61);
                    group.add(win);
                }
            }
            return group;
        },

        // C. Office & Technology
        laptop: () => {
            const group = new THREE.Group();
            // Base Keyboard
            const baseGeo = new THREE.BoxGeometry(2.0, 0.08, 1.4);
            const metalMat = new THREE.MeshStandardMaterial({ color: 0x94a3b8, metalness: 0.8, roughness: 0.3 });
            const base = new THREE.Mesh(baseGeo, metalMat);
            group.add(base);

            // Screen Lid (Angled 115 deg)
            const screenGeo = new THREE.BoxGeometry(2.0, 1.3, 0.06);
            const screen = new THREE.Mesh(screenGeo, metalMat);
            screen.position.set(0, 0.65, -0.65);
            screen.rotation.x = -Math.PI / 10;
            group.add(screen);

            // Display Glow
            const dispGeo = new THREE.PlaneGeometry(1.85, 1.15);
            const dispMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8 });
            const disp = new THREE.Mesh(dispGeo, dispMat);
            disp.position.set(0, 0.65, -0.61);
            disp.rotation.x = -Math.PI / 10;
            group.add(disp);
            return group;
        },

        smartphone: () => {
            const group = new THREE.Group();
            const phoneGeo = new THREE.BoxGeometry(1.0, 1.9, 0.1);
            const phoneMat = new THREE.MeshStandardMaterial({ color: 0x0f172a, roughness: 0.1, metalness: 0.9 });
            const phone = new THREE.Mesh(phoneGeo, phoneMat);
            group.add(phone);

            // Screen
            const screenGeo = new THREE.PlaneGeometry(0.92, 1.78);
            const screenMat = new THREE.MeshBasicMaterial({ color: 0x818cf8 });
            const screen = new THREE.Mesh(screenGeo, screenMat);
            screen.position.z = 0.055;
            group.add(screen);
            return group;
        },

        documentStack: () => {
            const group = new THREE.Group();
            for (let i = 0; i < 4; i++) {
                const docGeo = new THREE.BoxGeometry(1.4, 0.05, 1.9);
                const docMat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.6 });
                const doc = new THREE.Mesh(docGeo, docMat);
                doc.position.y = i * 0.06;
                doc.rotation.y = (i - 1.5) * 0.08;
                group.add(doc);
            }
            // Red Stamp
            const stamp = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.2, 0.02, 16), new THREE.MeshBasicMaterial({ color: 0xef4444 }));
            stamp.position.set(0.4, 0.26, 0.5);
            group.add(stamp);
            return group;
        },

        // D. Health, Sports & Body
        dumbbell: () => {
            const group = new THREE.Group();
            // Bar
            const barGeo = new THREE.CylinderGeometry(0.08, 0.08, 1.8, 16);
            const chromeMat = new THREE.MeshStandardMaterial({ color: 0xe2e8f0, metalness: 0.9, roughness: 0.2 });
            const bar = new THREE.Mesh(barGeo, chromeMat);
            bar.rotation.z = Math.PI / 2;
            group.add(bar);

            // Plates
            const plateMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.8 });
            [-0.7, -0.5, 0.5, 0.7].forEach(x => {
                const plate = new THREE.Mesh(new THREE.CylinderGeometry(0.65, 0.65, 0.15, 24), plateMat);
                plate.rotation.z = Math.PI / 2;
                plate.position.x = x;
                group.add(plate);
            });
            return group;
        },

        medicineBottle: () => {
            const group = new THREE.Group();
            // Bottle
            const botGeo = new THREE.CylinderGeometry(0.7, 0.7, 1.6, 24);
            const glassMat = new THREE.MeshStandardMaterial({
                color: 0x0284c7,
                roughness: 0.1,
                transparent: true,
                opacity: 0.85
            });
            const bot = new THREE.Mesh(botGeo, glassMat);
            group.add(bot);

            // Cap
            const cap = new THREE.Mesh(
                new THREE.CylinderGeometry(0.5, 0.5, 0.35, 24),
                new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.3 })
            );
            cap.position.y = 0.95;
            group.add(cap);

            // Capsule inside
            const capGeo = new THREE.CapsuleGeometry ? new THREE.CapsuleGeometry(0.18, 0.4, 8, 16) : new THREE.CylinderGeometry(0.18, 0.18, 0.5, 12);
            const redMat = new THREE.MeshStandardMaterial({ color: 0xef4444 });
            const cMesh = new THREE.Mesh(capGeo, redMat);
            cMesh.position.set(0.1, -0.2, 0);
            cMesh.rotation.z = 0.4;
            group.add(cMesh);
            return group;
        },

        heartHealth: () => {
            const group = new THREE.Group();
            // Stylized 3D Heart using two spheres and a cone
            const sphere1 = new THREE.Mesh(new THREE.SphereGeometry(0.6, 24, 24), new THREE.MeshStandardMaterial({ color: 0xf43f5e, roughness: 0.2 }));
            sphere1.position.set(-0.35, 0.4, 0);
            group.add(sphere1);

            const sphere2 = new THREE.Mesh(new THREE.SphereGeometry(0.6, 24, 24), new THREE.MeshStandardMaterial({ color: 0xf43f5e, roughness: 0.2 }));
            sphere2.position.set(0.35, 0.4, 0);
            group.add(sphere2);

            const cone = new THREE.Mesh(new THREE.ConeGeometry(0.9, 1.3, 24), new THREE.MeshStandardMaterial({ color: 0xf43f5e, roughness: 0.2 }));
            cone.position.set(0, -0.2, 0);
            cone.rotation.x = Math.PI;
            group.add(cone);
            return group;
        },

        sneakerShoe: () => {
            const group = new THREE.Group();
            // Sole
            const sole = new THREE.Mesh(
                new THREE.BoxGeometry(0.9, 0.25, 2.2),
                new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.7 })
            );
            sole.position.y = -0.4;
            group.add(sole);

            // Upper
            const upper = new THREE.Mesh(
                new THREE.BoxGeometry(0.85, 0.65, 1.6),
                new THREE.MeshStandardMaterial({ color: 0x06b6d4, roughness: 0.4 })
            );
            upper.position.set(0, 0.05, -0.2);
            group.add(upper);
            return group;
        },

        // E. Festivals, Culture & Gifts
        toriiGate: () => {
            const group = new THREE.Group();
            const redMat = new THREE.MeshStandardMaterial({ color: 0xdc2626, roughness: 0.4 });
            const blackMat = new THREE.MeshStandardMaterial({ color: 0x0f172a, roughness: 0.6 });

            // Pillars
            [-0.8, 0.8].forEach(x => {
                const pillar = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.14, 2.2, 16), redMat);
                pillar.position.set(x, 0, 0);
                group.add(pillar);
            });

            // Top Kasagi Beam
            const kasagi = new THREE.Mesh(new THREE.BoxGeometry(2.3, 0.22, 0.26), blackMat);
            kasagi.position.set(0, 1.15, 0);
            group.add(kasagi);

            // Middle Shimaki Beam
            const shimaki = new THREE.Mesh(new THREE.BoxGeometry(1.9, 0.14, 0.2), redMat);
            shimaki.position.set(0, 0.75, 0);
            group.add(shimaki);
            return group;
        },

        lanternFestival: () => {
            const group = new THREE.Group();
            // Red paper body
            const bodyGeo = new THREE.SphereGeometry(1.0, 32, 24);
            bodyGeo.scale(1, 1.35, 1);
            const redMat = new THREE.MeshStandardMaterial({
                color: 0xef4444,
                roughness: 0.6,
                emissive: 0x7f1d1d,
                emissiveIntensity: 0.25
            });
            const body = new THREE.Mesh(bodyGeo, redMat);
            group.add(body);

            // Black Rims
            const rimMat = new THREE.MeshStandardMaterial({ color: 0x0f172a });
            const topRim = new THREE.Mesh(new THREE.CylinderGeometry(0.5, 0.5, 0.15, 24), rimMat);
            topRim.position.y = 1.35;
            group.add(topRim);

            const botRim = new THREE.Mesh(new THREE.CylinderGeometry(0.5, 0.5, 0.15, 24), rimMat);
            botRim.position.y = -1.35;
            group.add(botRim);

            // Gold Tassel
            const tassel = new THREE.Mesh(new THREE.ConeGeometry(0.15, 0.6, 12), new THREE.MeshStandardMaterial({ color: 0xeab308 }));
            tassel.position.y = -1.75;
            group.add(tassel);
            return group;
        },

        giftBox: () => {
            const group = new THREE.Group();
            // Box
            const boxGeo = new THREE.BoxGeometry(1.5, 1.4, 1.5);
            const boxMat = new THREE.MeshStandardMaterial({ color: 0xec4899, roughness: 0.25 });
            const box = new THREE.Mesh(boxGeo, boxMat);
            group.add(box);

            // Gold Ribbon Bands
            const goldMat = new THREE.MeshStandardMaterial({ color: 0xfacc15, metalness: 0.7, roughness: 0.3 });
            const rib1 = new THREE.Mesh(new THREE.BoxGeometry(1.52, 1.42, 0.28), goldMat);
            const rib2 = new THREE.Mesh(new THREE.BoxGeometry(0.28, 1.42, 1.52), goldMat);
            group.add(rib1);
            group.add(rib2);

            // Bow on Top
            const bow1 = new THREE.Mesh(new THREE.TorusGeometry(0.25, 0.08, 12, 20), goldMat);
            bow1.position.set(0.2, 0.85, 0);
            bow1.rotation.y = Math.PI / 4;
            const bow2 = new THREE.Mesh(new THREE.TorusGeometry(0.25, 0.08, 12, 20), goldMat);
            bow2.position.set(-0.2, 0.85, 0);
            bow2.rotation.y = -Math.PI / 4;
            group.add(bow1);
            group.add(bow2);
            return group;
        },

        japaneseFan: () => {
            const group = new THREE.Group();
            // Fan Arc
            const fanGeo = new THREE.CylinderGeometry(1.4, 0.2, 0.04, 24, 1, false, 0, Math.PI);
            const fanMat = new THREE.MeshStandardMaterial({ color: 0xf43f5e, roughness: 0.5, side: THREE.DoubleSide });
            const fan = new THREE.Mesh(fanGeo, fanMat);
            fan.rotation.x = Math.PI / 2;
            group.add(fan);

            // Bamboo Ribs
            const ribMat = new THREE.MeshStandardMaterial({ color: 0x78350f });
            for (let a = 0; a <= Math.PI; a += Math.PI / 6) {
                const rib = new THREE.Mesh(new THREE.CylinderGeometry(0.02, 0.02, 1.4, 6), ribMat);
                rib.position.set(Math.cos(a) * 0.7, 0, Math.sin(a) * 0.7);
                rib.rotation.y = -a + Math.PI / 2;
                group.add(rib);
            }
            return group;
        },

        darumaDoll: () => {
            const group = new THREE.Group();
            const bodyGeo = new THREE.SphereGeometry(1.2, 32, 32);
            bodyGeo.scale(1, 1.1, 1);
            const redMat = new THREE.MeshStandardMaterial({ color: 0xdc2626, roughness: 0.4 });
            const body = new THREE.Mesh(bodyGeo, redMat);
            group.add(body);

            // White Face Plate
            const face = new THREE.Mesh(
                new THREE.CircleGeometry(0.65, 32),
                new THREE.MeshStandardMaterial({ color: 0xf8fafc, roughness: 0.3 })
            );
            face.position.set(0, 0.2, 1.05);
            group.add(face);

            // Black Eyeballs
            [-0.22, 0.22].forEach(x => {
                const eye = new THREE.Mesh(new THREE.CircleGeometry(0.12, 16), new THREE.MeshBasicMaterial({ color: 0x0f172a }));
                eye.position.set(x, 0.28, 1.07);
                group.add(eye);
            });
            return group;
        },

        // F. Universal Signature Japanese Holographic Pedestal (Smart Fallback)
                // B. Travel, Corporate & Airport Advanced 3D Models
        airplaneTakeoff: () => {
            const group = new THREE.Group();
            const runwayGeo = new THREE.BoxGeometry(1.8, 0.1, 4.2);
            const runwayMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.8 });
            const runway = new THREE.Mesh(runwayGeo, runwayMat);
            runway.position.y = -0.9;
            group.add(runway);
            const stripeGeo = new THREE.BoxGeometry(0.15, 0.11, 0.9);
            const stripeMat = new THREE.MeshBasicMaterial({ color: 0xfacc15 });
            const s1 = new THREE.Mesh(stripeGeo, stripeMat); s1.position.set(0, -0.89, -1.0);
            const s2 = new THREE.Mesh(stripeGeo, stripeMat); s2.position.set(0, -0.89, 1.0);
            group.add(s1); group.add(s2);
            const plane = new THREE.Group();
            const fuselageGeo = new THREE.CylinderGeometry(0.32, 0.38, 2.6, 16);
            const planeMat = new THREE.MeshStandardMaterial({ color: 0xffffff, metalness: 0.3, roughness: 0.2 });
            const fuselage = new THREE.Mesh(fuselageGeo, planeMat);
            fuselage.rotation.x = Math.PI / 2;
            plane.add(fuselage);
            const noseGeo = new THREE.ConeGeometry(0.32, 0.7, 16);
            const nose = new THREE.Mesh(noseGeo, planeMat);
            nose.rotation.x = -Math.PI / 2; nose.position.z = 1.6;
            plane.add(nose);
            const wingGeo = new THREE.BoxGeometry(3.2, 0.05, 0.7);
            const wingMat = new THREE.MeshStandardMaterial({ color: 0x0284c7, metalness: 0.5 });
            const wings = new THREE.Mesh(wingGeo, wingMat);
            wings.position.set(0, 0, 0.1);
            plane.add(wings);
            const tailGeo = new THREE.BoxGeometry(0.08, 0.7, 0.5);
            const tail = new THREE.Mesh(tailGeo, wingMat);
            tail.position.set(0, 0.45, -1.1); tail.rotation.x = -0.3;
            plane.add(tail);
            plane.rotation.x = -0.42;
            plane.position.set(0, 0.35, -0.3);
            group.add(plane);
            return group;
        },

        airplaneLanding: () => {
            const group = new THREE.Group();
            const runwayGeo = new THREE.BoxGeometry(1.8, 0.1, 4.2);
            const runwayMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.8 });
            const runway = new THREE.Mesh(runwayGeo, runwayMat);
            runway.position.y = -0.9;
            group.add(runway);
            for (let i = -0.7; i <= 0.7; i += 0.35) {
                const lightGeo = new THREE.CylinderGeometry(0.05, 0.05, 0.14, 8);
                const lightMat = new THREE.MeshBasicMaterial({ color: 0x22c55e });
                const mLight = new THREE.Mesh(lightGeo, lightMat);
                mLight.position.set(i, -0.82, 1.8);
                group.add(mLight);
            }
            const plane = new THREE.Group();
            const fuselageGeo = new THREE.CylinderGeometry(0.32, 0.38, 2.6, 16);
            const planeMat = new THREE.MeshStandardMaterial({ color: 0xffffff, metalness: 0.3, roughness: 0.2 });
            const fuselage = new THREE.Mesh(fuselageGeo, planeMat);
            fuselage.rotation.x = Math.PI / 2;
            plane.add(fuselage);
            const noseGeo = new THREE.ConeGeometry(0.32, 0.7, 16);
            const nose = new THREE.Mesh(noseGeo, planeMat);
            nose.rotation.x = -Math.PI / 2; nose.position.z = 1.6;
            plane.add(nose);
            const wingGeo = new THREE.BoxGeometry(3.2, 0.05, 0.7);
            const wingMat = new THREE.MeshStandardMaterial({ color: 0x10b981, metalness: 0.5 });
            const wings = new THREE.Mesh(wingGeo, wingMat);
            wings.position.set(0, 0, 0.1);
            plane.add(wings);
            plane.rotation.x = 0.22;
            plane.position.set(0, -0.38, 0.2);
            group.add(plane);
            return group;
        },

        briefcase: () => {
            const group = new THREE.Group();
            const bodyGeo = new THREE.BoxGeometry(2.2, 1.5, 0.65);
            const bodyMat = new THREE.MeshStandardMaterial({ color: 0x451a03, roughness: 0.35, metalness: 0.15 });
            const body = new THREE.Mesh(bodyGeo, bodyMat);
            group.add(body);
            const goldMat = new THREE.MeshStandardMaterial({ color: 0xf59e0b, metalness: 0.85, roughness: 0.2 });
            [-0.55, 0.55].forEach(x => {
                const latchGeo = new THREE.BoxGeometry(0.16, 0.22, 0.68);
                const latch = new THREE.Mesh(latchGeo, goldMat);
                latch.position.set(x, 0.35, 0);
                group.add(latch);
            });
            const handleGeo = new THREE.TorusGeometry(0.35, 0.06, 8, 16, Math.PI);
            const handle = new THREE.Mesh(handleGeo, bodyMat);
            handle.position.set(0, 0.75, 0);
            group.add(handle);
            return group;
        },

        officeBuilding: () => {
            const group = new THREE.Group();
            const towerGeo = new THREE.BoxGeometry(1.6, 2.6, 1.2);
            const towerMat = new THREE.MeshStandardMaterial({ color: 0x1e3a8a, metalness: 0.7, roughness: 0.25 });
            const tower = new THREE.Mesh(towerGeo, towerMat);
            tower.position.y = 0.2;
            group.add(tower);
            const winMat = new THREE.MeshBasicMaterial({ color: 0x93c5fd });
            for (let y = -0.7; y <= 1.1; y += 0.45) {
                for (let x = -0.55; x <= 0.55; x += 0.55) {
                    const winGeo = new THREE.PlaneGeometry(0.32, 0.24);
                    const win = new THREE.Mesh(winGeo, winMat);
                    win.position.set(x, y + 0.2, 0.61);
                    group.add(win);
                }
            }
            const canopyGeo = new THREE.BoxGeometry(0.9, 0.08, 0.4);
            const canopyMat = new THREE.MeshStandardMaterial({ color: 0x38bdf8 });
            const canopy = new THREE.Mesh(canopyGeo, canopyMat);
            canopy.position.set(0, -0.7, 0.8);
            group.add(canopy);
            return group;
        },

        headquartersTower: () => {
            const group = new THREE.Group();
            const mainGeo = new THREE.BoxGeometry(1.4, 3.2, 1.4);
            const mainMat = new THREE.MeshStandardMaterial({ color: 0x0f172a, metalness: 0.8, roughness: 0.15 });
            const mainTower = new THREE.Mesh(mainGeo, mainMat);
            mainTower.position.y = 0.3;
            group.add(mainTower);
            const glassGeo = new THREE.BoxGeometry(1.42, 2.8, 0.8);
            const glassMat = new THREE.MeshStandardMaterial({ color: 0x6366f1, metalness: 0.9, roughness: 0.1, transparent: true, opacity: 0.75 });
            const glass = new THREE.Mesh(glassGeo, glassMat);
            glass.position.y = 0.3;
            group.add(glass);
            const spireGeo = new THREE.CylinderGeometry(0.04, 0.12, 1.1, 8);
            const spireMat = new THREE.MeshStandardMaterial({ color: 0xf59e0b, metalness: 0.9 });
            const spire = new THREE.Mesh(spireGeo, spireMat);
            spire.position.y = 2.4;
            group.add(spire);
            return group;
        },

        clockGlobe: () => {
            const group = new THREE.Group();
            const earthGeo = new THREE.SphereGeometry(1.1, 32, 32);
            const earthMat = new THREE.MeshStandardMaterial({ color: 0x0284c7, metalness: 0.3, roughness: 0.6 });
            const earth = new THREE.Mesh(earthGeo, earthMat);
            group.add(earth);
            const ringGeo = new THREE.TorusGeometry(1.4, 0.05, 16, 64);
            const ringMat = new THREE.MeshBasicMaterial({ color: 0xfacc15 });
            const ring = new THREE.Mesh(ringGeo, ringMat);
            ring.rotation.x = Math.PI / 4;
            group.add(ring);
            const clockGeo = new THREE.CylinderGeometry(0.5, 0.5, 0.1, 32);
            const clockMat = new THREE.MeshStandardMaterial({ color: 0xffffff });
            const clock = new THREE.Mesh(clockGeo, clockMat);
            clock.rotation.x = Math.PI / 2;
            clock.position.set(0, 0, 1.25);
            group.add(clock);
            return group;
        },

        hotWaterShower: () => {
            const group = new THREE.Group();
            const pipeCurve = new THREE.CubicBezierCurve3(
                new THREE.Vector3(-0.6, -1.0, 0),
                new THREE.Vector3(-0.6, 1.2, 0),
                new THREE.Vector3(0.3, 1.3, 0),
                new THREE.Vector3(0.5, 0.8, 0)
            );
            const pipeGeo = new THREE.TubeGeometry(pipeCurve, 32, 0.07, 12, false);
            const chromeMat = new THREE.MeshStandardMaterial({ color: 0xe2e8f0, metalness: 0.95, roughness: 0.1 });
            const pipe = new THREE.Mesh(pipeGeo, chromeMat);
            group.add(pipe);
            const headGeo = new THREE.ConeGeometry(0.35, 0.3, 16);
            const head = new THREE.Mesh(headGeo, chromeMat);
            head.position.set(0.5, 0.65, 0); head.rotation.z = Math.PI;
            group.add(head);
            const waterMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8, transparent: true, opacity: 0.65 });
            for (let i = -0.2; i <= 0.2; i += 0.1) {
                const dropGeo = new THREE.CylinderGeometry(0.015, 0.015, 0.7, 6);
                const drop = new THREE.Mesh(dropGeo, waterMat);
                drop.position.set(0.5 + i, 0.1, (i * 0.5));
                group.add(drop);
            }
            return group;
        },

        calendarSchedule: () => {
            const group = new THREE.Group();
            const standGeo = new THREE.BoxGeometry(2.0, 1.6, 0.2);
            const standMat = new THREE.MeshStandardMaterial({ color: 0xdc2626 });
            const stand = new THREE.Mesh(standGeo, standMat);
            group.add(stand);
            const pageGeo = new THREE.BoxGeometry(1.8, 1.3, 0.08);
            const pageMat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.9 });
            const page = new THREE.Mesh(pageGeo, pageMat);
            page.position.set(0, -0.1, 0.12);
            group.add(page);
            return group;
        },

        key3D: () => {
            const group = new THREE.Group();
            const goldMat = new THREE.MeshStandardMaterial({ color: 0xf59e0b, metalness: 0.85, roughness: 0.2 });
            const headGeo = new THREE.TorusGeometry(0.45, 0.12, 12, 32);
            const head = new THREE.Mesh(headGeo, goldMat);
            head.position.y = 0.8;
            group.add(head);
            const shaftGeo = new THREE.CylinderGeometry(0.1, 0.1, 1.4, 16);
            const shaft = new THREE.Mesh(shaftGeo, goldMat);
            shaft.position.y = 0.1;
            group.add(shaft);
            const teethGeo = new THREE.BoxGeometry(0.35, 0.45, 0.15);
            const teeth = new THREE.Mesh(teethGeo, goldMat);
            teeth.position.set(0.18, -0.35, 0);
            group.add(teeth);
            return group;
        },

        conferenceRoom: () => {
            const group = new THREE.Group();
            const tableGeo = new THREE.CylinderGeometry(1.6, 1.6, 0.15, 32);
            const tableMat = new THREE.MeshStandardMaterial({ color: 0x451a03, roughness: 0.3 });
            const table = new THREE.Mesh(tableGeo, tableMat);
            table.position.y = -0.3;
            group.add(table);
            const legGeo = new THREE.CylinderGeometry(0.25, 0.4, 0.8, 16);
            const leg = new THREE.Mesh(legGeo, tableMat);
            leg.position.y = -0.7;
            group.add(leg);
            return group;
        },

        handshakeMeeting: () => {
            const group = new THREE.Group();
            const baseGeo = new THREE.CylinderGeometry(1.6, 1.7, 0.25, 32);
            const baseMat = new THREE.MeshStandardMaterial({ color: 0x0284c7, metalness: 0.3 });
            const base = new THREE.Mesh(baseGeo, baseMat);
            base.position.y = -0.9;
            group.add(base);
            const signGeo = new THREE.BoxGeometry(2.0, 1.2, 0.1);
            const signMat = new THREE.MeshStandardMaterial({ color: 0xffffff });
            const sign = new THREE.Mesh(signGeo, signMat);
            sign.position.y = 0.2;
            group.add(sign);
            return group;
        },

        comfortLounge: () => {
            const group = new THREE.Group();
            const fabricMat = new THREE.MeshStandardMaterial({ color: 0x4f46e5, roughness: 0.8 });
            const seatGeo = new THREE.BoxGeometry(1.6, 0.35, 1.4);
            const seat = new THREE.Mesh(seatGeo, fabricMat);
            seat.position.y = -0.3;
            group.add(seat);
            const backGeo = new THREE.BoxGeometry(1.6, 1.0, 0.35);
            const back = new THREE.Mesh(backGeo, fabricMat);
            back.position.set(0, 0.3, -0.55);
            group.add(back);
            return group;
        },

universalPrism: (word) => {
            const group = new THREE.Group();

            // 1. Lacquered Hexagonal Base Pedestal
            const baseGeo = new THREE.CylinderGeometry(1.6, 1.8, 0.35, 6);
            const baseMat = new THREE.MeshStandardMaterial({
                color: 0x0f172a,
                metalness: 0.8,
                roughness: 0.2
            });
            const base = new THREE.Mesh(baseGeo, baseMat);
            base.position.y = -1.1;
            group.add(base);

            // Neon Glowing Trim Ring
            const ringGeo = new THREE.TorusGeometry(1.65, 0.04, 16, 6);
            const ringMat = new THREE.MeshBasicMaterial({ color: 0x6366f1 });
            const ring = new THREE.Mesh(ringGeo, ringMat);
            ring.rotation.x = Math.PI / 2;
            ring.position.y = -0.92;
            group.add(ring);

            // 2. Floating Octahedron Gemstone / Prism
            const prismGeo = new THREE.OctahedronGeometry(1.0, 0);
            const prismMat = new THREE.MeshStandardMaterial({
                color: 0x818cf8,
                metalness: 0.3,
                roughness: 0.1,
                transparent: true,
                opacity: 0.85,
                wireframe: false
            });
            const prism = new THREE.Mesh(prismGeo, prismMat);
            prism.position.y = 0.2;
            group.add(prism);

            // 3. Orbiting Particle Ring
            const particleGeo = new THREE.BufferGeometry();
            const pCount = 36;
            const pCoords = [];
            for (let i = 0; i < pCount; i++) {
                const theta = (i / pCount) * Math.PI * 2;
                const r = 1.45 + (Math.random() - 0.5) * 0.2;
                pCoords.push(Math.cos(theta) * r, 0.2 + (Math.random() - 0.5) * 0.3, Math.sin(theta) * r);
            }
            particleGeo.setAttribute('position', new THREE.Float32BufferAttribute(pCoords, 3));
            const pMat = new THREE.PointsMaterial({ color: 0xfbbf24, size: 0.08 });
            const pSystem = new THREE.Points(particleGeo, pMat);
            group.add(pSystem);

            return group;
        }
    };

    // Category / Keyword Matcher for Procedural Models
    function resolveModelForVocab(v) {
        const text = `${v.jp || ''} ${v.kana || ''} ${v.kanji || ''} ${v.romaji || ''} ${v.vi || ''} ${v.badge || ''} ${v.cat || ''}`.toLowerCase();

        // 1. Food & Drink
        if (text.includes('くだもの') || text.includes('果物') || text.includes('りんご') || text.includes('hoa quả') || text.includes('trái cây')) return ModelGenerators.apple();
        if (text.includes('いちご') || text.includes('dâu tây')) return ModelGenerators.strawberry();
        if (text.includes('おにぎり') || text.includes('お握り') || text.includes('cơm nắm')) return ModelGenerators.onigiri();
        if (text.includes('サンドイッチ') || text.includes('sandwich')) return ModelGenerators.sandwich();
        if (text.includes('おさけ') || text.includes('お酒') || text.includes('rượu') || text.includes('đồ uống')) return ModelGenerators.sakeBottle();
        if (text.includes('ラーメン') || text.includes('mì') || text.includes('nước súp')) return ModelGenerators.ramenBowl();
        if (text.includes('からあげ') || text.includes('から揚げ') || text.includes('gà rán') || text.includes('thịt')) return ModelGenerators.friedChicken();
        if (text.includes('サラダ') || text.includes('salad') || text.includes('rau')) return ModelGenerators.saladBowl();

        // 2. Travel & Transport
        if (text.includes('ひこうき') || text.includes('飛行機') || text.includes('フライト') || text.includes('máy bay')) return ModelGenerators.airplane();
        if (text.includes('スーツケース') || text.includes('vali') || text.includes('hành lý') || text.includes('かばん')) return ModelGenerators.suitcase();
        if (text.includes('しんかんせん') || text.includes('でんしゃ') || text.includes('tàu')) return ModelGenerators.train();
        if (text.includes('ホテル') || text.includes('khách sạn') || text.includes('tòa nhà')) return ModelGenerators.hotelBuilding();

        // 3. Office & Workplace
        if (text.includes('パソコン') || text.includes('máy tính') || text.includes('laptop')) return ModelGenerators.laptop();
        if (text.includes('スマホ') || text.includes('điện thoại')) return ModelGenerators.smartphone();
        if (text.includes('しょるい') || text.includes('tài liệu') || text.includes('hồ sơ') || text.includes('báo cáo')) return ModelGenerators.documentStack();

        // 4. Health & Exercise
        if (text.includes('ダンベル') || text.includes('tập tạ') || text.includes('thể thao')) return ModelGenerators.dumbbell();
        if (text.includes('くすり') || text.includes('thuốc') || text.includes('bệnh viện')) return ModelGenerators.medicineBottle();
        if (text.includes('けんこう') || text.includes('tim') || text.includes('sức khỏe')) return ModelGenerators.heartHealth();
        if (text.includes('ジョギング') || text.includes('chạy bộ') || text.includes('giày')) return ModelGenerators.sneakerShoe();

        // 5. Festival, Culture & Celebration
        if (text.includes('とりい') || text.includes('鳥居') || text.includes('cổng torii') || text.includes('đền')) return ModelGenerators.toriiGate();
        if (text.includes('ちょうちん') || text.includes('đèn lồng')) return ModelGenerators.lanternFestival();
        if (text.includes('プレゼント') || text.includes('quà') || text.includes('chúc mừng') || text.includes('おいわい')) return ModelGenerators.giftBox();
        if (text.includes('せんす') || text.includes('うちわ') || text.includes('quạt')) return ModelGenerators.japaneseFan();
        if (text.includes('だるま') || text.includes('daruma')) return ModelGenerators.darumaDoll();

                // 6. Corporate, Travel & Business (Lesson 13-18 Specialized)
        if (text.includes('しゅっぱつ') || text.includes('出発') || text.includes('xuất phát') || text.includes('khởi hành') || text.includes('cất cánh')) return ModelGenerators.airplaneTakeoff();
        if (text.includes('とうちゃく') || text.includes('到着') || text.includes('đến nơi') || text.includes('hạ cánh')) return ModelGenerators.airplaneLanding();
        if (text.includes('しゅっちょう') || text.includes('出張') || text.includes('công tác')) return ModelGenerators.briefcase();
        if (text.includes('ししゃ') || text.includes('支社') || text.includes('chi nhánh')) return ModelGenerators.officeBuilding();
        if (text.includes('ほんしゃ') || text.includes('本社') || text.includes('trụ sở')) return ModelGenerators.headquartersTower();
        if (text.includes('じさ') || text.includes('時差') || text.includes('múi giờ')) return ModelGenerators.clockGlobe();
        if (text.includes('おゆ') || text.includes('お湯') || text.includes('nước nóng') || text.includes('vòi')) return ModelGenerators.hotWaterShower();
        if (text.includes('スケジュール') || text.includes('lịch trình')) return ModelGenerators.calendarSchedule();
        if (text.includes('かぎ') || text.includes('鍵') || text.includes('chìa khóa')) return ModelGenerators.key3D();
        if (text.includes('かいぎ') || text.includes('会議') || text.includes('cuộc họp') || text.includes('họp')) return ModelGenerators.conferenceRoom();
        if (text.includes('でむかえ') || text.includes('出迎え') || text.includes('あいさつ') || text.includes('挨拶') || text.includes('ようこそ')) return ModelGenerators.handshakeMeeting();
        if (text.includes('かいてき') || text.includes('快適') || text.includes('tiện nghi') || text.includes('thoải mái')) return ModelGenerators.comfortLounge();
        if (text.includes('おつかれ') || text.includes('お疲れ') || text.includes('いかが')) return ModelGenerators.sakeBottle();
        if (text.includes('チェック') || text.includes('kiểm tra')) return ModelGenerators.documentStack();


// Universal Signature 3D Holo-Pedestal for all other words
        return ModelGenerators.universalPrism(v);
    }

    // --- 2. THREE.JS 3D STUDIO MODAL SETUP ---
    function initStudioModal() {
        if (document.getElementById('vocab3DModal')) return;

        const modalHtml = `
        <div class="vocab-3d-modal-overlay" id="vocab3DModal">
            <div class="vocab-3d-studio-window">
                <!-- Header -->
                <div class="v3d-header">
                    <div class="v3d-title-group">
                        <span class="v3d-badge">Marugoto 3D Studio</span>
                        <h3 class="v3d-title">Không Gian Mô Hình 3D Tương Tác</h3>
                    </div>
                    <button type="button" class="v3d-close-btn" onclick="closeVocab3DModal()" title="Đóng cửa sổ 3D (Esc)">✕</button>
                </div>

                <!-- Body -->
                <div class="v3d-body">
                    <!-- 3D Canvas Viewport -->
                    <div class="v3d-viewport-container" id="v3dViewport">
                        <canvas id="v3dCanvas"></canvas>
                        <div class="v3d-hint-text">🖱️ Xoay 360° chuột trái • Cuộn để phóng to/thu nhỏ</div>

                        <!-- 3D Tool Controls -->
                        <div class="v3d-controls-overlay">
                            <button type="button" class="v3d-tool-btn active" id="btnToggleRotate" onclick="toggle3DAutoRotate()">🔄 Xoay 360°</button>
                            <button type="button" class="v3d-tool-btn" id="btnAnimFloat" onclick="set3DAnimMode('float')">✨ Nổi</button>
                            <button type="button" class="v3d-tool-btn" id="btnAnimSpin" onclick="set3DAnimMode('spin')">🌪️ Xoay nhanh</button>
                            <button type="button" class="v3d-tool-btn" id="btnAnimWireframe" onclick="toggle3DWireframe()">📐 Khung dây</button>
                        </div>
                    </div>

                    <!-- Vocab Info Details Panel -->
                    <div class="v3d-info-panel">
                        <div>
                            <div class="v3d-kanji-banner">
                                <div class="v3d-kanji-big jp-text" id="v3dKanji">果物</div>
                                <button type="button" class="v3d-speak-btn" id="v3dSpeakBtn" onclick="speakCurrent3DVocab()" title="Nghe phát âm chuẩn Tokyo">🔊</button>
                            </div>
                            <div class="v3d-kana-line jp-text" id="v3dKana">くだもの</div>
                            <div class="v3d-romaji-line" id="v3dRomaji">kudamono</div>

                            <div class="v3d-meaning-box">
                                <div class="v3d-meaning-label">Nghĩa tiếng Việt</div>
                                <div class="v3d-meaning-text" id="v3dVi">Hoa quả, trái cây tươi</div>
                            </div>

                            <div class="v3d-example-box" id="v3dExBox">
                                <div class="v3d-ex-jp jp-text" id="v3dExJp">ピクニックに くだものを もっていきます。</div>
                                <div class="v3d-ex-vi" id="v3dExVi">Tôi sẽ mang hoa quả đi dã ngoại.</div>
                            </div>
                        </div>

                        <!-- Navigation Bar -->
                        <div class="v3d-nav-bar">
                            <button type="button" class="v3d-nav-btn" onclick="prev3DVocab()">◀ Từ trước</button>
                            <span class="v3d-nav-counter" id="v3dCounter">1 / 28</span>
                            <button type="button" class="v3d-nav-btn" onclick="next3DVocab()">Từ tiếp theo ▶</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        `;

        document.body.insertAdjacentHTML('beforeend', modalHtml);
        initThreeJsViewport();
    }

    function initThreeJsViewport() {
        const container = document.getElementById('v3dViewport');
        const canvas = document.getElementById('v3dCanvas');
        if (!container || !canvas || typeof THREE === 'undefined') return;

        // Scene
        scene = new THREE.Scene();

        // Camera
        const width = container.clientWidth || 550;
        const height = container.clientHeight || 450;
        camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 100);
        camera.position.set(0, 1.8, 5.2);

        // Renderer with antialias and shadows
        renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
        renderer.setSize(width, height);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        renderer.shadowMap.enabled = true;
        renderer.shadowMap.type = THREE.PCFSoftShadowMap;

        // Lighting Studio Setup
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.85);
        scene.add(ambientLight);

        const keyLight = new THREE.DirectionalLight(0xffffff, 1.2);
        keyLight.position.set(5, 8, 5);
        keyLight.castShadow = true;
        scene.add(keyLight);

        const fillLight = new THREE.DirectionalLight(0x818cf8, 0.6);
        fillLight.position.set(-5, 3, -3);
        scene.add(fillLight);

        const rimLight = new THREE.PointLight(0xf43f5e, 1.0, 15);
        rimLight.position.set(0, 4, -4);
        scene.add(rimLight);

        // OrbitControls
        if (typeof THREE.OrbitControls !== 'undefined') {
            controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;
            controls.maxDistance = 10;
            controls.minDistance = 2;
            controls.autoRotate = isAutoRotating;
            controls.autoRotateSpeed = 2.2;
        }

        // Render Loop
        let clock = new THREE.Clock();
        function animate() {
            animFrameId = requestAnimationFrame(animate);
            const delta = clock.getDelta();
            const time = clock.getElapsedTime();

            if (controls) controls.update();

            // Custom Motion Animation on the active 3D model
            if (currentModelGroup) {
                if (animMode === 'float') {
                    currentModelGroup.position.y = Math.sin(time * 2.2) * 0.12;
                    currentModelGroup.rotation.y += 0.005;
                } else if (animMode === 'spin') {
                    currentModelGroup.rotation.y += 0.05;
                    currentModelGroup.position.y = Math.sin(time * 4) * 0.18;
                } else if (animMode === 'pulse') {
                    const s = 1.0 + Math.sin(time * 5) * 0.08;
                    currentModelGroup.scale.set(s, s, s);
                }
            }

            renderer.render(scene, camera);
        }
        animate();

        // Responsive Resize
        window.addEventListener('resize', () => {
            if (!container || !renderer || !camera) return;
            const w = container.clientWidth;
            const h = container.clientHeight;
            if (w === 0 || h === 0) return;
            camera.aspect = w / h;
            camera.updateProjectionMatrix();
            renderer.setSize(w, h);
        });

        isInitialized = true;
    }

    // Load active 3D model in studio
    function displayVocabIn3D(v, index) {
        if (!scene) return;
        currentVocabIndex = index;

        // Clear previous 3D model
        if (currentModelGroup) {
            scene.remove(currentModelGroup);
            currentModelGroup = null;
        }

        // Generate procedural 3D model
        currentModelGroup = resolveModelForVocab(v);
        scene.add(currentModelGroup);

        // Reset camera focus
        if (controls) {
            controls.target.set(0, 0, 0);
            camera.position.set(0, 1.6, 5.0);
        }

        // Update UI details
        const kanjiEl = document.getElementById('v3dKanji');
        const kanaEl = document.getElementById('v3dKana');
        const romajiEl = document.getElementById('v3dRomaji');
        const viEl = document.getElementById('v3dVi');
        const exJpEl = document.getElementById('v3dExJp');
        const exViEl = document.getElementById('v3dExVi');
        const counterEl = document.getElementById('v3dCounter');

        if (kanjiEl) kanjiEl.textContent = v.kanji || v.jp;
        if (kanaEl) kanaEl.textContent = v.kana || v.jp;
        if (romajiEl) romajiEl.textContent = v.romaji || '';
        if (viEl) viEl.textContent = v.vi || '';
        if (exJpEl) exJpEl.textContent = v.exJp || v.jp;
        if (exViEl) exViEl.textContent = v.exVi || v.vi;
        if (counterEl) counterEl.textContent = `${index + 1} / ${currentVocabList.length}`;
    }

    // --- 3. PUBLIC API & CONTROLS ---
    window.openVocab3D = function (index) {
        initStudioModal();
        currentVocabList = window.VOCAB_DATA || [];
        if (!currentVocabList || currentVocabList.length === 0) return;

        if (index < 0) index = 0;
        if (index >= currentVocabList.length) index = currentVocabList.length - 1;

        const modal = document.getElementById('vocab3DModal');
        if (modal) {
            modal.classList.add('show');
            document.body.style.overflow = 'hidden';
        }

        // Trigger resize calculation
        setTimeout(() => {
            const container = document.getElementById('v3dViewport');
            if (container && renderer && camera) {
                const w = container.clientWidth;
                const h = container.clientHeight;
                camera.aspect = w / h;
                camera.updateProjectionMatrix();
                renderer.setSize(w, h);
            }
            displayVocabIn3D(currentVocabList[index], index);
        }, 60);
    };

    window.closeVocab3DModal = function () {
        const modal = document.getElementById('vocab3DModal');
        if (modal) modal.classList.remove('show');
        document.body.style.overflow = '';
    };

    window.prev3DVocab = function () {
        if (!currentVocabList || currentVocabList.length === 0) return;
        const nextIdx = (currentVocabIndex - 1 + currentVocabList.length) % currentVocabList.length;
        displayVocabIn3D(currentVocabList[nextIdx], nextIdx);
    };

    window.next3DVocab = function () {
        if (!currentVocabList || currentVocabList.length === 0) return;
        const nextIdx = (currentVocabIndex + 1) % currentVocabList.length;
        displayVocabIn3D(currentVocabList[nextIdx], nextIdx);
    };

    window.speakCurrent3DVocab = function () {
        if (!currentVocabList || !currentVocabList[currentVocabIndex]) return;
        const v = currentVocabList[currentVocabIndex];
        const text = v.jp || v.kanji || v.kana;
        if (typeof window.speakText === 'function') {
            window.speakText(text);
        } else if ('speechSynthesis' in window) {
            const utter = new SpeechSynthesisUtterance(text);
            utter.lang = 'ja-JP';
            window.speechSynthesis.speak(utter);
        }
    };

    window.toggle3DAutoRotate = function () {
        if (!controls) return;
        isAutoRotating = !isAutoRotating;
        controls.autoRotate = isAutoRotating;
        const btn = document.getElementById('btnToggleRotate');
        if (btn) btn.classList.toggle('active', isAutoRotating);
    };

    window.set3DAnimMode = function (mode) {
        animMode = mode;
        ['btnAnimFloat', 'btnAnimSpin'].forEach(id => {
            const el = document.getElementById(id);
            if (el) el.classList.remove('active');
        });
        if (mode === 'float') document.getElementById('btnAnimFloat')?.classList.add('active');
        if (mode === 'spin') document.getElementById('btnAnimSpin')?.classList.add('active');
    };

    let isWireframeOn = false;
    window.toggle3DWireframe = function () {
        if (!currentModelGroup) return;
        isWireframeOn = !isWireframeOn;
        currentModelGroup.traverse(child => {
            if (child.isMesh && child.material) {
                child.material.wireframe = isWireframeOn;
            }
        });
        const btn = document.getElementById('btnAnimWireframe');
        if (btn) btn.classList.toggle('active', isWireframeOn);
    };

    // Keyboard Shortcuts (Arrow Left/Right, ESC)
    window.addEventListener('keydown', (e) => {
        const modal = document.getElementById('vocab3DModal');
        if (!modal || !modal.classList.contains('show')) return;
        if (e.key === 'Escape') closeVocab3DModal();
        if (e.key === 'ArrowLeft') prev3DVocab();
        if (e.key === 'ArrowRight') next3DVocab();
        if (e.key === ' ' || e.key === 'Enter') {
            e.preventDefault();
            speakCurrent3DVocab();
        }
    });

    // --- 4. FLASHCARD 3D PARALLAX TILT & STAGE ENHANCEMENT ---
    window.enhanceFlashcards3D = function () {
        const stages = document.querySelectorAll('.fc-3d-stage');
        stages.forEach(stage => {
            const wrapper = stage.querySelector('.fc-3d-model-wrapper');
            if (!wrapper) return;

            stage.addEventListener('mousemove', (e) => {
                const rect = stage.getBoundingClientRect();
                const x = e.clientX - rect.left - rect.width / 2;
                const y = e.clientY - rect.top - rect.height / 2;
                const rotateX = -(y / (rect.height / 2)) * 18;
                const rotateY = (x / (rect.width / 2)) * 22;
                wrapper.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.08, 1.08, 1.08)`;
            });

            stage.addEventListener('mouseleave', () => {
                wrapper.style.transform = 'rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
            });
        });
    };

    // Auto-hook on DOM load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            window.enhanceFlashcards3D();
        });
    } else {
        window.enhanceFlashcards3D();
    }

})(window, document);
