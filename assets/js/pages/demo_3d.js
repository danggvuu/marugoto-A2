/* ==========================================================================
   ⛩️ DEMO 3D - KIMETSU NO YAIBA MT. FUJIKASANE WISTERIA SHRINE
   WebGL Interactive Experience (Three.js r128)
   ========================================================================== */

let scene, camera, renderer, controls;
let isNight = true;
let autoRotate = true;
let particlesActive = true;
let isCinematic = true; // Start in majestic cinematic mode!
let soundChimeEnabled = true;

// Lights
let dirLight, ambientLight, moonRimLight;
let lanternPointLights = [];
let wisteriaGlowLights = [];

// Particle Systems
let sakuraGeo, sakuraParticles;
let wisteriaGeo, wisteriaParticles;
let fireflyGeo, fireflyParticles;

// God Rays & Moon Meshes
let godRaysGroup;
let moonMesh, moonHaloMesh;

// Model Object References & Camera Targets
const models = {};
const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();

// Target camera positions for smooth glide
let targetCamPos = new THREE.Vector3(0, 3.4, 9.8);
let targetLookAt = new THREE.Vector3(0, 2.0, 0);

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
        camPos: new THREE.Vector3(0, 2.8, 6.2),
        lookAt: new THREE.Vector3(0, 2.4, 0)
    },
    katana: {
        key: 'katana',
        tag: 'Bảo kiếm Diệt Quỷ • Sát Quỷ Đội',
        kanji: '日輪刀',
        romaji: 'Nichirin-tō',
        kana: 'にちりんとう (Nichirin-tō)',
        meaning: 'Thanh kiếm Nichirin rèn từ Cát sắt đỏ và Quặng đỏ thẫm hấp thụ ánh sáng mặt trời vĩnh cửu.',
        culture: '⚔️ Vũ khí tối thượng của các kiếm sĩ Sát Quỷ Đội (鬼殺隊). Khi rơi vào tay kiếm sĩ có thực lực, lưỡi gươm sẽ đổi màu theo hơi thở (Hơi Thở Của Nước xanh thẳm, Mặt Trời đỏ rực). Đặt trang trọng trên giá Katanakake sơn mài đen.',
        camPos: new THREE.Vector3(0.0, 1.4, 4.0),
        lookAt: new THREE.Vector3(0.0, 0.95, 2.8)
    },
    wisteria: {
        key: 'wisteria',
        tag: 'Thần Mộc Xua Quỷ • Kimetsu no Yaiba',
        kanji: '藤の花',
        romaji: 'Fuji no hana',
        kana: 'ふじのはな (Fuji no hana)',
        meaning: 'Hoa Tử Đằng linh thiêng với những chùm hoa tím biếc rủ xuống như thác nước huyền ảo.',
        culture: '🪻 Loài hoa nở rộ bốn mùa trên đỉnh núi Fujikasane. Hương thơm và độc tố của hoa Tử Đằng là khắc tinh số một khiến loài quỷ khiếp sợ và không bao giờ dám đến gần, tạo thành kết giới thiêng liêng bảo vệ loài người.',
        camPos: new THREE.Vector3(-3.2, 3.2, 3.6),
        lookAt: new THREE.Vector3(-3.0, 2.8, 0)
    },
    lantern: {
        key: 'lantern',
        tag: 'Dẫn Lối Thần Đạo • Cổ Kính',
        kanji: '燈籠',
        romaji: 'Tōrō',
        kana: 'とうろう (Tōrō)',
        meaning: 'Đèn lồng đá Kasuga cổ kính chạm khắc tinh xảo, thắp sáng ngọn lửa ấm áp giữa đêm sương.',
        culture: '🏮 Được đặt dọc hai bên lối vào đền thờ (Sando). Ngọn lửa thiêng bập bùng bên trong mang ý nghĩa xua tan bóng tối u ám, soi tỏ tâm hồn thanh tịnh và dẫn bước lữ khách trên con đường hướng thiện.',
        camPos: new THREE.Vector3(-2.6, 1.9, 4.0),
        lookAt: new THREE.Vector3(-2.6, 1.4, 1.8)
    },
    fuji: {
        key: 'fuji',
        tag: 'Linh Sơn Hùng Vĩ • Di Sản Thế Giới',
        kanji: '富士山',
        romaji: 'Fuji-san',
        kana: 'ふじさん (Fuji-san)',
        meaning: 'Núi Phú Sĩ tuyết phủ ngàn năm cùng ánh trăng rằm vằng vặc (満月 - Mangetsu).',
        culture: '🗻 Đỉnh núi linh thiêng cao 3.776m, biểu tượng trường tồn bất diệt của đất nước Mặt Trời Mọc. Xuất hiện trong Bài 3 & Bài 18 giáo trình Marugoto và là nguồn cảm hứng bất tận trong tranh Ukiyo-e của Hokusai.',
        camPos: new THREE.Vector3(0, 4.5, 12.5),
        lookAt: new THREE.Vector3(0, 4.2, -12)
    },
    daruma: {
        key: 'daruma',
        tag: 'Búp Bê Ý Chí & Ước Nguyện',
        kanji: 'だるま',
        romaji: 'Daruma',
        kana: 'だるま (Daruma)',
        meaning: 'Búp bê tròn đỏ truyền thống tượng trưng cho tinh thần bất khuất "Thất ngã bát khởi" (Ngã 7 lần, đứng dậy 8 lần).',
        culture: '🎎 Khắc chữ vàng "Tất Thắng" (必勝) và "Phúc" (福). Người Nhật khi lập chí lớn sẽ điểm nhãn mắt trái; khi vượt qua thử thách vẻ vang sẽ vẽ nốt mắt phải để tạ ơn thần linh.',
        camPos: new THREE.Vector3(-1.8, 1.45, 3.6),
        lookAt: new THREE.Vector3(-1.8, 0.85, 1.6)
    },
    neko: {
        key: 'neko',
        tag: 'Phong Thủy Cầu May • Tài Lộc',
        kanji: '招き猫',
        romaji: 'Maneki-neko',
        kana: 'まねきねこ (Maneki-neko)',
        meaning: 'Mèo may mắn sứ trắng vẫy tay đón tài lộc, mang lục lạc vàng và đồng tiền cổ Koban.',
        culture: '🐱 Tay phải giơ cao vẫy gọi phúc lành, tiền cổ ghi khắc "Thiên vạn lượng" (千万両 - Senmanryō). Thường được bày trang trọng tại cổng vào cửa hàng, mang lại sự ấm no và bình an cho gia chủ.',
        camPos: new THREE.Vector3(1.8, 1.45, 3.6),
        lookAt: new THREE.Vector3(1.8, 0.85, 1.6)
    },
    sakura: {
        key: 'sakura',
        tag: 'Quốc Hoa • Vẻ Đẹp Khoảnh Khắc',
        kanji: '桜の花びら',
        romaji: 'Sakura no hanabira',
        kana: 'さくら の はなびら (Sakura)',
        meaning: 'Những cánh hoa anh đào thanh khiết chao liệng trong làn gió đêm huyền ảo.',
        culture: '🌸 Triết lý "Mono no aware" (U hoài trước vẻ đẹp phù du) - trân quý từng phút giây hiện tại. Sắc hồng hoa anh đào hòa quyện cùng sắc tím hoa Tử Đằng tạo nên bức tranh thiên nhiên tuyệt mỹ.',
        camPos: new THREE.Vector3(0, 3.4, 9.2),
        lookAt: new THREE.Vector3(0, 2.2, 0)
    }
};

let currentActiveItem = VOCAB_DATABASE.torii;

// ==========================================
// INITIALIZATION
// ==========================================
function init() {
    const canvas = document.getElementById('canvas3d');

    // 1. Scene & Mystical Wisteria Atmosphere
    scene = new THREE.Scene();
    scene.background = new THREE.Color(0x070512);
    scene.fog = new THREE.FogExp2(0x0e071e, 0.026);

    // 2. Camera Setup
    camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 200);
    camera.position.copy(targetCamPos);

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

    // 4. Orbit Controls
    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
    controls.maxPolarAngle = Math.PI / 2 - 0.02; // Keep camera above sacred ground
    controls.minDistance = 2.2;
    controls.maxDistance = 32;
    controls.target.copy(targetLookAt);

    // 5. Lighting Setup
    setupLighting();

    // 6. Build Scene Geometry
    buildStarfield();
    buildFullMoonAndGodRays();
    buildMountainRanges();
    buildGroundAndSteps();
    buildGrandToriiGate();
    buildWisteriaTrees();
    buildNichirinKatana();
    buildStoneLanterns();
    buildDarumaDoll();
    buildManekiNeko();
    buildParticles();

    // 7. Event Handlers
    window.addEventListener('resize', onWindowResize);
    canvas.addEventListener('click', onCanvasClick);
    canvas.addEventListener('pointerdown', onUserInteraction);

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
    ambientLight = new THREE.AmbientLight(0x28124d, 0.85);
    scene.add(ambientLight);

    // Directional light: Silvery moonbeam casting soft shadows
    dirLight = new THREE.DirectionalLight(0x93c5fd, 0.75);
    dirLight.position.set(6, 20, 10);
    dirLight.castShadow = true;
    dirLight.shadow.mapSize.width = 2048;
    dirLight.shadow.mapSize.height = 2048;
    dirLight.shadow.camera.near = 0.5;
    dirLight.shadow.camera.far = 50;
    dirLight.shadow.camera.left = -12;
    dirLight.shadow.camera.right = 12;
    dirLight.shadow.camera.top = 12;
    dirLight.shadow.camera.bottom = -12;
    dirLight.shadow.bias = -0.0005;
    scene.add(dirLight);

    // Moon Rim Light (from behind the mountain towards the Torii gate)
    moonRimLight = new THREE.DirectionalLight(0xa855f7, 0.95);
    moonRimLight.position.set(0, 15, -20);
    scene.add(moonRimLight);
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
    ctx.fillStyle = 'rgba(148, 163, 184, 0.25)';
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

    // Oval petal shape with gradient
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
    const starCount = 1200;
    const starGeo = new THREE.BufferGeometry();
    const starPos = new Float32Array(starCount * 3);
    const starColors = new Float32Array(starCount * 3);

    for (let i = 0; i < starCount; i++) {
        // Distribute stars on a wide upper celestial dome
        const theta = 2 * Math.PI * Math.random();
        const phi = Math.acos(2 * Math.random() - 1);
        const radius = 90 + Math.random() * 40;

        starPos[i * 3] = radius * Math.sin(phi) * Math.cos(theta);
        starPos[i * 3 + 1] = Math.abs(radius * Math.cos(phi)) + 5; // Keep above horizon
        starPos[i * 3 + 2] = radius * Math.sin(phi) * Math.sin(theta);

        // Subtly colored stars (white, cyan, purple)
        const rand = Math.random();
        if (rand > 0.7) {
            starColors[i * 3] = 0.8; starColors[i * 3 + 1] = 0.7; starColors[i * 3 + 2] = 1.0; // Violet
        } else if (rand > 0.4) {
            starColors[i * 3] = 0.7; starColors[i * 3 + 1] = 0.9; starColors[i * 3 + 2] = 1.0; // Ice blue
        } else {
            starColors[i * 3] = 1.0; starColors[i * 3 + 1] = 1.0; starColors[i * 3 + 2] = 1.0; // White
        }
    }

    starGeo.setAttribute('position', new THREE.BufferAttribute(starPos, 3));
    starGeo.setAttribute('color', new THREE.BufferAttribute(starColors, 3));

    const starMat = new THREE.PointsMaterial({
        size: 0.65,
        vertexColors: true,
        transparent: true,
        opacity: 0.9,
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
    moonGroup.position.set(0, 14, -32);

    // Core Moon Disc
    const moonTex = createMoonTexture();
    const moonGeo = new THREE.CircleGeometry(5.2, 64);
    const moonMat = new THREE.MeshBasicMaterial({
        map: moonTex,
        transparent: true,
        opacity: 0.98
    });
    moonMesh = new THREE.Mesh(moonGeo, moonMat);
    moonGroup.add(moonMesh);

    // Multi-Layered Inner & Outer Moon Glow Halo
    const haloTex = createRadialGlowTexture('rgba(224, 231, 255, 1)', 'rgba(168, 85, 247, 0)');
    const haloGeo = new THREE.PlaneGeometry(16, 16);
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
    const outerHaloGeo = new THREE.PlaneGeometry(28, 28);
    const outerHaloMat = new THREE.MeshBasicMaterial({
        map: haloTex,
        transparent: true,
        blending: THREE.AdditiveBlending,
        depthWrite: false,
        opacity: 0.35,
        color: 0x9333ea
    });
    const outerHalo = new THREE.Mesh(outerHaloGeo, outerHaloMat);
    outerHalo.position.z = -0.2;
    moonGroup.add(outerHalo);

    scene.add(moonGroup);
    models.moon = moonGroup;

    // Volumetric God Rays (Slanted moonbeams streaming into the valley)
    godRaysGroup = new THREE.Group();
    const rayMat = new THREE.MeshBasicMaterial({
        color: 0xd8b4fe,
        transparent: true,
        opacity: 0.08,
        blending: THREE.AdditiveBlending,
        side: THREE.DoubleSide,
        depthWrite: false
    });

    const angles = [-0.25, -0.1, 0.08, 0.22];
    angles.forEach((ang, idx) => {
        const rayGeo = new THREE.CylinderGeometry(0.6, 5.0 + idx * 0.8, 38, 16, 1, true);
        const ray = new THREE.Mesh(rayGeo, rayMat);
        ray.position.set(ang * 24, 10, -18);
        ray.rotation.z = ang * 0.7;
        ray.rotation.x = 0.2;
        godRaysGroup.add(ray);
    });
    scene.add(godRaysGroup);
}

// 3. Layered Mountain Silhouettes & Snow-Capped Mt. Fuji
function buildMountainRanges() {
    const mountains = new THREE.Group();
    mountains.name = 'fuji';
    mountains.position.set(0, 0, -26);

    // Far Background Mountain Ridge (Deep indigo silhouettes)
    const ridgeMat = new THREE.MeshBasicMaterial({ color: 0x090518 });
    const ridgePoints = [
        -40, 0, -35, 7, -30, 4, -24, 9, -18, 5, -12, 8, -6, 4,
        0, 6, 6, 4, 12, 8, 18, 5, 24, 9, 30, 4, 35, 7, 40, 0
    ];
    const shape = new THREE.Shape();
    shape.moveTo(-45, -2);
    for (let i = 0; i < ridgePoints.length; i += 2) {
        shape.lineTo(ridgePoints[i], ridgePoints[i + 1]);
    }
    shape.lineTo(45, -2);
    shape.closePath();
    const ridgeMesh = new THREE.Mesh(new THREE.ShapeGeometry(shape), ridgeMat);
    ridgeMesh.position.z = -8;
    mountains.add(ridgeMesh);

    // Mount Fuji Cone (Sacred Profile with concave curve)
    const fujiMat = new THREE.MeshStandardMaterial({
        color: 0x140d30,
        roughness: 0.95,
        metalness: 0.05
    });
    const fujiGeo = new THREE.CylinderGeometry(1.2, 22, 16, 64, 1, true);
    const fujiBody = new THREE.Mesh(fujiGeo, fujiMat);
    fujiBody.position.set(0, 7.5, 0);
    mountains.add(fujiBody);

    // Fuji Snow-Capped Summit (Glowing under moonlight)
    const snowMat = new THREE.MeshStandardMaterial({
        color: 0xf1f5f9,
        roughness: 0.35,
        metalness: 0.2,
        emissive: 0x93c5fd,
        emissiveIntensity: 0.2
    });
    const snowGeo = new THREE.ConeGeometry(5.8, 6.5, 64);
    const snowCap = new THREE.Mesh(snowGeo, snowMat);
    snowCap.position.set(0, 13.8, 0);
    mountains.add(snowCap);

    scene.add(mountains);
    models.fuji = mountains;
}

// 4. Sacred Ground, Flagstone Sando Path & Weathered Stairs
function buildGroundAndSteps() {
    const groundGroup = new THREE.Group();

    // Main Sacred Island Plateau
    const islandGeo = new THREE.CylinderGeometry(11, 11.6, 0.9, 64);
    const islandMat = new THREE.MeshStandardMaterial({
        color: 0x110c24,
        roughness: 0.92,
        metalness: 0.08
    });
    const island = new THREE.Mesh(islandGeo, islandMat);
    island.position.y = -0.45;
    island.receiveShadow = true;
    groundGroup.add(island);

    // Weathered Stone Terrace Border
    const rimGeo = new THREE.TorusGeometry(11, 0.25, 12, 64);
    const stoneRimMat = new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.85 });
    const rim = new THREE.Mesh(rimGeo, stoneRimMat);
    rim.rotation.x = Math.PI / 2;
    rim.position.y = 0.02;
    groundGroup.add(rim);

    // Central Sando Flagstone Path (Lối vào đền)
    const pathMat = new THREE.MeshStandardMaterial({
        color: 0x24283b,
        roughness: 0.8,
        metalness: 0.1
    });
    const path = new THREE.Mesh(new THREE.PlaneGeometry(2.4, 16), pathMat);
    path.rotation.x = -Math.PI / 2;
    path.position.set(0, 0.015, 2.2);
    path.receiveShadow = true;
    groundGroup.add(path);

    // Weathered Stone Stairs (Bậc đá Ishidan trước cổng)
    const stepMat = new THREE.MeshStandardMaterial({ color: 0x3b4252, roughness: 0.85 });
    for (let s = 0; s < 4; s++) {
        const step = new THREE.Mesh(new THREE.BoxGeometry(3.0 - s * 0.15, 0.1, 0.7), stepMat);
        step.position.set(0, s * 0.09, 3.6 - s * 0.65);
        step.receiveShadow = true;
        step.castShadow = true;
        groundGroup.add(step);
    }

    scene.add(groundGroup);
    models.ground = groundGroup;
}

// ==========================================
// GRAND TORII SHRINE ENTRANCE BUILDER
// ==========================================
function buildGrandToriiGate() {
    const torii = new THREE.Group();
    torii.name = 'torii';

    // Materials
    const vermilionMat = new THREE.MeshStandardMaterial({
        color: 0xc02626,
        roughness: 0.32,
        metalness: 0.12
    });
    const blackLacquerMat = new THREE.MeshStandardMaterial({
        color: 0x0f1117,
        roughness: 0.2,
        metalness: 0.35
    });
    const stoneBaseMat = new THREE.MeshStandardMaterial({
        color: 0x475569,
        roughness: 0.9
    });
    const goldMat = new THREE.MeshStandardMaterial({
        color: 0xf59e0b,
        roughness: 0.3,
        metalness: 0.75
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

    const dist = 2.0;
    const height = 4.6;
    const radius = 0.23;

    // 1. Two Grand Vermilion Hashira Pillars with Lacquer Bases
    [-dist, dist].forEach(x => {
        // Kamebara (Stone base plinth)
        const plinth = new THREE.Mesh(new THREE.CylinderGeometry(0.42, 0.48, 0.4, 24), stoneBaseMat);
        plinth.position.set(x, 0.2, 0);
        plinth.castShadow = true;
        torii.add(plinth);

        // Black Lacquer Collar & Gold Band
        const collar = new THREE.Mesh(new THREE.CylinderGeometry(0.32, 0.32, 0.32, 24), blackLacquerMat);
        collar.position.set(x, 0.52, 0);
        torii.add(collar);

        const goldRing = new THREE.Mesh(new THREE.CylinderGeometry(0.33, 0.33, 0.05, 24), goldMat);
        goldRing.position.set(x, 0.69, 0);
        torii.add(goldRing);

        // Main Incline Vermilion Pillar
        const pillar = new THREE.Mesh(new THREE.CylinderGeometry(radius * 0.92, radius, height, 32), vermilionMat);
        pillar.position.set(x, height / 2 + 0.4, 0);
        pillar.rotation.z = x > 0 ? 0.035 : -0.035;
        pillar.castShadow = true;
        torii.add(pillar);

        // Kusabi (Wooden wedges at Nuki tie-beam)
        const wedge = new THREE.Mesh(new THREE.BoxGeometry(0.1, 0.32, 0.55), vermilionMat);
        wedge.position.set(x, 3.8, 0);
        torii.add(wedge);
    });

    // 2. Kasagi (Top sweeping curved beam with black copper ridge)
    const kasagiCurve = new THREE.QuadraticBezierCurve3(
        new THREE.Vector3(-3.4, 5.25, 0),
        new THREE.Vector3(0, 4.95, 0),
        new THREE.Vector3(3.4, 5.25, 0)
    );
    const kasagi = new THREE.Mesh(new THREE.TubeGeometry(kasagiCurve, 40, 0.22, 12, false), blackLacquerMat);
    kasagi.scale.set(1, 1.25, 0.9);
    kasagi.castShadow = true;
    torii.add(kasagi);

    // 3. Shimaki (Secondary vermilion beam directly underneath)
    const shimaki = new THREE.Mesh(new THREE.BoxGeometry(6.0, 0.28, 0.44), vermilionMat);
    shimaki.position.set(0, 4.75, 0);
    shimaki.castShadow = true;
    torii.add(shimaki);

    // 4. Nuki (Lower tie-beam interlocking pillars)
    const nuki = new THREE.Mesh(new THREE.BoxGeometry(5.2, 0.25, 0.32), vermilionMat);
    nuki.position.set(0, 3.8, 0);
    nuki.castShadow = true;
    torii.add(nuki);

    // 5. Gakuzuka (Center Plaque inscribed "藤襲山" - Mt. Fujikasane)
    const gakuzuka = new THREE.Mesh(new THREE.BoxGeometry(0.46, 0.72, 0.1), blackLacquerMat);
    gakuzuka.position.set(0, 4.28, 0.16);
    torii.add(gakuzuka);

    const gakuzukaFrame = new THREE.Mesh(new THREE.BoxGeometry(0.5, 0.76, 0.08), goldMat);
    gakuzukaFrame.position.set(0, 4.28, 0.14);
    torii.add(gakuzukaFrame);

    // 6. Sacred Braided Straw Rope (Shimenawa - 注連縄)
    const shimenawaCurve = new THREE.QuadraticBezierCurve3(
        new THREE.Vector3(-dist + 0.1, 3.65, 0.15),
        new THREE.Vector3(0, 3.25, 0.22),
        new THREE.Vector3(dist - 0.1, 3.65, 0.15)
    );
    const shimenawa = new THREE.Mesh(new THREE.TubeGeometry(shimenawaCurve, 32, 0.09, 10, false), shimenawaStrawMat);
    torii.add(shimenawa);

    // 7. Hanging White Zigzag Paper Streamers (Shide - 紙垂)
    const shidePositions = [-1.1, -0.4, 0.4, 1.1];
    models.shideMeshes = [];
    shidePositions.forEach(x => {
        const shideGroup = new THREE.Group();
        shideGroup.position.set(x, 3.32, 0.2);

        // 3 zigzag segments for authentic paper shide
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
// KIMETSU GLOWING WISTERIA & SAKURA TREES
// ==========================================
function buildWisteriaTrees() {
    const wisteriaGroup = new THREE.Group();
    wisteriaGroup.name = 'wisteria';

    const barkMat = new THREE.MeshStandardMaterial({
        color: 0x2d2424,
        roughness: 0.9,
        metalness: 0.05
    });

    // Cascading Wisteria Flower Cluster Material (Emissive Violet Glow)
    const wisteriaClusterMat = new THREE.MeshStandardMaterial({
        color: 0x9333ea,
        emissive: 0xa855f7,
        emissiveIntensity: 0.75,
        roughness: 0.4,
        metalness: 0.1
    });

    const wisteriaTipMat = new THREE.MeshStandardMaterial({
        color: 0xe879f9,
        emissive: 0xf0abfc,
        emissiveIntensity: 0.65,
        roughness: 0.35
    });

    const sakuraLeafMat = new THREE.MeshStandardMaterial({
        color: 0xf472b6,
        roughness: 0.6
    });

    models.wisteriaClusters = [];

    // Helper: Build a single twisted wisteria tree with cascading clusters
    function createWisteriaTree(x, z, scaleX) {
        const tree = new THREE.Group();
        tree.position.set(x, 0, z);

        // Twisted trunk using curved tube
        const trunkCurve = new THREE.CatmullRomCurve3([
            new THREE.Vector3(0, 0, 0),
            new THREE.Vector3(scaleX * 0.3, 1.4, 0.1),
            new THREE.Vector3(scaleX * 0.6, 2.8, -0.2),
            new THREE.Vector3(scaleX * 0.9, 3.8, 0.1)
        ]);
        const trunk = new THREE.Mesh(new THREE.TubeGeometry(trunkCurve, 20, 0.24, 10, false), barkMat);
        trunk.castShadow = true;
        tree.add(trunk);

        // Sweeping branches
        const branchOffsets = [
            { x: scaleX * 1.5, y: 4.2, z: 0.8 },
            { x: scaleX * 1.8, y: 4.0, z: -0.6 },
            { x: scaleX * 0.7, y: 4.4, z: 0.4 },
            { x: scaleX * 1.2, y: 4.6, z: -1.0 }
        ];

        branchOffsets.forEach(b => {
            const bCurve = new THREE.LineCurve3(
                new THREE.Vector3(scaleX * 0.9, 3.8, 0.1),
                new THREE.Vector3(b.x, b.y, b.z)
            );
            const branch = new THREE.Mesh(new THREE.TubeGeometry(bCurve, 10, 0.12, 8, false), barkMat);
            tree.add(branch);

            // Sakura foliage cloud at branch head
            const foliage = new THREE.Mesh(new THREE.SphereGeometry(0.7, 12, 12), sakuraLeafMat);
            foliage.position.set(b.x, b.y + 0.2, b.z);
            foliage.scale.set(1.4, 0.7, 1.2);
            tree.add(foliage);

            // Cascading Wisteria Flower Clusters hanging down (Racemes)
            for (let c = 0; c < 3; c++) {
                const clusterGroup = new THREE.Group();
                clusterGroup.position.set(
                    b.x + (Math.random() - 0.5) * 0.6,
                    b.y - 0.1,
                    b.z + (Math.random() - 0.5) * 0.6
                );

                // Multi-tier tapered droplets
                const tiers = 4;
                for (let t = 0; t < tiers; t++) {
                    const radius = (tiers - t) * 0.045 + 0.03;
                    const cMat = t < 2 ? wisteriaClusterMat : wisteriaTipMat;
                    const tierMesh = new THREE.Mesh(new THREE.SphereGeometry(radius, 8, 8), cMat);
                    tierMesh.position.y = -t * 0.24;
                    tierMesh.scale.set(1, 1.4, 1);
                    clusterGroup.add(tierMesh);
                }

                tree.add(clusterGroup);
                models.wisteriaClusters.push(clusterGroup);
            }
        });

        return tree;
    }

    // Left and Right Flanking Ancient Wisteria Trees framing the Torii
    const leftTree = createWisteriaTree(-3.5, 0.5, -1);
    const rightTree = createWisteriaTree(3.5, 0.5, 1);
    wisteriaGroup.add(leftTree);
    wisteriaGroup.add(rightTree);

    // Ethereal Purple Point Lights casting wisteria glow on the ground & pillars
    const leftWisteriaGlow = new THREE.PointLight(0xa855f7, 2.2, 8);
    leftWisteriaGlow.position.set(-3.5, 3.2, 0.8);
    scene.add(leftWisteriaGlow);
    wisteriaGlowLights.push(leftWisteriaGlow);

    const rightWisteriaGlow = new THREE.PointLight(0xa855f7, 2.2, 8);
    rightWisteriaGlow.position.set(3.5, 3.2, 0.8);
    scene.add(rightWisteriaGlow);
    wisteriaGlowLights.push(rightWisteriaGlow);

    scene.add(wisteriaGroup);
    models.wisteria = wisteriaGroup;
}

// ==========================================
// DEMON SLAYER NICHIRIN KATANA ON STAND
// ==========================================
function buildNichirinKatana() {
    const katanaGroup = new THREE.Group();
    katanaGroup.name = 'katana';
    katanaGroup.position.set(0.0, 0.0, 2.8);

    // 1. Black Lacquer Katanakake Sword Display Stand
    const standMat = new THREE.MeshStandardMaterial({
        color: 0x111111,
        roughness: 0.18,
        metalness: 0.35
    });
    const goldTrimMat = new THREE.MeshStandardMaterial({
        color: 0xf59e0b,
        roughness: 0.25,
        metalness: 0.8
    });

    // Stand Base Plate
    const standBase = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.08, 0.5), standMat);
    standBase.position.y = 0.04;
    standBase.castShadow = true;
    katanaGroup.add(standBase);

    // Stand Golden Crest Emblem (Mitsudomoe circle)
    const crest = new THREE.Mesh(new THREE.CircleGeometry(0.09, 16), goldTrimMat);
    crest.position.set(0, 0.05, 0.26);
    katanaGroup.add(crest);

    // Left and Right Upright Notched Arms
    [-0.55, 0.55].forEach(x => {
        const arm = new THREE.Mesh(new THREE.BoxGeometry(0.08, 0.65, 0.22), standMat);
        arm.position.set(x, 0.36, 0);
        arm.castShadow = true;
        katanaGroup.add(arm);

        // Gold finial on top of stand arm
        const finial = new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.05, 0.04, 12), goldTrimMat);
        finial.position.set(x, 0.7, 0);
        katanaGroup.add(finial);
    });

    // 2. Glossy Black Lacquer Saya (Scabbard) resting on lower rack
    const sayaMat = new THREE.MeshStandardMaterial({
        color: 0x16161a,
        roughness: 0.15,
        metalness: 0.3
    });
    const sayaCurve = new THREE.QuadraticBezierCurve3(
        new THREE.Vector3(-0.75, 0.35, 0),
        new THREE.Vector3(0, 0.33, 0),
        new THREE.Vector3(0.75, 0.37, 0)
    );
    const saya = new THREE.Mesh(new THREE.TubeGeometry(sayaCurve, 24, 0.045, 12, false), sayaMat);
    saya.castShadow = true;
    katanaGroup.add(saya);

    // Saya Golden Kojiri (tip) and Kurikata (cord knot)
    const kojiri = new THREE.Mesh(new THREE.CylinderGeometry(0.048, 0.048, 0.06, 12), goldTrimMat);
    kojiri.position.set(0.75, 0.37, 0);
    kojiri.rotation.z = Math.PI / 2;
    katanaGroup.add(kojiri);

    // 3. The Nichirin Katana Blade resting on upper rack
    const steelBladeMat = new THREE.MeshStandardMaterial({
        color: 0xdde6ed,
        roughness: 0.18,
        metalness: 0.95
    });

    // Razor Curved Blade with Sori
    const bladeCurve = new THREE.QuadraticBezierCurve3(
        new THREE.Vector3(-0.25, 0.60, 0),
        new THREE.Vector3(0.35, 0.58, 0),
        new THREE.Vector3(0.95, 0.63, 0)
    );
    const blade = new THREE.Mesh(new THREE.TubeGeometry(bladeCurve, 24, 0.032, 8, false), steelBladeMat);
    blade.scale.set(1, 1.4, 0.35); // Flattened razor blade edge
    blade.castShadow = true;
    katanaGroup.add(blade);

    // Habaki (Golden blade collar)
    const habaki = new THREE.Mesh(new THREE.BoxGeometry(0.08, 0.07, 0.05), goldTrimMat);
    habaki.position.set(-0.24, 0.60, 0);
    katanaGroup.add(habaki);

    // Tsuba (Ornate Demon Slayer Guard - Flame / Sun Motif)
    const tsuba = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.12, 0.02, 24), goldTrimMat);
    tsuba.position.set(-0.29, 0.60, 0);
    tsuba.rotation.z = Math.PI / 2;
    katanaGroup.add(tsuba);

    // Tsuka (Handle wrapped in black and white diamond cord)
    const tsukaMat = new THREE.MeshStandardMaterial({ color: 0x0f172a, roughness: 0.5 });
    const tsuka = new THREE.Mesh(new THREE.CylinderGeometry(0.038, 0.038, 0.45, 12), tsukaMat);
    tsuka.position.set(-0.52, 0.61, 0);
    tsuka.rotation.z = Math.PI / 2;
    tsuka.castShadow = true;
    katanaGroup.add(tsuka);

    // Kashira (Gold pommel cap)
    const kashira = new THREE.Mesh(new THREE.CylinderGeometry(0.042, 0.042, 0.04, 12), goldTrimMat);
    kashira.position.set(-0.75, 0.61, 0);
    kashira.rotation.z = Math.PI / 2;
    katanaGroup.add(kashira);

    scene.add(katanaGroup);
    models.katana = katanaGroup;
}

// ==========================================
// CARVED STONE TORO LANTERNS WITH FLICKERING FIRE
// ==========================================
function buildStoneLanterns() {
    const stoneMat = new THREE.MeshStandardMaterial({
        color: 0x475569,
        roughness: 0.88
    });
    const fireMeshMat = new THREE.MeshBasicMaterial({
        color: 0xffa500
    });

    models.lanterns = [];
    lanternPointLights = [];

    [-2.5, 2.5].forEach((x, idx) => {
        const lantern = new THREE.Group();
        lantern.name = 'lantern';
        lantern.position.set(x, 0, 1.8);

        // Kiso (Hexagonal Stone Base)
        const base = new THREE.Mesh(new THREE.CylinderGeometry(0.44, 0.55, 0.35, 6), stoneMat);
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

        // Hōju (Sacred Flaming Jewel finial)
        const hoju = new THREE.Mesh(new THREE.SphereGeometry(0.12, 12, 12), stoneMat);
        hoju.position.y = 2.58;
        lantern.add(hoju);

        // Warm Flickering Flame Point Light
        const pLight = new THREE.PointLight(0xff8c1a, 2.4, 8);
        pLight.position.set(x, 1.9, 1.8);
        pLight.castShadow = true;
        pLight.shadow.bias = -0.002;
        scene.add(pLight);

        lanternPointLights.push({
            light: pLight,
            baseIntensity: 2.4,
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
    daruma.position.set(-1.8, 0, 1.6);

    // Weathered Stone Pedestal
    const altar = new THREE.Mesh(new THREE.CylinderGeometry(0.45, 0.52, 0.42, 16), new THREE.MeshStandardMaterial({ color: 0x334155 }));
    altar.position.y = 0.21;
    altar.castShadow = true;
    daruma.add(altar);

    // Crimson Lacquer Roly-Poly Body
    const bodyMat = new THREE.MeshStandardMaterial({
        color: 0xdc2626,
        roughness: 0.28,
        metalness: 0.15
    });
    const body = new THREE.Mesh(new THREE.SphereGeometry(0.38, 32, 32), bodyMat);
    body.position.y = 0.65;
    body.scale.set(1.12, 1.0, 0.98);
    body.castShadow = true;
    daruma.add(body);

    // White Face Plate
    const faceMat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.4 });
    const face = new THREE.Mesh(new THREE.CircleGeometry(0.24, 32), faceMat);
    face.position.set(0, 0.72, 0.35);
    daruma.add(face);

    // Crane Eyebrows & Turtle Mustache (Inked)
    const blackInkMat = new THREE.MeshBasicMaterial({ color: 0x09090b });
    [-0.09, 0.09].forEach(ex => {
        const brow = new THREE.Mesh(new THREE.BoxGeometry(0.1, 0.03, 0.01), blackInkMat);
        brow.position.set(ex, 0.82, 0.36);
        brow.rotation.z = ex > 0 ? -0.22 : 0.22;
        daruma.add(brow);

        const eye = new THREE.Mesh(new THREE.CircleGeometry(0.045, 16), blackInkMat);
        eye.position.set(ex, 0.73, 0.36);
        daruma.add(eye);
    });

    // Gold Calligraphy Emblem ("必勝" - Hisshō / Victory & "福" - Fuku)
    const goldMat = new THREE.MeshStandardMaterial({
        color: 0xf59e0b,
        roughness: 0.2,
        metalness: 0.75
    });
    const kanjiBadge = new THREE.Mesh(new THREE.CircleGeometry(0.12, 16), goldMat);
    kanjiBadge.position.set(0, 0.48, 0.38);
    daruma.add(kanjiBadge);

    scene.add(daruma);
    models.daruma = daruma;
}

// ==========================================
// GLOSSY PORCELAIN MANEKI-NEKO (招き猫)
// ==========================================
function buildManekiNeko() {
    const neko = new THREE.Group();
    neko.name = 'neko';
    neko.position.set(1.8, 0, 1.6);

    // Stone Pedestal
    const altar = new THREE.Mesh(new THREE.CylinderGeometry(0.45, 0.52, 0.42, 16), new THREE.MeshStandardMaterial({ color: 0x334155 }));
    altar.position.y = 0.21;
    altar.castShadow = true;
    neko.add(altar);

    // Porcelain Materials
    const porcelainMat = new THREE.MeshStandardMaterial({
        color: 0xffffff,
        roughness: 0.15,
        metalness: 0.05
    });
    const pinkMat = new THREE.MeshStandardMaterial({ color: 0xf472b6, roughness: 0.4 });
    const redMat = new THREE.MeshStandardMaterial({ color: 0xe11d48, roughness: 0.25 });
    const goldMat = new THREE.MeshStandardMaterial({ color: 0xf59e0b, roughness: 0.2, metalness: 0.8 });

    // Porcelain Body
    const body = new THREE.Mesh(new THREE.SphereGeometry(0.35, 32, 32), porcelainMat);
    body.position.y = 0.62;
    body.scale.set(0.92, 1.1, 0.92);
    body.castShadow = true;
    neko.add(body);

    // Cute Head
    const head = new THREE.Mesh(new THREE.SphereGeometry(0.28, 32, 32), porcelainMat);
    head.position.y = 0.95;
    head.castShadow = true;
    neko.add(head);

    // Pointed Ears with Pink Interior
    [-0.14, 0.14].forEach(ex => {
        const ear = new THREE.Mesh(new THREE.ConeGeometry(0.1, 0.18, 4), porcelainMat);
        ear.position.set(ex, 1.18, 0);
        ear.rotation.z = ex > 0 ? -0.2 : 0.2;
        neko.add(ear);

        const innerEar = new THREE.Mesh(new THREE.ConeGeometry(0.06, 0.12, 4), pinkMat);
        innerEar.position.set(ex, 1.18, 0.04);
        innerEar.rotation.z = ex > 0 ? -0.2 : 0.2;
        neko.add(innerEar);
    });

    // Crimson Collar & Golden Suzu Bell
    const collar = new THREE.Mesh(new THREE.TorusGeometry(0.22, 0.035, 12, 24), redMat);
    collar.position.set(0, 0.78, 0.05);
    collar.rotation.x = Math.PI / 2;
    neko.add(collar);

    const bell = new THREE.Mesh(new THREE.SphereGeometry(0.06, 16, 16), goldMat);
    bell.position.set(0, 0.74, 0.25);
    neko.add(bell);

    // Raised Right Paw (Beckoning Good Fortune)
    const arm = new THREE.Mesh(new THREE.CylinderGeometry(0.07, 0.09, 0.32, 16), porcelainMat);
    arm.position.set(0.26, 0.88, 0.18);
    arm.rotation.set(0.4, 0, -0.4);
    neko.add(arm);

    const paw = new THREE.Mesh(new THREE.SphereGeometry(0.08, 16, 16), porcelainMat);
    paw.position.set(0.32, 1.06, 0.26);
    neko.add(paw);

    // Golden Koban Coin ("千万両" - 10 Million Gold Ryo)
    const koban = new THREE.Mesh(new THREE.BoxGeometry(0.18, 0.26, 0.03), goldMat);
    koban.position.set(0, 0.52, 0.32);
    koban.rotation.x = -0.15;
    neko.add(koban);

    scene.add(neko);
    models.neko = neko;
}

// ==========================================
// DYNAMIC PARTICLES: SAKURA, WISTERIA & FIREFLIES
// ==========================================
function buildParticles() {
    // 1. Drifting Sakura Blossom Petals
    const sakuraCount = 450;
    sakuraGeo = new THREE.BufferGeometry();
    const sPos = new Float32Array(sakuraCount * 3);
    const sSpd = new Float32Array(sakuraCount * 3);

    for (let i = 0; i < sakuraCount; i++) {
        sPos[i * 3] = (Math.random() - 0.5) * 20;
        sPos[i * 3 + 1] = Math.random() * 10 + 0.5;
        sPos[i * 3 + 2] = (Math.random() - 0.5) * 20;

        sSpd[i * 3] = (Math.random() - 0.5) * 0.025;
        sSpd[i * 3 + 1] = -(Math.random() * 0.02 + 0.012);
        sSpd[i * 3 + 2] = Math.random() * 0.02 + 0.008;
    }

    sakuraGeo.setAttribute('position', new THREE.BufferAttribute(sPos, 3));
    sakuraGeo.userData.speeds = sSpd;

    const sakuraTex = createPetalTexture('rgba(255, 192, 203, 1)', 'rgba(244, 114, 182, 0.8)');
    const sakuraMat = new THREE.PointsMaterial({
        size: 0.28,
        map: sakuraTex,
        transparent: true,
        depthWrite: false,
        blending: THREE.NormalBlending
    });

    sakuraParticles = new THREE.Points(sakuraGeo, sakuraMat);
    scene.add(sakuraParticles);
    models.sakura = sakuraParticles;

    // 2. Glowing Purple Wisteria Embers / Spirit Spores (Demon Slayer Mt. Fujikasane)
    const wisteriaCount = 350;
    wisteriaGeo = new THREE.BufferGeometry();
    const wPos = new Float32Array(wisteriaCount * 3);
    const wSpd = new Float32Array(wisteriaCount * 3);

    for (let i = 0; i < wisteriaCount; i++) {
        wPos[i * 3] = (Math.random() - 0.5) * 16;
        wPos[i * 3 + 1] = Math.random() * 7 + 0.2;
        wPos[i * 3 + 2] = (Math.random() - 0.5) * 16;

        // Upward floating vortex
        wSpd[i * 3] = (Math.random() - 0.5) * 0.015;
        wSpd[i * 3 + 1] = Math.random() * 0.018 + 0.008; // Float UP
        wSpd[i * 3 + 2] = (Math.random() - 0.5) * 0.015;
    }

    wisteriaGeo.setAttribute('position', new THREE.BufferAttribute(wPos, 3));
    wisteriaGeo.userData.speeds = wSpd;

    const wisteriaTex = createRadialGlowTexture('rgba(216, 180, 254, 1)', 'rgba(147, 51, 234, 0)');
    const wisteriaMat = new THREE.PointsMaterial({
        size: 0.32,
        map: wisteriaTex,
        transparent: true,
        depthWrite: false,
        blending: THREE.AdditiveBlending
    });

    wisteriaParticles = new THREE.Points(wisteriaGeo, wisteriaMat);
    scene.add(wisteriaParticles);

    // 3. Warm Fireflies dancing near the lanterns
    const fireflyCount = 60;
    fireflyGeo = new THREE.BufferGeometry();
    const fPos = new Float32Array(fireflyCount * 3);
    const fSpd = new Float32Array(fireflyCount * 3);

    for (let i = 0; i < fireflyCount; i++) {
        fPos[i * 3] = (Math.random() - 0.5) * 10;
        fPos[i * 3 + 1] = Math.random() * 3.5 + 0.4;
        fPos[i * 3 + 2] = (Math.random() - 0.5) * 8 + 1.0;

        fSpd[i * 3] = (Math.random() - 0.5) * 0.012;
        fSpd[i * 3 + 1] = (Math.random() - 0.5) * 0.008;
        fSpd[i * 3 + 2] = (Math.random() - 0.5) * 0.012;
    }

    fireflyGeo.setAttribute('position', new THREE.BufferAttribute(fPos, 3));
    fireflyGeo.userData.speeds = fSpd;

    const fireflyTex = createRadialGlowTexture('rgba(254, 240, 138, 1)', 'rgba(234, 179, 8, 0)');
    const fireflyMat = new THREE.PointsMaterial({
        size: 0.26,
        map: fireflyTex,
        transparent: true,
        depthWrite: false,
        blending: THREE.AdditiveBlending
    });

    fireflyParticles = new THREE.Points(fireflyGeo, fireflyMat);
    scene.add(fireflyParticles);
}

// ==========================================
// LIGHTING & NIGHT/DAWN MODE TOGGLE
// ==========================================
function updateLightingVisuals() {
    const btn = document.getElementById('btnNightMode');
    if (isNight) {
        // Deep Kimetsu Wisteria Midnight
        scene.background.set(0x070512);
        scene.fog.color.set(0x0e071e);
        ambientLight.color.set(0x28124d);
        ambientLight.intensity = 0.85;

        dirLight.color.set(0x93c5fd);
        dirLight.intensity = 0.75;
        moonRimLight.color.set(0xa855f7);
        moonRimLight.intensity = 0.95;

        lanternPointLights.forEach(item => item.light.intensity = item.baseIntensity);
        wisteriaGlowLights.forEach(light => light.intensity = 2.2);

        if (moonMesh) moonMesh.material.opacity = 0.98;
        if (godRaysGroup) godRaysGroup.visible = true;

        if (btn) {
            btn.innerHTML = `<span class="dock-btn-icon">🌙</span><span class="dock-btn-label">Không Gian: Đêm Tử Đằng</span>`;
            btn.classList.add('active');
        }
    } else {
        // Sacred Dawn / Sunrise (Bình minh Akebono)
        scene.background.set(0x201235);
        scene.fog.color.set(0x351b47);
        ambientLight.color.set(0x6b21a8);
        ambientLight.intensity = 1.35;

        dirLight.color.set(0xfde047);
        dirLight.intensity = 1.5;
        moonRimLight.color.set(0xf43f5e);
        moonRimLight.intensity = 1.2;

        lanternPointLights.forEach(item => item.light.intensity = 0.6);
        wisteriaGlowLights.forEach(light => light.intensity = 1.0);

        if (godRaysGroup) godRaysGroup.visible = false;

        if (btn) {
            btn.innerHTML = `<span class="dock-btn-icon">☀️</span><span class="dock-btn-label">Không Gian: Bình Minh Rạng Rỡ</span>`;
            btn.classList.remove('active');
        }
    }
}

// ==========================================
// PROCEDURAL SHINTO TEMPLE BELL / CHIME (WEB AUDIO API)
// ==========================================
function playTempleChimeSound() {
    if (!soundChimeEnabled) return;
    try {
        const AudioContextClass = window.AudioContext || window.webkitAudioContext;
        if (!AudioContextClass) return;
        if (!audioCtx) audioCtx = new AudioContextClass();
        if (audioCtx.state === 'suspended') audioCtx.resume();

        const now = audioCtx.currentTime;
        // Two resonant crystal sine harmonics simulating Shinto Suzu Bell
        const freqs = [880, 1760, 2640];
        freqs.forEach((freq, idx) => {
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();

            osc.type = idx === 0 ? 'sine' : 'triangle';
            osc.frequency.setValueAtTime(freq, now);

            const initialGain = idx === 0 ? 0.18 : 0.08 / idx;
            gain.gain.setValueAtTime(initialGain, now);
            gain.gain.exponentialRampToValueAtTime(0.0001, now + 1.8);

            osc.connect(gain);
            gain.connect(audioCtx.destination);

            osc.start(now);
            osc.stop(now + 1.85);
        });
    } catch (e) {
        // Audio error silent fallback
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
// INTERACTIVE RAYCASTING & HOTSPOTS
// ==========================================
function onCanvasClick(e) {
    mouse.x = (e.clientX / window.innerWidth) * 2 - 1;
    mouse.y = -(e.clientY / window.innerHeight) * 2 + 1;

    raycaster.setFromCamera(mouse, camera);
    const hits = raycaster.intersectObjects(scene.children, true);

    if (hits.length > 0) {
        let obj = hits[0].object;
        let foundKey = null;

        while (obj && obj !== scene) {
            if (obj.name && VOCAB_DATABASE[obj.name]) {
                foundKey = obj.name;
                break;
            }
            obj = obj.parent;
        }

        if (foundKey) {
            focusObject(foundKey);
        }
    }
}

function onUserInteraction() {
    // If user manually rotates or zooms with mouse/touch, pause cinematic roam
    if (isCinematic) {
        setCinematicMode(false);
    }
}

function focusObject(key) {
    const data = VOCAB_DATABASE[key];
    if (!data) return;

    currentActiveItem = data;
    currentVocabIndex = VOCAB_KEYS.indexOf(key);

    // Turn off cinematic roam when inspecting a specific object
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

    // Set Smooth Camera Glide Target
    targetCamPos.copy(data.camPos);
    targetLookAt.copy(data.lookAt);

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
    targetCamPos.set(0, 3.4, 9.8);
    targetLookAt.set(0, 2.0, 0);
    controls.autoRotate = autoRotate;
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

    // 1. Cinematic Drone Roam Mode or Smooth Lerp
    if (isCinematic) {
        cinematicAngle += 0.22 * delta;
        const camX = Math.sin(cinematicAngle) * cinematicRadius;
        const camZ = Math.cos(cinematicAngle) * cinematicRadius;
        const camY = cinematicHeight + Math.sin(cinematicAngle * 1.5) * 0.8;

        targetCamPos.set(camX, camY, camZ);
        targetLookAt.set(0, 2.0, 0);
    }

    camera.position.lerp(targetCamPos, 0.045);
    controls.target.lerp(targetLookAt, 0.045);

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
        models.wisteriaClusters.forEach((cluster, idx) => {
            cluster.rotation.z = Math.sin(elapsedTime * 1.8 + idx * 0.4) * 0.06;
            cluster.rotation.x = Math.cos(elapsedTime * 1.6 + idx * 0.3) * 0.05;
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
                pos[i * 3 + 1] = 10.0;
                pos[i * 3] = (Math.random() - 0.5) * 20;
                pos[i * 3 + 2] = (Math.random() - 0.5) * 20;
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

    controls.update();
    renderer.render(scene, camera);
}

// Start application when DOM is ready
window.addEventListener('DOMContentLoaded', init);
