/* ==========================================================================
   ⛩️ DEMO 3D - KIMETSU NO YAIBA MT. FUJIKASANE WISTERIA SHRINE
   WebGL Interactive Experience (Three.js r128)
   ========================================================================== */

let scene, camera, renderer, controls;
let isNight = true;
let autoRotate = false;
let particlesActive = true;
let isCinematic = false; // Start in interactive mode for instant user control
let soundChimeEnabled = true;

// Lights
let dirLight, ambientLight, moonRimLight, katanaSpotLight;
let lanternPointLights = [];
let wisteriaGlowLights = [];

// Particle Systems
let sakuraGeo, sakuraParticles;
let wisteriaGeo, wisteriaParticles;
let fireflyGeo, fireflyParticles;

// God Rays & Moon Meshes
let godRaysGroup;
let moonMesh, moonHaloMesh;

// Model Object References & Raycasting
const models = {};
const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();

// Camera Smooth Glide Transition State
let isTransitioning = false;
let transitionStartTime = 0;
let transitionDuration = 900; // ms
const transitionStartCam = new THREE.Vector3();
const transitionStartTarget = new THREE.Vector3();
const transitionEndCam = new THREE.Vector3();
const transitionEndTarget = new THREE.Vector3();

// Cinematic Camera Roam parameters
let cinematicAngle = 0;
const cinematicRadius = 11.5;
const cinematicHeight = 3.6;

// Audio Context for Procedural Shinto Temple Bell / Chime
let audioCtx = null;

// ==========================================================================
// CULTURAL VOCABULARY & DEMON SLAYER LORE DATABASE
// ==========================================================================
const VOCAB_KEYS = ['torii', 'katana', 'wisteria', 'lantern', 'fuji', 'daruma', 'neko', 'sakura'];
let currentVocabIndex = 0;

const VOCAB_DATABASE = {
    torii: {
        key: 'torii',
        tag: 'Kiến trúc Thần đạo • Mt. Fujikasane',
        kanji: '鳥居',
        romaji: 'Torii',
        kana: 'とりい (Torii)',
        meaning: 'Cổng Thần đạo truyền thống sơn đỏ chu sa rực rỡ, phân định ranh giới giữa cõi trần và chốn thần linh.',
        culture: '⛩️ Trong anime Kimetsu no Yaiba, cổng Torii sừng sững tại lối vào Đỉnh Núi Tử Đằng (藤襲山 - Fujikasane). Nơi đây treo dây thừng thiêng Shimenawa và giấy trắng Shide, là điểm khởi đầu cho kỳ Tuyển Chọn Cuối Cùng (最終選別 - Saishū Senbetsu).',
        camPos: new THREE.Vector3(0, 3.0, 7.5),
        lookAt: new THREE.Vector3(0, 2.6, 0)
    },
    katana: {
        key: 'katana',
        tag: 'Bảo kiếm Diệt Quỷ • Sát Quỷ Đội',
        kanji: '日輪刀',
        romaji: 'Nichirin-tō',
        kana: 'にちりんとう (Nichirin-tō)',
        meaning: 'Thanh kiếm Nichirin rèn từ Cát sắt đỏ và Quặng đỏ thẫm hấp thụ ánh sáng mặt trời vĩnh cửu.',
        culture: '⚔️ Vũ khí tối thượng của các kiếm sĩ Sát Quỷ Đội (鬼殺隊). Lưỡi kiếm rèn thủ công cong vút uyển chuyển với vân Hamon sắc lẹm, tsuba rực lửa và bao kiếm sơn mài đen tuyền đặt trang trọng trên giá Katanakake.',
        camPos: new THREE.Vector3(2.4, 1.35, 2.8),
        lookAt: new THREE.Vector3(2.4, 0.85, 1.2)
    },
    wisteria: {
        key: 'wisteria',
        tag: 'Thần Mộc Xua Quỷ • Kimetsu no Yaiba',
        kanji: '藤の花',
        romaji: 'Fuji no hana',
        kana: 'ふじのはな (Fuji no hana)',
        meaning: 'Hoa Tử Đằng linh thiêng với những chùm hoa tím biếc rủ xuống như thác nước huyền ảo.',
        culture: '🪻 Loài hoa nở rộ bốn mùa trên đỉnh núi Fujikasane. Hương thơm và độc tố của hoa Tử Đằng là khắc tinh số một khiến loài quỷ khiếp sợ và không bao giờ dám đến gần, tạo thành kết giới thiêng liêng bảo vệ loài người.',
        camPos: new THREE.Vector3(-3.2, 3.2, 4.0),
        lookAt: new THREE.Vector3(-3.8, 3.0, 1.8)
    },
    lantern: {
        key: 'lantern',
        tag: 'Dẫn Lối Thần Đạo • Cổ Kính',
        kanji: '燈籠',
        romaji: 'Tōrō',
        kana: 'とうろう (Tōrō)',
        meaning: 'Đèn lồng đá Kasuga cổ kính chạm khắc tinh xảo, thắp sáng ngọn lửa ấm áp giữa đêm sương.',
        culture: '🏮 Được đặt dọc hai bên lối vào đền thờ (Sando). Ngọn lửa thiêng bập bùng bên trong mang ý nghĩa xua tan bóng tối u ám, soi tỏ tâm hồn thanh tịnh và dẫn bước lữ khách trên con đường hướng thiện.',
        camPos: new THREE.Vector3(-2.2, 1.8, 3.6),
        lookAt: new THREE.Vector3(-2.6, 1.5, 2.2)
    },
    fuji: {
        key: 'fuji',
        tag: 'Linh Sơn Hùng Vĩ • Di Sản Thế Giới',
        kanji: '富士山',
        romaji: 'Fuji-san',
        kana: 'ふじさん (Fuji-san)',
        meaning: 'Núi Phú Sĩ tuyết phủ ngàn năm cùng ánh trăng rằm vằng vặc (満月 - Mangetsu).',
        culture: '🗻 Đỉnh núi linh thiêng cao 3.776m, biểu tượng trường tồn bất diệt của đất nước Mặt Trời Mọc. Đỉnh núi tuyết sừng sững uy nghi phía sau cổng Torii dưới ánh trăng rằm huyền ảo.',
        camPos: new THREE.Vector3(0, 3.6, 9.2),
        lookAt: new THREE.Vector3(0, 5.2, -40)
    },
    daruma: {
        key: 'daruma',
        tag: 'Búp Bê Ý Chí & Ước Nguyện',
        kanji: 'だるま',
        romaji: 'Daruma',
        kana: 'だるま (Daruma)',
        meaning: 'Búp bê tròn đỏ truyền thống tượng trưng cho tinh thần bất khuất "Thất ngã bát khởi" (Ngã 7 lần, đứng dậy 8 lần).',
        culture: '🎎 Khắc chữ vàng "Tất Thắng" (必勝) và "Phúc" (福). Người Nhật khi lập chí lớn sẽ điểm nhãn mắt trái; khi vượt qua thử thách vẻ vang sẽ vẽ nốt mắt phải để tạ ơn thần linh.',
        camPos: new THREE.Vector3(-1.4, 1.35, 2.7),
        lookAt: new THREE.Vector3(-1.8, 0.85, 1.4)
    },
    neko: {
        key: 'neko',
        tag: 'Phong Thủy Cầu May • Tài Lộc',
        kanji: '招き猫',
        romaji: 'Maneki-neko',
        kana: 'まねきねこ (Maneki-neko)',
        meaning: 'Mèo may mắn sứ trắng vẫy tay đón tài lộc, mang lục lạc vàng và đồng tiền cổ Koban.',
        culture: '🐱 Tay phải giơ cao vẫy gọi phúc lành, tiền cổ ghi khắc "Thiên vạn lượng" (千万両 - Senmanryō). Thường được bày trang trọng tại cổng vào cửa hàng, mang lại sự ấm no và bình an cho gia chủ.',
        camPos: new THREE.Vector3(-2.0, 1.25, 1.8),
        lookAt: new THREE.Vector3(-2.4, 0.75, 0.5)
    },
    sakura: {
        key: 'sakura',
        tag: 'Quốc Hoa • Vẻ Đẹp Khoảnh Khắc',
        kanji: '桜の花びら',
        romaji: 'Sakura no hanabira',
        kana: 'さくら の はなびら (Sakura)',
        meaning: 'Những cánh hoa anh đào thanh khiết chao liệng trong làn gió đêm huyền ảo.',
        culture: '🌸 Triết lý "Mono no aware" (U hoài trước vẻ đẹp phù du) - trân quý từng phút giây hiện tại. Sắc hồng hoa anh đào hòa quyện cùng sắc tím hoa Tử Đằng tạo nên bức tranh thiên nhiên tuyệt mỹ.',
        camPos: new THREE.Vector3(0, 3.4, 11.2),
        lookAt: new THREE.Vector3(0, 2.2, 0)
    }
};

let currentActiveItem = VOCAB_DATABASE.torii;

// ==========================================
// INITIALIZATION
// ==========================================
function init() {
    const canvas = document.getElementById('canvas3d');

    // 1. Scene & Atmosphere
    scene = new THREE.Scene();
    scene.background = new THREE.Color(0x060411);
    scene.fog = new THREE.FogExp2(0x0a0518, 0.016);

    // 2. Camera Setup (Balanced initial establishing composition)
    camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 250);
    camera.position.set(0, 3.4, 11.2);

    // 3. Renderer with High-Performance Shadows
    renderer = new THREE.WebGLRenderer({
        canvas,
        antialias: true,
        powerPreference: 'high-performance',
        stencil: false
    });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.05;

    // 4. Orbit Controls (Unrestricted, Silky Smooth)
    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.06;
    controls.minDistance = 1.2;
    controls.maxDistance = 55;
    controls.minPolarAngle = 0.05; // Can look all the way up to Moon & Fuji summit
    controls.maxPolarAngle = Math.PI / 2 + 0.02; // Down to stone floor
    controls.target.set(0, 2.2, 0);
    controls.autoRotate = false;
    controls.autoRotateSpeed = 0.8;

    // Any manual touch/mouse interaction cancels active glide & cinematic mode
    controls.addEventListener('start', () => {
        isTransitioning = false;
        if (isCinematic) setCinematicMode(false);
    });

    // 5. Lighting Setup
    setupLighting();

    // 6. Build Scene Geometry
    buildStarfield();
    buildFullMoonAndGodRays();
    buildMajesticMountFuji();
    buildShrineGroundAndSteps();
    buildGrandToriiGate();
    buildWeepingWisteriaForest();
    buildNichirinKatanaMasterpiece();
    buildKasugaStoneLanterns();
    buildDarumaDoll();
    buildManekiNeko();
    buildDualParticleSystems();

    // 7. Event Handlers
    window.addEventListener('resize', onWindowResize);
    canvas.addEventListener('click', onCanvasClick);

    // Initial Display
    updateLightingVisuals();
    updateCinematicUI();
    showModal(VOCAB_DATABASE.torii, false);

    // Start Main Render Loop
    requestAnimationFrame(animate);
}

// ==========================================
// LIGHTING SETUP
// ==========================================
function setupLighting() {
    // Ambient light: mystical deep purple indigo
    ambientLight = new THREE.AmbientLight(0x241445, 0.95);
    scene.add(ambientLight);

    // Main Silvery Moonbeam casting soft shadows
    dirLight = new THREE.DirectionalLight(0xa5b4fc, 0.95);
    dirLight.position.set(8, 22, 10);
    dirLight.castShadow = true;
    dirLight.shadow.mapSize.width = 2048;
    dirLight.shadow.mapSize.height = 2048;
    dirLight.shadow.camera.near = 0.5;
    dirLight.shadow.camera.far = 60;
    dirLight.shadow.camera.left = -14;
    dirLight.shadow.camera.right = 14;
    dirLight.shadow.camera.top = 14;
    dirLight.shadow.camera.bottom = -14;
    dirLight.shadow.bias = -0.0004;
    scene.add(dirLight);

    // Moon Rim Light (casting luminous violet rim light from behind Fuji)
    moonRimLight = new THREE.DirectionalLight(0xc084fc, 1.3);
    moonRimLight.position.set(0, 16, -38);
    scene.add(moonRimLight);

    // Dedicated Katana Altar Spotlight
    katanaSpotLight = new THREE.SpotLight(0xfef08a, 1.8, 8, Math.PI / 4, 0.35);
    katanaSpotLight.position.set(2.4, 3.2, 2.5);
    katanaSpotLight.target.position.set(2.4, 0.85, 1.2);
    katanaSpotLight.castShadow = true;
    scene.add(katanaSpotLight);
    scene.add(katanaSpotLight.target);
}

// ==========================================
// PROCEDURAL TEXTURE GENERATORS
// ==========================================
function createMoonTexture() {
    const canvas = document.createElement('canvas');
    canvas.width = 512;
    canvas.height = 512;
    const ctx = canvas.getContext('2d');

    // Base moon gradient
    const grad = ctx.createRadialGradient(256, 256, 20, 256, 256, 256);
    grad.addColorStop(0, '#ffffff');
    grad.addColorStop(0.7, '#e0e7ff');
    grad.addColorStop(0.95, '#c7d2fe');
    grad.addColorStop(1, '#a5b4fc');
    ctx.fillStyle = grad;
    ctx.beginPath();
    ctx.arc(256, 256, 256, 0, Math.PI * 2);
    ctx.fill();

    // Lunar Mare (craters and dark basaltic plains)
    ctx.fillStyle = 'rgba(148, 163, 184, 0.28)';
    const craters = [
        { x: 180, y: 160, r: 70 },
        { x: 230, y: 220, r: 90 },
        { x: 330, y: 170, r: 60 },
        { x: 300, y: 310, r: 85 },
        { x: 190, y: 340, r: 50 },
        { x: 370, y: 270, r: 45 }
    ];
    craters.forEach(c => {
        ctx.beginPath();
        ctx.arc(c.x, c.y, c.r, 0, Math.PI * 2);
        ctx.fill();
    });

    return new THREE.CanvasTexture(canvas);
}

function createRadialGlowTexture(innerColor, outerColor) {
    const canvas = document.createElement('canvas');
    canvas.width = 128;
    canvas.height = 128;
    const ctx = canvas.getContext('2d');

    const grad = ctx.createRadialGradient(64, 64, 0, 64, 64, 64);
    grad.addColorStop(0, innerColor);
    grad.addColorStop(0.4, innerColor.replace('1)', '0.5)'));
    grad.addColorStop(1, outerColor);
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 128, 128);

    return new THREE.CanvasTexture(canvas);
}

function createPetalTexture(colorHex1, colorHex2) {
    const canvas = document.createElement('canvas');
    canvas.width = 64;
    canvas.height = 64;
    const ctx = canvas.getContext('2d');

    ctx.translate(32, 32);
    const grad = ctx.createRadialGradient(0, 0, 2, 0, 0, 28);
    grad.addColorStop(0, colorHex1);
    grad.addColorStop(0.7, colorHex2);
    grad.addColorStop(1, 'rgba(0,0,0,0)');

    ctx.fillStyle = grad;
    ctx.beginPath();
    ctx.ellipse(0, 0, 14, 26, Math.PI / 6, 0, Math.PI * 2);
    ctx.fill();

    return new THREE.CanvasTexture(canvas);
}

// ==========================================
// SCENE & ATMOSPHERE BUILDERS
// ==========================================

// 1. Cosmic Starfield
function buildStarfield() {
    const starCount = 1500;
    const starGeo = new THREE.BufferGeometry();
    const starPos = new Float32Array(starCount * 3);
    const starColors = new Float32Array(starCount * 3);

    for (let i = 0; i < starCount; i++) {
        const theta = 2 * Math.PI * Math.random();
        const phi = Math.acos(2 * Math.random() - 1);
        const radius = 100 + Math.random() * 45;

        starPos[i * 3] = radius * Math.sin(phi) * Math.cos(theta);
        starPos[i * 3 + 1] = Math.abs(radius * Math.cos(phi)) + 6; // Keep above horizon
        starPos[i * 3 + 2] = radius * Math.sin(phi) * Math.sin(theta);

        const rand = Math.random();
        if (rand > 0.7) {
            starColors[i * 3] = 0.85; starColors[i * 3 + 1] = 0.75; starColors[i * 3 + 2] = 1.0; // Violet
        } else if (rand > 0.4) {
            starColors[i * 3] = 0.7; starColors[i * 3 + 1] = 0.92; starColors[i * 3 + 2] = 1.0; // Ice blue
        } else {
            starColors[i * 3] = 1.0; starColors[i * 3 + 1] = 1.0; starColors[i * 3 + 2] = 1.0; // White
        }
    }

    starGeo.setAttribute('position', new THREE.BufferAttribute(starPos, 3));
    starGeo.setAttribute('color', new THREE.BufferAttribute(starColors, 3));

    const starMat = new THREE.PointsMaterial({
        size: 0.7,
        vertexColors: true,
        transparent: true,
        opacity: 0.92,
        depthWrite: false
    });

    const stars = new THREE.Points(starGeo, starMat);
    scene.add(stars);
    models.starfield = stars;
}

// 2. Glowing Full Moon & Volumetric God Rays
function buildFullMoonAndGodRays() {
    const moonGroup = new THREE.Group();
    moonGroup.name = 'fuji';
    moonGroup.position.set(4.2, 18.0, -40);

    // Core Moon Disc
    const moonTex = createMoonTexture();
    const moonGeo = new THREE.CircleGeometry(5.5, 64);
    const moonMat = new THREE.MeshBasicMaterial({
        map: moonTex,
        transparent: true,
        opacity: 0.98
    });
    moonMesh = new THREE.Mesh(moonGeo, moonMat);
    moonGroup.add(moonMesh);

    // Multi-Layered Inner & Outer Moon Glow Halo
    const haloTex = createRadialGlowTexture('rgba(224, 231, 255, 1)', 'rgba(168, 85, 247, 0)');
    const haloGeo = new THREE.PlaneGeometry(18, 18);
    const haloMat = new THREE.MeshBasicMaterial({
        map: haloTex,
        transparent: true,
        blending: THREE.AdditiveBlending,
        depthWrite: false,
        opacity: 0.75
    });
    moonHaloMesh = new THREE.Mesh(haloGeo, haloMat);
    moonHaloMesh.position.z = -0.1;
    moonGroup.add(moonHaloMesh);

    // Massive Ethereal Outer Wisteria Aura
    const outerHaloGeo = new THREE.PlaneGeometry(32, 32);
    const outerHaloMat = new THREE.MeshBasicMaterial({
        map: haloTex,
        transparent: true,
        blending: THREE.AdditiveBlending,
        depthWrite: false,
        opacity: 0.38,
        color: 0x9333ea
    });
    const outerHalo = new THREE.Mesh(outerHaloGeo, outerHaloMat);
    outerHalo.position.z = -0.2;
    moonGroup.add(outerHalo);

    scene.add(moonGroup);
    models.moon = moonGroup;

    // Volumetric Moonbeams (Slanted rays streaming into the valley)
    godRaysGroup = new THREE.Group();
    const rayMat = new THREE.MeshBasicMaterial({
        color: 0xd8b4fe,
        transparent: true,
        opacity: 0.08,
        blending: THREE.AdditiveBlending,
        side: THREE.DoubleSide,
        depthWrite: false
    });

    const angles = [-0.22, -0.08, 0.10, 0.25];
    angles.forEach((ang, idx) => {
        const rayGeo = new THREE.CylinderGeometry(0.6, 5.5 + idx * 0.8, 42, 16, 1, true);
        const ray = new THREE.Mesh(rayGeo, rayMat);
        ray.position.set(ang * 26, 11, -22);
        ray.rotation.z = ang * 0.65;
        ray.rotation.x = 0.18;
        godRaysGroup.add(ray);
    });
    scene.add(godRaysGroup);
}

// 3. Majestic Mount Fuji (Authentic Exponential Volcanic Curvature & Snow Summit)
function buildMajesticMountFuji() {
    const fujiGroup = new THREE.Group();
    fujiGroup.name = 'fuji';
    fujiGroup.position.set(0, 0.5, -44);

    // Parametric Exponential Volcanic Flank Geometry
    const slices = 64;
    const stacks = 32;
    const totalHeight = 24.0;
    const baseRadius = 38.0;

    const fujiGeo = new THREE.BufferGeometry();
    const positions = [];
    const uvs = [];
    const indices = [];

    for (let j = 0; j <= stacks; j++) {
        const v = j / stacks;
        const y = v * totalHeight;
        // Exponential flare: gentle summit tapering out into a wide, majestic mountain base
        const radius = 3.0 + (baseRadius - 3.0) * Math.pow(1 - v, 1.85);

        for (let i = 0; i <= slices; i++) {
            const u = i / slices;
            const theta = u * Math.PI * 2;
            const x = radius * Math.sin(theta);
            const z = radius * Math.cos(theta);

            // Subtle ridge undulation
            const ridge = Math.sin(theta * 16) * 0.3 * (1 - v);

            positions.push(x, y, z + ridge);
            uvs.push(u, v);
        }
    }

    for (let j = 0; j < stacks; j++) {
        for (let i = 0; i < slices; i++) {
            const a = j * (slices + 1) + i;
            const b = (j + 1) * (slices + 1) + i;
            const c = (j + 1) * (slices + 1) + (i + 1);
            const d = j * (slices + 1) + (i + 1);

            indices.push(a, b, d);
            indices.push(b, c, d);
        }
    }

    fujiGeo.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
    fujiGeo.setAttribute('uv', new THREE.Float32BufferAttribute(uvs, 2));
    fujiGeo.setIndex(indices);
    fujiGeo.computeVertexNormals();

    // Dark obsidian basalt material for mountain body
    const rockMat = new THREE.MeshStandardMaterial({
        color: 0x110c26,
        roughness: 0.95,
        metalness: 0.05
    });
    const fujiBody = new THREE.Mesh(fujiGeo, rockMat);
    fujiBody.receiveShadow = true;
    fujiGroup.add(fujiBody);

    // Pure Glistening Snow Cap (From snowline y = 14 to summit y = 24)
    const snowGeo = new THREE.ConeGeometry(8.2, 10.5, 64);
    const snowMat = new THREE.MeshStandardMaterial({
        color: 0xf8fafc,
        roughness: 0.28,
        metalness: 0.15,
        emissive: 0x818cf8,
        emissiveIntensity: 0.22
    });
    const snowCap = new THREE.Mesh(snowGeo, snowMat);
    snowCap.position.set(0, 19.5, 0);
    fujiGroup.add(snowCap);

    // Jagged Glacier Snow Tongues (Yukikei) streaming down gullies
    const tongueCount = 14;
    for (let t = 0; t < tongueCount; t++) {
        const ang = (t / tongueCount) * Math.PI * 2;
        const length = 3.5 + Math.sin(t * 3) * 1.5;
        const tongueGeo = new THREE.ConeGeometry(0.85, length, 8);
        const tongue = new THREE.Mesh(tongueGeo, snowMat);
        tongue.position.set(
            Math.sin(ang) * 9.2,
            14.5 - length * 0.4,
            Math.cos(ang) * 9.2
        );
        tongue.rotation.z = Math.sin(ang) * 0.35;
        tongue.rotation.x = -Math.cos(ang) * 0.35;
        fujiGroup.add(tongue);
    }

    // Mountain Ridge Silhouettes framing the horizon
    const ridgeMat = new THREE.MeshBasicMaterial({ color: 0x080415 });
    const ridgePoints = [
        -55, 0, -48, 8, -40, 5, -32, 10, -24, 6, -16, 9, -8, 5,
        0, 7, 8, 5, 16, 9, 24, 6, 32, 10, 40, 5, 48, 8, 55, 0
    ];
    const shape = new THREE.Shape();
    shape.moveTo(-60, -2);
    for (let i = 0; i < ridgePoints.length; i += 2) {
        shape.lineTo(ridgePoints[i], ridgePoints[i + 1]);
    }
    shape.lineTo(60, -2);
    shape.closePath();
    const ridgeMesh = new THREE.Mesh(new THREE.ShapeGeometry(shape), ridgeMat);
    ridgeMesh.position.set(0, 0, -18);
    fujiGroup.add(ridgeMesh);

    scene.add(fujiGroup);
    models.fuji = fujiGroup;
}

// 4. Shrine Ground, Sando Path & Weathered Steps
function buildShrineGroundAndSteps() {
    const groundGroup = new THREE.Group();

    // Expansive Mountain Ridge Plateau (Radius 55m, eliminates void cutoff)
    const plateauGeo = new THREE.CylinderGeometry(55, 58, 1.5, 64);
    const plateauMat = new THREE.MeshStandardMaterial({
        color: 0x0f0b1f,
        roughness: 0.94,
        metalness: 0.05
    });
    const plateau = new THREE.Mesh(plateauGeo, plateauMat);
    plateau.position.y = -0.75;
    plateau.receiveShadow = true;
    groundGroup.add(plateau);

    // Stone Terrace Border
    const stoneBorderMat = new THREE.MeshStandardMaterial({ color: 0x2b3342, roughness: 0.88 });
    const stoneTerrace = new THREE.Mesh(new THREE.CylinderGeometry(12.5, 13.0, 0.25, 64), stoneBorderMat);
    stoneTerrace.position.y = 0.08;
    stoneTerrace.receiveShadow = true;
    groundGroup.add(stoneTerrace);

    // Central Sando Flagstone Path (Paved walkway through Torii)
    const pathMat = new THREE.MeshStandardMaterial({
        color: 0x1f2433,
        roughness: 0.78,
        metalness: 0.12
    });
    const path = new THREE.Mesh(new THREE.PlaneGeometry(2.6, 22), pathMat);
    path.rotation.x = -Math.PI / 2;
    path.position.set(0, 0.22, 1.0);
    path.receiveShadow = true;
    groundGroup.add(path);

    // White Raked Shrine Pebbles (Shirakawa-suna) flanking the path
    const pebbleMat = new THREE.MeshStandardMaterial({ color: 0x475569, roughness: 0.85 });
    [-1.65, 1.65].forEach(x => {
        const pebbles = new THREE.Mesh(new THREE.PlaneGeometry(0.7, 22), pebbleMat);
        pebbles.rotation.x = -Math.PI / 2;
        pebbles.position.set(x, 0.215, 1.0);
        pebbles.receiveShadow = true;
        groundGroup.add(pebbles);
    });

    // Weathered Stone Steps (Ishidan ascending to Torii)
    const stepMat = new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.85 });
    for (let s = 0; s < 4; s++) {
        const step = new THREE.Mesh(new THREE.BoxGeometry(3.6 - s * 0.15, 0.11, 0.75), stepMat);
        step.position.set(0, 0.1 + s * 0.1, 4.4 - s * 0.7);
        step.receiveShadow = true;
        step.castShadow = true;
        groundGroup.add(step);
    }

    scene.add(groundGroup);
    models.ground = groundGroup;
}

// ==========================================
// GRAND TORII SHRINE ENTRANCE (MYOJIN TORII)
// ==========================================
function buildGrandToriiGate() {
    const torii = new THREE.Group();
    torii.name = 'torii';

    // Premium Materials
    const vermilionMat = new THREE.MeshStandardMaterial({
        color: 0xd62828,
        roughness: 0.32,
        metalness: 0.15
    });
    const blackLacquerMat = new THREE.MeshStandardMaterial({
        color: 0x0f1117,
        roughness: 0.18,
        metalness: 0.35
    });
    const stoneBaseMat = new THREE.MeshStandardMaterial({
        color: 0x475569,
        roughness: 0.9
    });
    const goldMat = new THREE.MeshStandardMaterial({
        color: 0xf59e0b,
        roughness: 0.25,
        metalness: 0.8
    });
    const shimenawaStrawMat = new THREE.MeshStandardMaterial({
        color: 0xd97706,
        roughness: 0.95
    });
    const whiteShideMat = new THREE.MeshStandardMaterial({
        color: 0xf8fafc,
        roughness: 0.45,
        side: THREE.DoubleSide
    });

    const dist = 2.2;
    const height = 4.8;
    const radius = 0.24;

    // 1. Two Grand Vermilion Hashira Pillars with Entasis & Gold-Banded Bases
    [-dist, dist].forEach(x => {
        // Kamebara (Stone base plinth)
        const plinth = new THREE.Mesh(new THREE.CylinderGeometry(0.44, 0.50, 0.4, 24), stoneBaseMat);
        plinth.position.set(x, 0.3, 0);
        plinth.castShadow = true;
        torii.add(plinth);

        // Black Lacquer Collar & Polished Gold Ring
        const collar = new THREE.Mesh(new THREE.CylinderGeometry(0.33, 0.33, 0.34, 24), blackLacquerMat);
        collar.position.set(x, 0.65, 0);
        torii.add(collar);

        const goldRing = new THREE.Mesh(new THREE.CylinderGeometry(0.34, 0.34, 0.05, 24), goldMat);
        goldRing.position.set(x, 0.84, 0);
        torii.add(goldRing);

        // Main Incline Vermilion Pillar (Entasis taper)
        const pillar = new THREE.Mesh(new THREE.CylinderGeometry(radius * 0.9, radius, height, 32), vermilionMat);
        pillar.position.set(x, height / 2 + 0.55, 0);
        pillar.rotation.z = x > 0 ? 0.032 : -0.032;
        pillar.castShadow = true;
        torii.add(pillar);

        // Kusabi (Wooden wedges at Nuki tie-beam)
        const wedge = new THREE.Mesh(new THREE.BoxGeometry(0.12, 0.35, 0.58), vermilionMat);
        wedge.position.set(x, 4.0, 0);
        torii.add(wedge);
    });

    // 2. Kasagi (Top sweeping curved beam with black copper ridge)
    const kasagiCurve = new THREE.QuadraticBezierCurve3(
        new THREE.Vector3(-3.8, 5.5, 0),
        new THREE.Vector3(0, 5.2, 0),
        new THREE.Vector3(3.8, 5.5, 0)
    );
    const kasagi = new THREE.Mesh(new THREE.TubeGeometry(kasagiCurve, 48, 0.24, 12, false), blackLacquerMat);
    kasagi.scale.set(1, 1.25, 0.9);
    kasagi.castShadow = true;
    torii.add(kasagi);

    // 3. Shimaki (Secondary vermilion beam directly underneath)
    const shimaki = new THREE.Mesh(new THREE.BoxGeometry(6.6, 0.3, 0.46), vermilionMat);
    shimaki.position.set(0, 4.98, 0);
    shimaki.castShadow = true;
    torii.add(shimaki);

    // 4. Nuki (Lower tie-beam interlocking pillars)
    const nuki = new THREE.Mesh(new THREE.BoxGeometry(5.6, 0.26, 0.34), vermilionMat);
    nuki.position.set(0, 4.0, 0);
    nuki.castShadow = true;
    torii.add(nuki);

    // 5. Gakuzuka (Center Plaque inscribed "藤襲山" - Mt. Fujikasane)
    const gakuzuka = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.78, 0.1), blackLacquerMat);
    gakuzuka.position.set(0, 4.5, 0.16);
    torii.add(gakuzuka);

    const gakuzukaFrame = new THREE.Mesh(new THREE.BoxGeometry(0.54, 0.82, 0.08), goldMat);
    gakuzukaFrame.position.set(0, 4.5, 0.14);
    torii.add(gakuzukaFrame);

    // 6. Sacred Braided Straw Rope (Shimenawa - 注連縄)
    const shimenawaCurve = new THREE.QuadraticBezierCurve3(
        new THREE.Vector3(-dist + 0.15, 3.85, 0.15),
        new THREE.Vector3(0, 3.42, 0.22),
        new THREE.Vector3(dist - 0.15, 3.85, 0.15)
    );
    const shimenawa = new THREE.Mesh(new THREE.TubeGeometry(shimenawaCurve, 36, 0.095, 10, false), shimenawaStrawMat);
    torii.add(shimenawa);

    // 7. Hanging White Zigzag Paper Streamers (Shide - 紙垂)
    const shidePositions = [-1.2, -0.45, 0.45, 1.2];
    models.shideMeshes = [];
    shidePositions.forEach(x => {
        const shideGroup = new THREE.Group();
        shideGroup.position.set(x, 3.5, 0.2);

        const seg1 = new THREE.Mesh(new THREE.BoxGeometry(0.12, 0.18, 0.01), whiteShideMat);
        seg1.rotation.z = 0.25;
        seg1.position.set(-0.03, -0.09, 0);
        shideGroup.add(seg1);

        const seg2 = new THREE.Mesh(new THREE.BoxGeometry(0.12, 0.18, 0.01), whiteShideMat);
        seg2.rotation.z = -0.25;
        seg2.position.set(0.03, -0.22, 0);
        shideGroup.add(seg2);

        const seg3 = new THREE.Mesh(new THREE.BoxGeometry(0.1, 0.16, 0.01), whiteShideMat);
        seg3.rotation.z = 0.2;
        seg3.position.set(-0.02, -0.34, 0);
        shideGroup.add(seg3);

        torii.add(shideGroup);
        models.shideMeshes.push(shideGroup);
    });

    scene.add(torii);
    models.torii = torii;
}

// ==========================================
// ORGANIC WEEPING WISTERIA FOREST (KIMETSU STYLE)
// ==========================================
function buildWeepingWisteriaForest() {
    const wisteriaGroup = new THREE.Group();
    wisteriaGroup.name = 'wisteria';

    const barkMat = new THREE.MeshStandardMaterial({
        color: 0x271e1b,
        roughness: 0.92,
        metalness: 0.05
    });

    // Tiered Wisteria Raceme Blossom Materials
    const baseMat = new THREE.MeshStandardMaterial({
        color: 0x6b21a8,
        emissive: 0x7e22ce,
        emissiveIntensity: 0.6,
        roughness: 0.4
    });
    const midMat = new THREE.MeshStandardMaterial({
        color: 0x9333ea,
        emissive: 0xa855f7,
        emissiveIntensity: 0.75,
        roughness: 0.35
    });
    const tipMat = new THREE.MeshStandardMaterial({
        color: 0xe879f9,
        emissive: 0xf0abfc,
        emissiveIntensity: 0.85,
        roughness: 0.3
    });
    const foliageMat = new THREE.MeshStandardMaterial({
        color: 0x1a2e26,
        roughness: 0.85
    });

    models.wisteriaClusters = [];
    wisteriaGlowLights = [];

    // Helper: Build a single twisted wisteria tree with weeping racemes
    function createWisteriaTree(x, z, archDirection) {
        const tree = new THREE.Group();
        tree.position.set(x, 0.2, z);

        // Twisted, gnarled ancient trunk
        const trunkCurve = new THREE.CatmullRomCurve3([
            new THREE.Vector3(0, 0, 0),
            new THREE.Vector3(archDirection * 0.4, 1.2, 0.1),
            new THREE.Vector3(archDirection * 0.7, 2.6, -0.2),
            new THREE.Vector3(archDirection * 1.1, 4.0, 0.1)
        ]);
        const trunk = new THREE.Mesh(new THREE.TubeGeometry(trunkCurve, 24, 0.28, 10, false), barkMat);
        trunk.castShadow = true;
        tree.add(trunk);

        // Spreading arching boughs
        const branchConfigs = [
            { end: new THREE.Vector3(archDirection * 1.8, 4.5, 0.8), racemes: 6 },
            { end: new THREE.Vector3(archDirection * 2.2, 4.3, -0.6), racemes: 7 },
            { end: new THREE.Vector3(archDirection * 1.0, 4.7, 0.4), racemes: 5 },
            { end: new THREE.Vector3(archDirection * 1.5, 4.8, -1.0), racemes: 6 }
        ];

        branchConfigs.forEach(cfg => {
            const bCurve = new THREE.LineCurve3(
                new THREE.Vector3(archDirection * 1.1, 4.0, 0.1),
                cfg.end
            );
            const branch = new THREE.Mesh(new THREE.TubeGeometry(bCurve, 12, 0.14, 8, false), barkMat);
            branch.castShadow = true;
            tree.add(branch);

            // Foliage canopy cluster
            const foliage = new THREE.Mesh(new THREE.SphereGeometry(0.85, 12, 12), foliageMat);
            foliage.position.set(cfg.end.x, cfg.end.y + 0.2, cfg.end.z);
            foliage.scale.set(1.5, 0.6, 1.3);
            tree.add(foliage);

            // Flowing Weeping Racemes (Fujinohana curtains)
            for (let r = 0; r < cfg.racemes; r++) {
                const cluster = new THREE.Group();
                const offsetX = (Math.random() - 0.5) * 1.1;
                const offsetZ = (Math.random() - 0.5) * 1.1;
                cluster.position.set(cfg.end.x + offsetX, cfg.end.y - 0.1, cfg.end.z + offsetZ);

                // Multi-tiered flower raceme tapering downward
                const tiers = 5 + Math.floor(Math.random() * 3);
                for (let t = 0; t < tiers; t++) {
                    const radius = (tiers - t) * 0.038 + 0.025;
                    const cMat = t < 2 ? baseMat : (t < tiers - 1 ? midMat : tipMat);
                    const tierMesh = new THREE.Mesh(new THREE.SphereGeometry(radius, 8, 8), cMat);
                    tierMesh.position.y = -t * 0.22;
                    tierMesh.scale.set(1, 1.35, 1);
                    cluster.add(tierMesh);
                }

                cluster.userData = {
                    phaseOffset: Math.random() * Math.PI * 2,
                    speed: 1.5 + Math.random() * 0.6
                };

                tree.add(cluster);
                models.wisteriaClusters.push(cluster);
            }
        });

        // Wisteria Glow Point Light
        const glowLight = new THREE.PointLight(0xa855f7, 2.2, 8);
        glowLight.position.set(archDirection * 1.5, 3.6, 0);
        tree.add(glowLight);
        wisteriaGlowLights.push(glowLight);

        return tree;
    }

    // 4 Flanking Trees (Foreground and Midground framing the Torii)
    const tree1 = createWisteriaTree(-3.8, 1.8, -1);
    const tree2 = createWisteriaTree(3.8, 1.8, 1);
    const tree3 = createWisteriaTree(-4.2, -1.5, -1);
    const tree4 = createWisteriaTree(4.2, -1.5, 1);

    wisteriaGroup.add(tree1);
    wisteriaGroup.add(tree2);
    wisteriaGroup.add(tree3);
    wisteriaGroup.add(tree4);

    scene.add(wisteriaGroup);
    models.wisteria = wisteriaGroup;
}

// ==========================================
// MASTERPIECE DEMON SLAYER NICHIRIN KATANA
// (Museum-Grade Geometry & Shrine Display Table)
// ==========================================
function buildNichirinKatanaMasterpiece() {
    const katanaEnsemble = new THREE.Group();
    katanaEnsemble.name = 'katana';
    // Placed on the right terrace, beautifully framing the walkway and lit by lantern
    katanaEnsemble.position.set(2.4, 0.22, 1.2);

    // 1. Vermilion & Gold Lacquer Shrine Altar Table (Sanbō)
    const tableMat = new THREE.MeshStandardMaterial({
        color: 0x881337,
        roughness: 0.25,
        metalness: 0.2
    });
    const goldTrimMat = new THREE.MeshStandardMaterial({
        color: 0xf59e0b,
        roughness: 0.25,
        metalness: 0.85
    });
    const blackStandMat = new THREE.MeshStandardMaterial({
        color: 0x0f172a,
        roughness: 0.15,
        metalness: 0.3
    });

    // Tabletop
    const tableTop = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.08, 0.58), tableMat);
    tableTop.position.y = 0.42;
    tableTop.castShadow = true;
    tableTop.receiveShadow = true;
    katanaEnsemble.add(tableTop);

    // Table Gold Corner Plates
    [-0.78, 0.78].forEach(x => {
        [-0.27, 0.27].forEach(z => {
            const corner = new THREE.Mesh(new THREE.BoxGeometry(0.06, 0.09, 0.06), goldTrimMat);
            corner.position.set(x, 0.42, z);
            katanaEnsemble.add(corner);
        });
    });

    // Table Carved Legs
    [-0.68, 0.68].forEach(x => {
        [-0.22, 0.22].forEach(z => {
            const leg = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.035, 0.42, 12), tableMat);
            leg.position.set(x, 0.21, z);
            leg.castShadow = true;
            katanaEnsemble.add(leg);
        });
    });

    // 2. Black Lacquer Katanakake (Sword Stand with Authentic Notches)
    const standBase = new THREE.Mesh(new THREE.BoxGeometry(1.05, 0.04, 0.26), blackStandMat);
    standBase.position.y = 0.48;
    standBase.castShadow = true;
    katanaEnsemble.add(standBase);

    // Crest emblem on stand
    const crest = new THREE.Mesh(new THREE.CircleGeometry(0.07, 16), goldTrimMat);
    crest.position.set(0, 0.49, 0.135);
    katanaEnsemble.add(crest);

    // Left and Right Uprights with True U-Notches
    [-0.28, 0.28].forEach(x => {
        // Lower upright body
        const lowerBody = new THREE.Mesh(new THREE.BoxGeometry(0.06, 0.14, 0.16), blackStandMat);
        lowerBody.position.set(x, 0.57, 0);
        katanaEnsemble.add(lowerBody);

        // Mid section between lower and upper notches
        const midBody = new THREE.Mesh(new THREE.BoxGeometry(0.06, 0.12, 0.14), blackStandMat);
        midBody.position.set(x, 0.73, 0);
        katanaEnsemble.add(midBody);

        // Top finial
        const topFinial = new THREE.Mesh(new THREE.CylinderGeometry(0.035, 0.035, 0.05, 12), goldTrimMat);
        topFinial.position.set(x, 0.82, 0);
        katanaEnsemble.add(topFinial);
    });

    // 3. The Continuous Curvature Nichirin Katana (Sori: y(x) = y0 + 0.045 * ((x+0.38)/1.06)^2)
    const y0 = 0.81; // Resting height in upper notch
    const curveSori = (x) => y0 + 0.045 * Math.pow((x + 0.38) / 1.06, 2);

    // --- A. Faceted Razor-Sharp Blade (Nagasa) from x = -0.10 to x = +0.68 ---
    const bladeSegments = 24;
    const bladePositions = [];
    const bladeNormals = [];
    const bladeIndices = [];

    for (let i = 0; i <= bladeSegments; i++) {
        const u = i / bladeSegments;
        const x = -0.10 + u * (0.68 - (-0.10));
        const y = curveSori(x);
        const taper = 1 - u * 0.35;

        // Tangent slope
        const dy = 0.09 * (x + 0.38) / Math.pow(1.06, 2);
        const theta = Math.atan(dy);
        const nx = -Math.sin(theta);
        const ny = Math.cos(theta);

        // 4 cross-section vertices: Mune (top), Shinogi-Left, Shinogi-Right, Ha (cutting edge)
        const topW = 0.011 * taper;
        const botW = 0.0015;
        const ridgeH = 0.004;

        if (i === bladeSegments) {
            // Kissaki tip point
            bladePositions.push(x + 0.03, y + dy * 0.03, 0); // Vertex 0 at tip
            bladePositions.push(x, y + ridgeH, 0.006 * taper); // Vertex 1
            bladePositions.push(x, y + ridgeH, -0.006 * taper); // Vertex 2
            bladePositions.push(x, y - 0.015 * taper, 0); // Vertex 3
        } else {
            // Vertex 0: Mune (spine)
            bladePositions.push(x + nx * topW, y + ny * topW, 0);
            // Vertex 1: Shinogi Left
            bladePositions.push(x, y + ridgeH, 0.007 * taper);
            // Vertex 2: Shinogi Right
            bladePositions.push(x, y + ridgeH, -0.007 * taper);
            // Vertex 3: Ha (cutting edge)
            bladePositions.push(x - nx * 0.015 * taper, y - ny * 0.015 * taper, 0);
        }
    }

    for (let i = 0; i < bladeSegments; i++) {
        const r1 = i * 4;
        const r2 = (i + 1) * 4;

        // Top ridge left & right
        bladeIndices.push(r1, r2, r2 + 1); bladeIndices.push(r1, r2 + 1, r1 + 1);
        bladeIndices.push(r1, r1 + 2, r2 + 2); bladeIndices.push(r1, r2 + 2, r2);

        // Lower bevel to cutting edge left & right
        bladeIndices.push(r1 + 1, r2 + 1, r2 + 3); bladeIndices.push(r1 + 1, r2 + 3, r1 + 3);
        bladeIndices.push(r1 + 2, r1 + 3, r2 + 3); bladeIndices.push(r1 + 2, r2 + 3, r2 + 2);
    }

    const bladeGeo = new THREE.BufferGeometry();
    bladeGeo.setAttribute('position', new THREE.Float32BufferAttribute(bladePositions, 3));
    bladeGeo.setIndex(bladeIndices);
    bladeGeo.computeVertexNormals();

    const steelMat = new THREE.MeshStandardMaterial({
        color: 0xe2e8f0,
        metalness: 0.98,
        roughness: 0.10,
        emissive: 0x38bdf8,
        emissiveIntensity: 0.15 // Nichirin energy glow
    });
    const bladeMesh = new THREE.Mesh(bladeGeo, steelMat);
    bladeMesh.castShadow = true;
    katanaEnsemble.add(bladeMesh);

    // --- B. Habaki (Golden Blade Collar) at x = -0.13 to -0.10 ---
    const habakiY = curveSori(-0.115);
    const habaki = new THREE.Mesh(new THREE.BoxGeometry(0.045, 0.038, 0.024), goldTrimMat);
    habaki.position.set(-0.115, habakiY, 0);
    katanaEnsemble.add(habaki);

    // --- C. Flame Tsuba (Demon Slayer Sword Guard) at x = -0.14 ---
    const tsubaY = curveSori(-0.14);
    const tsubaGroup = new THREE.Group();
    tsubaGroup.position.set(-0.14, tsubaY, 0);
    tsubaGroup.rotation.z = Math.PI / 2;

    const tsubaCore = new THREE.Mesh(new THREE.CylinderGeometry(0.09, 0.09, 0.016, 24), blackStandMat);
    tsubaGroup.add(tsubaCore);
    const tsubaRim = new THREE.Mesh(new THREE.TorusGeometry(0.09, 0.014, 12, 24), goldTrimMat);
    tsubaGroup.add(tsubaRim);
    katanaEnsemble.add(tsubaGroup);

    // --- D. Tsuka (Hilt Wrapped in Silk) from x = -0.38 to -0.14 ---
    const tsukaLength = 0.24;
    const tsukaY = curveSori(-0.26);
    const tsukaMat = new THREE.MeshStandardMaterial({
        color: 0x0f172a,
        roughness: 0.6
    });
    const tsuka = new THREE.Mesh(new THREE.CylinderGeometry(0.022, 0.024, tsukaLength, 16), tsukaMat);
    tsuka.position.set(-0.26, tsukaY, 0);
    tsuka.rotation.z = Math.PI / 2;
    tsuka.castShadow = true;
    katanaEnsemble.add(tsuka);

    // Kashira (Gold Pommel Cap) at x = -0.38
    const kashiraY = curveSori(-0.38);
    const kashira = new THREE.Mesh(new THREE.CylinderGeometry(0.026, 0.026, 0.025, 16), goldTrimMat);
    kashira.position.set(-0.38, kashiraY, 0);
    kashira.rotation.z = Math.PI / 2;
    katanaEnsemble.add(kashira);

    // 4. Glossy Obsidian Black Lacquer Saya (Scabbard) in Lower Notch
    const sayaY0 = 0.65;
    const sayaCurveSori = (x) => sayaY0 + 0.045 * Math.pow((x + 0.38) / 1.06, 2);

    const sayaCurve = new THREE.QuadraticBezierCurve3(
        new THREE.Vector3(-0.36, sayaCurveSori(-0.36), 0),
        new THREE.Vector3(0.15, sayaCurveSori(0.15), 0),
        new THREE.Vector3(0.68, sayaCurveSori(0.68), 0)
    );
    const sayaMat = new THREE.MeshStandardMaterial({
        color: 0x09090b,
        roughness: 0.12,
        metalness: 0.25
    });
    const saya = new THREE.Mesh(new THREE.TubeGeometry(sayaCurve, 24, 0.028, 12, false), sayaMat);
    saya.castShadow = true;
    katanaEnsemble.add(saya);

    // Saya Golden Kojiri (tip cap)
    const kojiri = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.03, 0.04, 12), goldTrimMat);
    kojiri.position.set(0.68, sayaCurveSori(0.68), 0);
    kojiri.rotation.z = Math.PI / 2;
    katanaEnsemble.add(kojiri);

    scene.add(katanaEnsemble);
    models.katana = katanaEnsemble;
}

// ==========================================
// KASUGA STONE LANTERNS WITH WARM FLICKERING FLAME
// ==========================================
function buildKasugaStoneLanterns() {
    const stoneMat = new THREE.MeshStandardMaterial({
        color: 0x475569,
        roughness: 0.88
    });
    const fireMeshMat = new THREE.MeshBasicMaterial({
        color: 0xffa500
    });

    models.lanterns = [];
    lanternPointLights = [];

    [-2.6, 2.6].forEach((x, idx) => {
        const lantern = new THREE.Group();
        lantern.name = 'lantern';
        lantern.position.set(x, 0.22, 2.2);

        // Kiso (Hexagonal Stone Base)
        const base = new THREE.Mesh(new THREE.CylinderGeometry(0.44, 0.54, 0.35, 6), stoneMat);
        base.position.y = 0.175;
        base.castShadow = true;
        lantern.add(base);

        // Sao (Central Shaft)
        const shaft = new THREE.Mesh(new THREE.CylinderGeometry(0.16, 0.19, 1.15, 6), stoneMat);
        shaft.position.y = 0.92;
        shaft.castShadow = true;
        lantern.add(shaft);

        // Chūdai (Middle Platform)
        const chudai = new THREE.Mesh(new THREE.CylinderGeometry(0.52, 0.38, 0.22, 6), stoneMat);
        chudai.position.y = 1.58;
        chudai.castShadow = true;
        lantern.add(chudai);

        // Hibukuro (Carved Stone Fire Chamber with lattice openings)
        const lamp = new THREE.Mesh(new THREE.BoxGeometry(0.44, 0.44, 0.44), fireMeshMat);
        lamp.position.y = 1.9;
        lantern.add(lamp);

        // Kasa (Hexagonal Tiered Pagoda Roof with upturned corners)
        const roof = new THREE.Mesh(new THREE.ConeGeometry(0.72, 0.42, 6), stoneMat);
        roof.position.y = 2.32;
        roof.castShadow = true;
        lantern.add(roof);

        // Hōju (Sacred Jewel finial)
        const hoju = new THREE.Mesh(new THREE.SphereGeometry(0.12, 12, 12), stoneMat);
        hoju.position.y = 2.58;
        lantern.add(hoju);

        // Warm Flickering Flame Point Light
        const pLight = new THREE.PointLight(0xff8c1a, 2.5, 7.5);
        pLight.position.set(x, 2.12, 2.2);
        pLight.castShadow = true;
        pLight.shadow.bias = -0.002;
        scene.add(pLight);

        lanternPointLights.push({
            light: pLight,
            baseIntensity: 2.5,
            flickerOffset: idx * 3.14
        });

        scene.add(lantern);
        models.lanterns.push(lantern);
    });
}

// ==========================================
// DARUMA DOLL (だるま)
// ==========================================
function buildDarumaDoll() {
    const daruma = new THREE.Group();
    daruma.name = 'daruma';
    daruma.position.set(-1.8, 0.22, 1.4);

    // Weathered Stone Pedestal
    const altar = new THREE.Mesh(new THREE.CylinderGeometry(0.45, 0.52, 0.42, 16), new THREE.MeshStandardMaterial({ color: 0x334155 }));
    altar.position.y = 0.21;
    altar.castShadow = true;
    daruma.add(altar);

    // Crimson Lacquer Roly-Poly Body
    const bodyGeo = new THREE.SphereGeometry(0.38, 24, 24);
    bodyGeo.scale(1, 1.15, 0.95);
    const bodyMat = new THREE.MeshStandardMaterial({
        color: 0xdc2626,
        roughness: 0.35,
        metalness: 0.1
    });
    const body = new THREE.Mesh(bodyGeo, bodyMat);
    body.position.y = 0.65;
    body.castShadow = true;
    daruma.add(body);

    // White Porcelain Face Area
    const faceGeo = new THREE.SphereGeometry(0.24, 20, 20);
    faceGeo.scale(1, 1.1, 0.4);
    const faceMat = new THREE.MeshStandardMaterial({ color: 0xfef3c7, roughness: 0.6 });
    const face = new THREE.Mesh(faceGeo, faceMat);
    face.position.set(0, 0.72, 0.26);
    face.rotation.x = -0.15;
    daruma.add(face);

    // Bold Black Eyes
    const eyeMat = new THREE.MeshBasicMaterial({ color: 0x0f172a });
    [-0.08, 0.08].forEach(x => {
        const eye = new THREE.Mesh(new THREE.CircleGeometry(0.045, 16), eyeMat);
        eye.position.set(x, 0.76, 0.36);
        daruma.add(eye);
    });

    scene.add(daruma);
    models.daruma = daruma;
}

// ==========================================
// PORCELAIN MANEKI-NEKO (招き猫)
// ==========================================
function buildManekiNeko() {
    const neko = new THREE.Group();
    neko.name = 'neko';
    neko.position.set(-2.4, 0.22, 0.5);

    // Stone Pedestal
    const plinth = new THREE.Mesh(new THREE.CylinderGeometry(0.42, 0.48, 0.4, 16), new THREE.MeshStandardMaterial({ color: 0x334155 }));
    plinth.position.y = 0.2;
    plinth.castShadow = true;
    neko.add(plinth);

    // Glossy White Porcelain Body
    const whiteMat = new THREE.MeshStandardMaterial({
        color: 0xf8fafc,
        roughness: 0.15,
        metalness: 0.1
    });
    const goldMat = new THREE.MeshStandardMaterial({
        color: 0xf59e0b,
        roughness: 0.25,
        metalness: 0.85
    });

    const body = new THREE.Mesh(new THREE.SphereGeometry(0.32, 24, 24), whiteMat);
    body.position.y = 0.6;
    body.scale.set(1, 1.25, 0.95);
    body.castShadow = true;
    neko.add(body);

    // Head
    const head = new THREE.Mesh(new THREE.SphereGeometry(0.24, 24, 24), whiteMat);
    head.position.set(0, 0.95, 0.05);
    neko.add(head);

    // Ears
    [-0.12, 0.12].forEach(x => {
        const ear = new THREE.Mesh(new THREE.ConeGeometry(0.08, 0.14, 12), whiteMat);
        ear.position.set(x, 1.15, 0.05);
        ear.rotation.z = x > 0 ? -0.3 : 0.3;
        neko.add(ear);
    });

    // Raised Right Paw (Welcoming Luck)
    const paw = new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.05, 0.22, 12), whiteMat);
    paw.position.set(0.22, 0.98, 0.14);
    paw.rotation.z = -0.65;
    neko.add(paw);

    // Golden Bell
    const bell = new THREE.Mesh(new THREE.SphereGeometry(0.045, 12, 12), goldMat);
    bell.position.set(0, 0.74, 0.25);
    neko.add(bell);

    scene.add(neko);
    models.neko = neko;
}

// ==========================================
// DUAL PARTICLE SYSTEMS (SAKURA & WISTERIA SPIRITS)
// ==========================================
function buildDualParticleSystems() {
    // 1. Swirling Pink Sakura Blossom Petals
    const sakuraCount = 400;
    sakuraGeo = new THREE.BufferGeometry();
    const sakuraPos = new Float32Array(sakuraCount * 3);
    const sakuraSpeeds = new Float32Array(sakuraCount * 3);

    for (let i = 0; i < sakuraCount; i++) {
        sakuraPos[i * 3] = (Math.random() - 0.5) * 22;
        sakuraPos[i * 3 + 1] = Math.random() * 11;
        sakuraPos[i * 3 + 2] = (Math.random() - 0.5) * 22;

        sakuraSpeeds[i * 3] = (Math.random() - 0.5) * 0.015;
        sakuraSpeeds[i * 3 + 1] = -0.012 - Math.random() * 0.02;
        sakuraSpeeds[i * 3 + 2] = (Math.random() - 0.5) * 0.015;
    }

    sakuraGeo.setAttribute('position', new THREE.BufferAttribute(sakuraPos, 3));
    sakuraGeo.userData = { speeds: sakuraSpeeds };

    const sakuraTex = createPetalTexture('#fbcfe8', '#f472b6');
    const sakuraMat = new THREE.PointsMaterial({
        size: 0.38,
        map: sakuraTex,
        transparent: true,
        opacity: 0.88,
        depthWrite: false,
        blending: THREE.NormalBlending
    });

    sakuraParticles = new THREE.Points(sakuraGeo, sakuraMat);
    scene.add(sakuraParticles);
    models.sakura = sakuraParticles;

    // 2. Upward Swirling Wisteria Embers (Kimetsu Spirit Spores)
    const wisteriaCount = 300;
    wisteriaGeo = new THREE.BufferGeometry();
    const wisteriaPos = new Float32Array(wisteriaCount * 3);
    const wisteriaSpeeds = new Float32Array(wisteriaCount * 3);

    for (let i = 0; i < wisteriaCount; i++) {
        wisteriaPos[i * 3] = (Math.random() - 0.5) * 16;
        wisteriaPos[i * 3 + 1] = Math.random() * 7;
        wisteriaPos[i * 3 + 2] = (Math.random() - 0.5) * 16;

        wisteriaSpeeds[i * 3] = (Math.random() - 0.5) * 0.01;
        wisteriaSpeeds[i * 3 + 1] = 0.014 + Math.random() * 0.02;
        wisteriaSpeeds[i * 3 + 2] = (Math.random() - 0.5) * 0.01;
    }

    wisteriaGeo.setAttribute('position', new THREE.BufferAttribute(wisteriaPos, 3));
    wisteriaGeo.userData = { speeds: wisteriaSpeeds };

    const wisteriaTex = createRadialGlowTexture('rgba(216, 180, 254, 1)', 'rgba(147, 51, 234, 0)');
    const wisteriaMat = new THREE.PointsMaterial({
        size: 0.32,
        map: wisteriaTex,
        transparent: true,
        opacity: 0.75,
        blending: THREE.AdditiveBlending,
        depthWrite: false
    });

    wisteriaParticles = new THREE.Points(wisteriaGeo, wisteriaMat);
    scene.add(wisteriaParticles);

    // 3. Fireflies Dancing Near Moss & Steps
    const fireflyCount = 60;
    fireflyGeo = new THREE.BufferGeometry();
    const fireflyPos = new Float32Array(fireflyCount * 3);
    const fireflySpeeds = new Float32Array(fireflyCount * 3);

    for (let i = 0; i < fireflyCount; i++) {
        fireflyPos[i * 3] = (Math.random() - 0.5) * 10;
        fireflyPos[i * 3 + 1] = 0.3 + Math.random() * 2.2;
        fireflyPos[i * 3 + 2] = (Math.random() - 0.5) * 10;

        fireflySpeeds[i * 3] = (Math.random() - 0.5) * 0.012;
        fireflySpeeds[i * 3 + 1] = (Math.random() - 0.5) * 0.008;
        fireflySpeeds[i * 3 + 2] = (Math.random() - 0.5) * 0.012;
    }

    fireflyGeo.setAttribute('position', new THREE.BufferAttribute(fireflyPos, 3));
    fireflyGeo.userData = { speeds: fireflySpeeds };

    const fireflyTex = createRadialGlowTexture('rgba(254, 240, 138, 1)', 'rgba(234, 179, 8, 0)');
    const fireflyMat = new THREE.PointsMaterial({
        size: 0.3,
        map: fireflyTex,
        transparent: true,
        opacity: 0.85,
        blending: THREE.AdditiveBlending,
        depthWrite: false
    });

    fireflyParticles = new THREE.Points(fireflyGeo, fireflyMat);
    scene.add(fireflyParticles);
}

// ==========================================
// PROCEDURAL SHINTO CHIME & AUDIO
// ==========================================
function playTempleChimeSound() {
    if (!soundChimeEnabled) return;

    try {
        if (!audioCtx) {
            audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        }
        if (audioCtx.state === 'suspended') {
            audioCtx.resume();
        }

        const now = audioCtx.currentTime;
        const freqs = [587.33, 880.00, 1174.66, 1760.00]; // D5, A5, D6, A6 harmonics

        freqs.forEach((freq, idx) => {
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();

            osc.type = idx === 0 ? 'sine' : 'triangle';
            osc.frequency.setValueAtTime(freq, now);

            gain.gain.setValueAtTime(0.08 / (idx + 1), now);
            gain.gain.exponentialRampToValueAtTime(0.0001, now + 2.8 + idx * 0.4);

            osc.connect(gain);
            gain.connect(audioCtx.destination);

            osc.start(now);
            osc.stop(now + 3.2 + idx * 0.4);
        });
    } catch (e) {
        // Safe fallback if browser blocks audio autoplay
    }
}

function toggleSoundChime() {
    soundChimeEnabled = !soundChimeEnabled;
    const btn = document.getElementById('btnSoundChime');
    if (btn) {
        btn.innerHTML = `<span class="dock-btn-icon">🔔</span><span class="dock-btn-label">Chuông Đền: ${soundChimeEnabled ? 'BẬT' : 'TẮT'}</span>`;
        btn.classList.toggle('active', soundChimeEnabled);
    }
    if (soundChimeEnabled) playTempleChimeSound();
}

// ==========================================
// LIGHTING VISUAL MODES
// ==========================================
function updateLightingVisuals() {
    const btn = document.getElementById('btnNightMode');

    if (isNight) {
        scene.background.setHex(0x060411);
        scene.fog.color.setHex(0x0a0518);
        ambientLight.color.setHex(0x241445);
        ambientLight.intensity = 0.95;
        dirLight.color.setHex(0xa5b4fc);
        dirLight.intensity = 0.95;
        moonRimLight.intensity = 1.3;

        if (models.starfield) models.starfield.visible = true;
        if (models.moon) models.moon.visible = true;
        if (godRaysGroup) godRaysGroup.visible = true;

        lanternPointLights.forEach(item => { item.light.intensity = item.baseIntensity; });
        wisteriaGlowLights.forEach(light => { light.intensity = 2.2; });

        if (btn) {
            btn.innerHTML = '<span class="dock-btn-icon">🌙</span><span class="dock-btn-label">Không Gian: Đêm Tử Đằng</span>';
            btn.classList.add('active');
        }
    } else {
        // Dawn of Fujikasane (Hừng Đông Núi Tử Đằng)
        scene.background.setHex(0x2d1738);
        scene.fog.color.setHex(0x401f4c);
        ambientLight.color.setHex(0x5b335c);
        ambientLight.intensity = 1.25;
        dirLight.color.setHex(0xfde68a);
        dirLight.intensity = 1.35;
        moonRimLight.intensity = 0.3;

        if (models.starfield) models.starfield.visible = false;
        if (models.moon) models.moon.visible = true;
        if (godRaysGroup) godRaysGroup.visible = true;

        lanternPointLights.forEach(item => { item.light.intensity = item.baseIntensity * 0.45; });
        wisteriaGlowLights.forEach(light => { light.intensity = 1.2; });

        if (btn) {
            btn.innerHTML = '<span class="dock-btn-icon">🌅</span><span class="dock-btn-label">Không Gian: Hừng Đông</span>';
            btn.classList.remove('active');
        }
    }
}

// ==========================================
// INTERACTIVE RAYCASTING & FOCUS GLIDE
// ==========================================
function onCanvasClick(e) {
    // If clicking on UI, ignore
    if (e.target.id !== 'canvas3d') return;

    mouse.x = (e.clientX / window.innerWidth) * 2 - 1;
    mouse.y = -(e.clientY / window.innerHeight) * 2 + 1;

    raycaster.setFromCamera(mouse, camera);

    const hitObjects = [];
    ['torii', 'katana', 'wisteria', 'lantern', 'daruma', 'neko'].forEach(key => {
        if (models[key]) hitObjects.push(models[key]);
    });

    const intersects = raycaster.intersectObjects(hitObjects, true);
    if (intersects.length > 0) {
        let current = intersects[0].object;
        while (current && current.parent && !current.name) {
            current = current.parent;
        }
        if (current && current.name && VOCAB_DATABASE[current.name]) {
            focusObject(current.name);
        }
    }
}

// Start smooth camera glide without locking controls afterwards
function startCameraTransition(camEnd, targetEnd, duration = 900) {
    isTransitioning = true;
    transitionStartTime = performance.now();
    transitionDuration = duration;

    transitionStartCam.copy(camera.position);
    transitionStartTarget.copy(controls.target);

    transitionEndCam.copy(camEnd);
    transitionEndTarget.copy(targetEnd);

    if (isCinematic) setCinematicMode(false);
}

function focusObject(key) {
    const data = VOCAB_DATABASE[key];
    if (!data) return;

    currentActiveItem = data;
    currentVocabIndex = VOCAB_KEYS.indexOf(key);

    if (isCinematic) {
        setCinematicMode(false);
    }

    // Highlight Active Pill
    document.querySelectorAll('.obj-pill').forEach(p => p.classList.remove('active'));
    const activePill = document.getElementById(`pill-${key}`);
    if (activePill) {
        activePill.classList.add('active');
        activePill.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
    }

    // Smooth glide to object target
    startCameraTransition(data.camPos, data.lookAt, 900);

    // Play tranquil temple chime
    playTempleChimeSound();

    // Display Vocab Card with Tokyo Audio
    showModal(data, true);
}

function stepObject(direction) {
    currentVocabIndex = (currentVocabIndex + direction + VOCAB_KEYS.length) % VOCAB_KEYS.length;
    const nextKey = VOCAB_KEYS[currentVocabIndex];
    focusObject(nextKey);
}

function showModal(item, autoPlayAudio = false) {
    const modal = document.getElementById('vocabModal');
    if (!modal) return;

    document.getElementById('cardTag').innerText = item.tag;
    document.getElementById('cardKanji').innerText = item.kanji;
    document.getElementById('cardRomaji').innerText = item.romaji;
    document.getElementById('cardKana').innerText = item.kana;
    document.getElementById('cardMeaning').innerText = item.meaning;
    document.getElementById('cardCultureNote').innerHTML = item.culture;

    const counter = document.getElementById('cardStepCounter');
    if (counter) {
        counter.innerText = `${currentVocabIndex + 1} / ${VOCAB_KEYS.length}`;
    }

    modal.style.display = 'block';

    if (autoPlayAudio && window.speakText) {
        window.speakText(item.kanji, document.getElementById('cardAudioBtn'));
    }
}

function closeModal() {
    const modal = document.getElementById('vocabModal');
    if (modal) modal.style.display = 'none';
}

function speakCurrentCard() {
    if (currentActiveItem && window.speakText) {
        window.speakText(currentActiveItem.kanji, document.getElementById('cardAudioBtn'));
    }
}

// ==========================================
// CINEMATIC DRONE ROAM & DOCK CONTROLS
// ==========================================
function toggleCinematicRoam() {
    setCinematicMode(!isCinematic);
}

function setCinematicMode(enable) {
    isCinematic = enable;
    updateCinematicUI();
    if (isCinematic) {
        closeModal();
    }
}

function updateCinematicUI() {
    const overlay = document.getElementById('cinematicOverlay');
    const btnDock = document.getElementById('btnCinematic');
    const btnTop = document.getElementById('btnCinematicTop');

    if (overlay) overlay.classList.toggle('active', isCinematic);
    if (btnDock) {
        btnDock.classList.toggle('active', isCinematic);
        btnDock.innerHTML = `<span class="dock-btn-icon">🎬</span><span class="dock-btn-label">Bay Lượn Điện Ảnh: ${isCinematic ? 'BẬT' : 'TẮT'}</span>`;
    }
    if (btnTop) btnTop.classList.toggle('active', isCinematic);
}

function toggleAutoRotate() {
    autoRotate = !autoRotate;
    controls.autoRotate = autoRotate;
    const btn = document.getElementById('btnAutoRotate');
    if (btn) {
        btn.innerHTML = `<span class="dock-btn-icon">🔄</span><span class="dock-btn-label">Xoay 360°: ${autoRotate ? 'BẬT' : 'TẮT'}</span>`;
        btn.classList.toggle('active', autoRotate);
    }
}

function toggleNightMode() {
    isNight = !isNight;
    updateLightingVisuals();
    playTempleChimeSound();
}

function toggleParticles() {
    particlesActive = !particlesActive;
    if (sakuraParticles) sakuraParticles.visible = particlesActive;
    if (wisteriaParticles) wisteriaParticles.visible = particlesActive;
    if (fireflyParticles) fireflyParticles.visible = particlesActive;

    const btn = document.getElementById('btnParticles');
    if (btn) {
        btn.innerHTML = `<span class="dock-btn-icon">🪻</span><span class="dock-btn-label">Cánh Hoa & Đom Đóm: ${particlesActive ? 'BẬT' : 'TẮT'}</span>`;
        btn.classList.toggle('active', particlesActive);
    }
}

function resetView() {
    document.querySelectorAll('.obj-pill').forEach(p => p.classList.remove('active'));
    startCameraTransition(new THREE.Vector3(0, 3.4, 11.2), new THREE.Vector3(0, 2.2, 0), 900);
    showModal(VOCAB_DATABASE.torii, false);
    const toriiPill = document.getElementById('pill-torii');
    if (toriiPill) toriiPill.classList.add('active');
    playTempleChimeSound();
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

// ==========================================
// MAIN ANIMATION LOOP (120 FPS HIGH FIDELITY)
// ==========================================
let clock = new THREE.Clock();

function animate() {
    requestAnimationFrame(animate);

    const delta = clock.getDelta();
    const elapsedTime = clock.getElapsedTime();

    // 1. Camera Glide Transition or Cinematic Roam
    if (isTransitioning) {
        const now = performance.now();
        const elapsed = now - transitionStartTime;
        const t = Math.min(1.0, elapsed / transitionDuration);
        // Smooth Cubic Easing: 1 - (1 - t)^3
        const ease = 1 - Math.pow(1 - t, 3);

        camera.position.lerpVectors(transitionStartCam, transitionEndCam, ease);
        controls.target.lerpVectors(transitionStartTarget, transitionEndTarget, ease);

        if (t >= 1.0) {
            isTransitioning = false;
            camera.position.copy(transitionEndCam);
            controls.target.copy(transitionEndTarget);
        }
    } else if (isCinematic) {
        cinematicAngle += 0.20 * delta;
        const camX = Math.sin(cinematicAngle) * cinematicRadius;
        const camZ = Math.cos(cinematicAngle) * cinematicRadius;
        const camY = cinematicHeight + Math.sin(cinematicAngle * 1.5) * 0.7;

        camera.position.set(camX, camY, camZ);
        controls.target.set(0, 2.2, 0);
    }

    // 2. Flickering Stone Lantern Fire Light
    lanternPointLights.forEach(item => {
        if (isNight) {
            const flicker = Math.sin(elapsedTime * 8 + item.flickerOffset) * 0.35 +
                            (Math.random() - 0.5) * 0.25;
            item.light.intensity = item.baseIntensity + flicker;
        }
    });

    // 3. Swaying Shide Paper Streamers & Wisteria Blossom Clusters in Wind
    if (models.shideMeshes) {
        models.shideMeshes.forEach((shide, idx) => {
            shide.rotation.z = Math.sin(elapsedTime * 2.5 + idx * 0.8) * 0.12;
            shide.rotation.x = Math.cos(elapsedTime * 2.0 + idx * 0.5) * 0.08;
        });
    }

    if (models.wisteriaClusters) {
        models.wisteriaClusters.forEach(cluster => {
            const { phaseOffset, speed } = cluster.userData;
            cluster.rotation.z = Math.sin(elapsedTime * speed + phaseOffset) * 0.07;
            cluster.rotation.x = Math.cos(elapsedTime * (speed * 0.85) + phaseOffset) * 0.06;
        });
    }

    // 4. Volumetric God Rays Soft Breathing Pulsation
    if (godRaysGroup && godRaysGroup.visible) {
        const pulse = 0.07 + Math.sin(elapsedTime * 0.8) * 0.03;
        godRaysGroup.children.forEach(ray => {
            ray.material.opacity = pulse;
        });
    }

    // 5. Falling Sakura Blossom Petals
    if (particlesActive && sakuraGeo) {
        const pos = sakuraGeo.attributes.position.array;
        const spd = sakuraGeo.userData.speeds;
        const count = pos.length / 3;

        for (let i = 0; i < count; i++) {
            pos[i * 3] += spd[i * 3] + Math.sin(elapsedTime + i) * 0.005; // Wind curl
            pos[i * 3 + 1] += spd[i * 3 + 1];
            pos[i * 3 + 2] += spd[i * 3 + 2];

            if (pos[i * 3 + 1] < 0) {
                pos[i * 3 + 1] = 11.0;
                pos[i * 3] = (Math.random() - 0.5) * 22;
                pos[i * 3 + 2] = (Math.random() - 0.5) * 22;
            }
        }
        sakuraGeo.attributes.position.needsUpdate = true;
    }

    // 6. Upward Swirling Wisteria Embers (Kimetsu Spirit Spores)
    if (particlesActive && wisteriaGeo) {
        const pos = wisteriaGeo.attributes.position.array;
        const spd = wisteriaGeo.userData.speeds;
        const count = pos.length / 3;

        for (let i = 0; i < count; i++) {
            pos[i * 3] += spd[i * 3] + Math.cos(elapsedTime * 1.5 + i) * 0.008;
            pos[i * 3 + 1] += spd[i * 3 + 1];
            pos[i * 3 + 2] += spd[i * 3 + 2] + Math.sin(elapsedTime * 1.5 + i) * 0.008;

            if (pos[i * 3 + 1] > 7.5) {
                pos[i * 3 + 1] = 0.2;
                pos[i * 3] = (Math.random() - 0.5) * 16;
                pos[i * 3 + 2] = (Math.random() - 0.5) * 16;
            }
        }
        wisteriaGeo.attributes.position.needsUpdate = true;
    }

    // 7. Fireflies Floating
    if (particlesActive && fireflyGeo) {
        const pos = fireflyGeo.attributes.position.array;
        const spd = fireflyGeo.userData.speeds;
        const count = pos.length / 3;

        for (let i = 0; i < count; i++) {
            pos[i * 3] += Math.sin(elapsedTime * 2 + i) * 0.006;
            pos[i * 3 + 1] += Math.cos(elapsedTime * 2 + i) * 0.004;
            pos[i * 3 + 2] += spd[i * 3 + 2];

            if (pos[i * 3 + 2] > 7) pos[i * 3 + 2] = -5;
        }
        fireflyGeo.attributes.position.needsUpdate = true;
    }

    // Controls update (when not transitioning, OrbitControls has 100% full, smooth control)
    controls.update();
    renderer.render(scene, camera);
}

// Start application when DOM is ready
window.addEventListener('DOMContentLoaded', init);
