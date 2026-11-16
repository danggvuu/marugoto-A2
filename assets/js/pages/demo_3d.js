/* ==========================================================================
   ⛩️ DEMO 3D - KIMETSU NO YAIBA MT. FUJIKASANE WISTERIA SHRINE
   High-Fidelity Stylized WebGL 3D Experience (Three.js r128)
   Senior Environment Art & Performance Optimization
   ========================================================================== */

let scene, camera, renderer, controls;
let isNight = true;
let autoRotate = false;
let particlesActive = true;
let isCinematic = false;
let soundChimeEnabled = true;

// Lights
let dirLight, ambientLight, moonRimLight, katanaSpotLight;
let lanternPointLights = [];
let wisteriaGlowLights = [];

// Particle Systems
let sakuraGeo, sakuraParticles;
let wisteriaGeo, wisteriaParticles;
let fireflyGeo, fireflyParticles;

// Moon Meshes & Environment
let moonMesh, moonHaloMesh;

// Model Object References & Raycasting
const models = {};
const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();

// Camera Smooth Glide Transition State
let isTransitioning = false;
let transitionStartTime = 0;
let transitionDuration = 950; // ms
const transitionStartCam = new THREE.Vector3();
const transitionStartTarget = new THREE.Vector3();
const transitionEndCam = new THREE.Vector3();
const transitionEndTarget = new THREE.Vector3();

// Cinematic Camera Roam parameters
let cinematicAngle = 0;
const cinematicRadius = 14.2;
const cinematicHeight = 4.2;

// Audio Context for Procedural Shinto Temple Bell / Chime
let audioCtx = null;

// Clock for Delta Time & Animations
const clock = new THREE.Clock();
let isTabActive = true;

// Wisteria Instanced Mesh Reference
let wisteriaInstancedMesh = null;
let wisteriaInstanceCount = 0;
let wisteriaClustersData = [];

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
        meaning: 'Cổng Thần đạo truyền thống sơn đỏ chu sa trầm mặc, phân định ranh giới giữa cõi trần và chốn thần linh.',
        culture: '⛩️ Trong anime Kimetsu no Yaiba, cổng Torii sừng sững tại lối vào Đỉnh Núi Tử Đằng (藤襲山 - Fujikasane). Nơi đây treo dây thừng thiêng Shimenawa bện rơm và giấy trắng Shide, là điểm khởi đầu cho kỳ Tuyển Chọn Cuối Cùng (最終選別 - Saishū Senbetsu).',
        camPos: new THREE.Vector3(0, 3.4, 9.8),
        lookAt: new THREE.Vector3(0, 3.2, 0)
    },
    katana: {
        key: 'katana',
        tag: 'Bảo kiếm Diệt Quỷ • Sát Quỷ Đội',
        kanji: '日輪刀',
        romaji: 'Nichirin-tō',
        kana: 'にちりんとう (Nichirin-tō)',
        meaning: 'Thanh kiếm Nichirin rèn từ Cát sắt đỏ và Quặng đỏ thẫm hấp thụ ánh sáng mặt trời vĩnh cửu.',
        culture: '⚔️ Vũ khí tối thượng của các kiếm sĩ Sát Quỷ Đội (鬼殺隊). Lưỡi kiếm rèn thủ công cong vút uyển chuyển với vân Hamon sắc lẹm, tsuba rực lửa, chuôi kiếm quấn lụa quả trám và bao kiếm sơn mài đen tuyền đặt trang trọng trên giá Katanakake.',
        camPos: new THREE.Vector3(1.3, 1.45, 2.9),
        lookAt: new THREE.Vector3(2.3, 0.92, 1.2)
    },
    wisteria: {
        key: 'wisteria',
        tag: 'Thần Mộc Xua Quỷ • Kimetsu no Yaiba',
        kanji: '藤の花',
        romaji: 'Fuji no hana',
        kana: 'ふじのはな (Fuji no hana)',
        meaning: 'Hoa Tử Đằng linh thiêng với những chùm hoa tím oải hương buông rủ như thác nước huyền ảo.',
        culture: '🪻 Loài hoa nở rộ bốn mùa trên đỉnh núi Fujikasane. Hương thơm và độc tố của hoa Tử Đằng là khắc tinh số một khiến loài quỷ khiếp sợ và không bao giờ dám đến gần, tạo thành kết giới thiêng liêng bảo vệ loài người.',
        camPos: new THREE.Vector3(-2.6, 3.6, 4.4),
        lookAt: new THREE.Vector3(-3.6, 3.5, 1.5)
    },
    lantern: {
        key: 'lantern',
        tag: 'Dẫn Lối Thần Đạo • Cổ Kính',
        kanji: '燈籠',
        romaji: 'Tōrō',
        kana: 'とうろう (Tōrō)',
        meaning: 'Đèn lồng đá Kasuga cổ kính chạm khắc tinh xảo, thắp sáng ngọn lửa ấm áp giữa đêm sương.',
        culture: '🏮 Được đặt dọc hai bên lối vào đền thờ (Sandō). Ngọn lửa thiêng bập bùng bên trong mang ý nghĩa xua tan bóng tối u ám, soi tỏ tâm hồn thanh tịnh và dẫn bước lữ khách trên con đường hướng thiện.',
        camPos: new THREE.Vector3(-1.7, 2.0, 3.7),
        lookAt: new THREE.Vector3(-2.6, 1.6, 2.2)
    },
    fuji: {
        key: 'fuji',
        tag: 'Linh Sơn Hùng Vĩ • Di Sản Thế Giới',
        kanji: '富士山',
        romaji: 'Fuji-san',
        kana: 'ふじさん (Fuji-san)',
        meaning: 'Núi Phú Sĩ tuyết phủ ngàn năm cùng ánh trăng rằm vằng vặc (満月 - Mangetsu).',
        culture: '🗻 Đỉnh núi linh thiêng cao 3.776m, biểu tượng trường tồn bất diệt của đất nước Mặt Trời Mọc. Đỉnh núi tuyết sừng sững uy nghi phía sau cổng Torii dưới ánh trăng rằm huyền ảo.',
        camPos: new THREE.Vector3(0, 4.0, 15.0),
        lookAt: new THREE.Vector3(0, 6.2, -40)
    },
    daruma: {
        key: 'daruma',
        tag: 'Búp Bê Ý Chí & Ước Nguyện',
        kanji: 'だるま',
        romaji: 'Daruma',
        kana: 'だるま (Daruma)',
        meaning: 'Búp bê tròn đỏ truyền thống tượng trưng cho tinh thần bất khuất "Thất ngã bát khởi" (Ngã 7 lần, đứng dậy 8 lần).',
        culture: '🎎 Khắc chữ vàng "Phúc" (福) và nét mày hạc râu rùa biểu trưng trường thọ. Người Nhật khi lập chí lớn sẽ điểm nhãn mắt trái; khi vượt qua thử thách vẻ vang sẽ vẽ nốt mắt phải để tạ ơn thần linh.',
        camPos: new THREE.Vector3(-1.4, 1.15, 3.2),
        lookAt: new THREE.Vector3(-1.4, 0.85, 1.8)
    },
    neko: {
        key: 'neko',
        tag: 'Phong Thủy Cầu May • Tài Lộc',
        kanji: '招き猫',
        romaji: 'Maneki-neko',
        kana: 'まねきねこ (Maneki-neko)',
        meaning: 'Mèo may mắn sứ trắng vẫy tay đón tài lộc, mang lục lạc vàng và đồng tiền cổ Koban.',
        culture: '🐱 Tay phải giơ cao vẫy gọi phúc lành, tiền cổ ghi khắc "Thiên vạn lượng" (千万両 - Senmanryō). Thường được bày trang trọng tại cổng vào cửa hàng, mang lại sự ấm no và bình an cho gia chủ.',
        camPos: new THREE.Vector3(-1.3, 1.1, 3.1),
        lookAt: new THREE.Vector3(-2.2, 0.85, 1.8)
    },
    sakura: {
        key: 'sakura',
        tag: 'Quốc Hoa • Vẻ Đẹp Khoảnh Khắc',
        kanji: '桜の花びら',
        romaji: 'Sakura no hanabira',
        kana: 'さくら の はなびら (Sakura)',
        meaning: 'Những cánh hoa anh đào thanh khiết chao liệng trong làn gió đêm huyền ảo.',
        culture: '🌸 Triết lý "Mono no aware" (U hoài trước vẻ đẹp phù du) - trân quý từng phút giây hiện tại. Sắc hồng hoa anh đào hòa quyện cùng sắc tím hoa Tử Đằng tạo nên bức tranh thiên nhiên tuyệt mỹ.',
        camPos: new THREE.Vector3(0, 3.8, 14.5),
        lookAt: new THREE.Vector3(0, 3.0, 0)
    }
};

let currentActiveItem = VOCAB_DATABASE.torii;

// ==========================================================================
// INITIALIZATION
// ==========================================================================
function init() {
    const canvas = document.getElementById('canvas3d');

    if (!window.WebGLRenderingContext) {
        showWebGLFallback();
        return;
    }

    // 1. Scene & Atmosphere (Mystical Indigo & Wisteria Night)
    scene = new THREE.Scene();
    scene.background = new THREE.Color(0x0a0718);
    scene.fog = new THREE.FogExp2(0x0e0a24, 0.0125);

    // 2. Camera Setup (Aspect-Adaptive Establishing View)
    const aspect = window.innerWidth / window.innerHeight;
    camera = new THREE.PerspectiveCamera(45, aspect, 0.1, 280);
    applyDefaultCameraPose();

    // 3. Renderer with sRGB Encoding & Soft PCF Shadows
    try {
        renderer = new THREE.WebGLRenderer({
            canvas,
            antialias: true,
            powerPreference: 'high-performance',
            stencil: false
        });
    } catch (e) {
        showWebGLFallback();
        return;
    }

    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    renderer.outputEncoding = THREE.sRGBEncoding;
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.0;

    // 4. Orbit Controls (Smooth, Bounded Safely Above Ground)
    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.06;
    controls.minDistance = 2.0;
    controls.maxDistance = 48.0;
    controls.minPolarAngle = 0.1;
    controls.maxPolarAngle = Math.PI / 2 - 0.05; // Prevent camera from clipping through floor
    controls.target.set(0, 3.0, 0);
    controls.autoRotate = false;
    controls.autoRotateSpeed = 0.7;

    // Manual interaction cancels active camera transitions
    controls.addEventListener('start', () => {
        isTransitioning = false;
        if (isCinematic) setCinematicMode(false);
    });

    // 5. Lighting Setup
    setupLighting();

    // 6. Build Scene Geometry
    buildStarfield();
    buildFullMoonAndAtmosphere();
    buildMajesticMountFuji();
    buildShrineGroundAndSteps();
    buildGrandToriiGate();
    buildWeepingWisteriaForest();
    buildNichirinKatanaMasterpiece();
    buildKasugaStoneLanterns();
    buildDarumaDoll();
    buildManekiNeko();
    buildDualParticleSystems();

    // 7. Event Handlers & Page Visibility
    window.addEventListener('resize', onWindowResize);
    canvas.addEventListener('click', onCanvasClick);
    document.addEventListener('visibilitychange', () => {
        isTabActive = !document.hidden;
        if (isTabActive) clock.start();
    });

    // Initial Display
    updateLightingVisuals();
    updateCinematicUI();
    syncAutoRotateUI();

    const urlParams = new URLSearchParams(window.location.search);
    const initialFocus = urlParams.get('focus');
    if (initialFocus && VOCAB_DATABASE[initialFocus]) {
        focusObject(initialFocus);
    } else {
        closeModal();
    }

    // Start Main Render Loop
    requestAnimationFrame(animate);
}

function showWebGLFallback() {
    const canvas = document.getElementById('canvas3d');
    if (canvas && canvas.parentElement) {
        const fallback = document.createElement('div');
        fallback.className = 'webgl-fallback-banner';
        fallback.innerHTML = `
            <div class="fallback-card">
                <h2>⛩️ Trình duyệt chưa kích hoạt WebGL</h2>
                <p>Thiết bị hoặc trình duyệt của bạn đang tắt tính năng tăng tốc phần cứng WebGL. Vui lòng bật WebGL trong cài đặt trình duyệt để thưởng thức không gian 3D.</p>
                <a href="index.html" class="fallback-btn">Quay Lại Trang Chủ</a>
            </div>
        `;
        canvas.parentElement.appendChild(fallback);
    }
}

function applyDefaultCameraPose() {
    const aspect = window.innerWidth / window.innerHeight;
    if (aspect < 1.0) {
        // Mobile portrait: step back so both Torii columns and Fuji summit breathe comfortably
        camera.position.set(0, 3.8, 19.5);
        if (controls) controls.target.set(0, 3.0, 0);
    } else {
        // Desktop / Landscape: grand balanced composition
        camera.position.set(0, 3.8, 14.5);
        if (controls) controls.target.set(0, 3.0, 0);
    }
}

// ==========================================================================
// LIGHTING SETUP (Atmospheric Indigo & Warm Amber Candlelight)
// ==========================================================================
function setupLighting() {
    // Ambient light: mystical deep indigo
    ambientLight = new THREE.AmbientLight(0x1a153b, 1.05);
    scene.add(ambientLight);

    // Main Silvery Moonbeam casting soft shadows
    dirLight = new THREE.DirectionalLight(0xb4c6fc, 0.95);
    dirLight.position.set(10, 24, 12);
    dirLight.castShadow = true;
    dirLight.shadow.mapSize.width = 2048;
    dirLight.shadow.mapSize.height = 2048;
    dirLight.shadow.camera.near = 0.5;
    dirLight.shadow.camera.far = 70;
    dirLight.shadow.camera.left = -16;
    dirLight.shadow.camera.right = 16;
    dirLight.shadow.camera.top = 16;
    dirLight.shadow.camera.bottom = -16;
    dirLight.shadow.bias = -0.0004;
    scene.add(dirLight);

    // Soft Lavender-Violet Rim Light from behind mountain
    moonRimLight = new THREE.DirectionalLight(0x8b5cf6, 0.45);
    moonRimLight.position.set(0, 16, -38);
    scene.add(moonRimLight);

    // Warm Altar Spotlight for Nichirin Katana
    katanaSpotLight = new THREE.SpotLight(0xfef08a, 1.5, 8.5, Math.PI / 4.2, 0.4);
    katanaSpotLight.position.set(2.4, 3.4, 2.6);
    katanaSpotLight.target.position.set(2.3, 0.9, 1.2);
    katanaSpotLight.castShadow = true;
    scene.add(katanaSpotLight);
    scene.add(katanaSpotLight.target);
}

// ==========================================================================
// PROCEDURAL HIGH-FIDELITY TEXTURE GENERATORS
// ==========================================================================
function createMoonTexture() {
    const canvas = document.createElement('canvas');
    canvas.width = 512;
    canvas.height = 512;
    const ctx = canvas.getContext('2d');

    const grad = ctx.createRadialGradient(256, 256, 10, 256, 256, 256);
    grad.addColorStop(0, '#ffffff');
    grad.addColorStop(0.65, '#f5f3ff');
    grad.addColorStop(0.88, '#e0e7ff');
    grad.addColorStop(1, '#c7d2fe');
    ctx.fillStyle = grad;
    ctx.beginPath();
    ctx.arc(256, 256, 256, 0, Math.PI * 2);
    ctx.fill();

    // Lunar Maria (Soft basaltic plains)
    ctx.fillStyle = 'rgba(165, 180, 252, 0.22)';
    const maria = [
        { x: 190, y: 170, r: 65 },
        { x: 240, y: 230, r: 85 },
        { x: 330, y: 180, r: 55 },
        { x: 310, y: 300, r: 75 },
        { x: 200, y: 330, r: 50 },
        { x: 360, y: 260, r: 40 }
    ];
    maria.forEach(m => {
        ctx.beginPath();
        ctx.arc(m.x, m.y, m.r, 0, Math.PI * 2);
        ctx.fill();
    });

    const tex = new THREE.CanvasTexture(canvas);
    tex.wrapS = THREE.ClampToEdgeWrapping;
    tex.wrapT = THREE.ClampToEdgeWrapping;
    return tex;
}

function createRadialGlowTexture(innerColor, outerColor) {
    const canvas = document.createElement('canvas');
    canvas.width = 256;
    canvas.height = 256;
    const ctx = canvas.getContext('2d');

    const grad = ctx.createRadialGradient(128, 128, 0, 128, 128, 128);
    grad.addColorStop(0, innerColor);
    grad.addColorStop(0.4, innerColor.replace(/[\d\.]+\)$/, '0.35)'));
    grad.addColorStop(0.8, innerColor.replace(/[\d\.]+\)$/, '0.08)'));
    grad.addColorStop(1, outerColor);
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 256, 256);

    return new THREE.CanvasTexture(canvas);
}

function createPetalTexture(colorHex1, colorHex2) {
    const canvas = document.createElement('canvas');
    canvas.width = 64;
    canvas.height = 64;
    const ctx = canvas.getContext('2d');

    ctx.translate(32, 32);
    const grad = ctx.createRadialGradient(0, -6, 2, 0, 0, 28);
    grad.addColorStop(0, colorHex1);
    grad.addColorStop(0.7, colorHex2);
    grad.addColorStop(1, 'rgba(0,0,0,0)');

    ctx.fillStyle = grad;
    ctx.beginPath();
    ctx.ellipse(0, 0, 12, 24, Math.PI / 8, 0, Math.PI * 2);
    ctx.fill();

    return new THREE.CanvasTexture(canvas);
}

function createFujiTexture() {
    const canvas = document.createElement('canvas');
    canvas.width = 512;
    canvas.height = 512;
    const ctx = canvas.getContext('2d');

    // Base obsidian basalt dark slope gradient (Y=0 bottom, Y=512 top)
    const baseGrad = ctx.createLinearGradient(0, 512, 0, 0);
    baseGrad.addColorStop(0, '#0c091f');
    baseGrad.addColorStop(0.45, '#16122e');
    baseGrad.addColorStop(0.65, '#241c45');
    baseGrad.addColorStop(0.85, '#e0e7ff');
    baseGrad.addColorStop(1.0, '#ffffff');
    ctx.fillStyle = baseGrad;
    ctx.fillRect(0, 0, 512, 512);

    // Realistic jagged snow tongues (Yukikei) streaming down along the slope
    ctx.fillStyle = '#f8fafc';
    for (let x = 0; x < 512; x += 16) {
        const tongueLength = 120 + Math.sin(x * 0.08) * 45 + Math.cos(x * 0.17) * 25;
        const startY = 160;
        ctx.beginPath();
        ctx.moveTo(x - 8, 0);
        ctx.lineTo(x + 24, 0);
        ctx.lineTo(x + 8, startY + tongueLength);
        ctx.lineTo(x, startY + tongueLength * 0.7);
        ctx.closePath();
        ctx.fill();
    }

    ctx.fillStyle = 'rgba(255, 255, 255, 0.15)';
    ctx.fillRect(0, 0, 512, 220);

    const tex = new THREE.CanvasTexture(canvas);
    tex.wrapS = THREE.RepeatWrapping;
    tex.wrapT = THREE.ClampToEdgeWrapping;
    return tex;
}

function createToriiPlaqueTexture() {
    const canvas = document.createElement('canvas');
    canvas.width = 256;
    canvas.height = 384;
    const ctx = canvas.getContext('2d');

    ctx.fillStyle = '#0a0d14';
    ctx.fillRect(0, 0, 256, 384);

    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 10;
    ctx.strokeRect(10, 10, 236, 364);

    ctx.strokeStyle = '#d97706';
    ctx.lineWidth = 3;
    ctx.strokeRect(20, 20, 216, 344);

    ctx.fillStyle = '#fbbf24';
    ctx.shadowColor = '#d97706';
    ctx.shadowBlur = 8;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.font = '900 68px "Shippori Mincho", "Noto Sans JP", serif';

    ctx.fillText('藤', 128, 90);
    ctx.fillText('襲', 128, 192);
    ctx.fillText('山', 128, 294);

    return new THREE.CanvasTexture(canvas);
}

function createDarumaTexture() {
    const canvas = document.createElement('canvas');
    canvas.width = 512;
    canvas.height = 512;
    const ctx = canvas.getContext('2d');

    // Crimson red lacquer background
    ctx.fillStyle = '#b91c1c';
    ctx.fillRect(0, 0, 512, 512);

    // White porcelain face area on front center (X: 128 to 384)
    ctx.fillStyle = '#fef3c7';
    ctx.beginPath();
    ctx.ellipse(256, 210, 150, 130, 0, 0, Math.PI * 2);
    ctx.fill();

    // Crane eyebrows (Tsuru)
    ctx.strokeStyle = '#0f172a';
    ctx.lineWidth = 14;
    ctx.lineCap = 'round';

    ctx.beginPath();
    ctx.moveTo(150, 175);
    ctx.quadraticCurveTo(195, 135, 235, 175);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(362, 175);
    ctx.quadraticCurveTo(317, 135, 277, 175);
    ctx.stroke();

    // Turtle mustache (Kame)
    ctx.lineWidth = 12;
    ctx.beginPath();
    ctx.moveTo(170, 255);
    ctx.quadraticCurveTo(256, 295, 342, 255);
    ctx.stroke();

    // Resolute Eyes with gold reflection ring
    ctx.fillStyle = '#0f172a';
    ctx.beginPath();
    ctx.arc(200, 205, 26, 0, Math.PI * 2);
    ctx.arc(312, 205, 26, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = '#ffffff';
    ctx.beginPath();
    ctx.arc(192, 198, 8, 0, Math.PI * 2);
    ctx.arc(304, 198, 8, 0, Math.PI * 2);
    ctx.fill();

    // Golden "福" on belly
    ctx.fillStyle = '#fbbf24';
    ctx.shadowColor = '#d97706';
    ctx.shadowBlur = 6;
    ctx.font = '900 85px "Shippori Mincho", "Noto Sans JP", serif';
    ctx.textAlign = 'center';
    ctx.fillText('福', 256, 420);

    return new THREE.CanvasTexture(canvas);
}

function createManekiNekoTexture() {
    const canvas = document.createElement('canvas');
    canvas.width = 512;
    canvas.height = 512;
    const ctx = canvas.getContext('2d');

    // Glossy White Porcelain Base
    ctx.fillStyle = '#f8fafc';
    ctx.fillRect(0, 0, 512, 512);

    // Calico Patches on head
    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.ellipse(150, 130, 65, 45, -0.3, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = '#ea580c';
    ctx.beginPath();
    ctx.ellipse(360, 140, 55, 40, 0.4, 0, Math.PI * 2);
    ctx.fill();

    // Happy smiling eyes
    ctx.strokeStyle = '#0f172a';
    ctx.lineWidth = 10;
    ctx.lineCap = 'round';

    ctx.beginPath();
    ctx.arc(195, 230, 22, Math.PI * 1.15, Math.PI * 1.85);
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(317, 230, 22, Math.PI * 1.15, Math.PI * 1.85);
    ctx.stroke();

    // Pink nose and mouth
    ctx.fillStyle = '#fb7185';
    ctx.beginPath();
    ctx.ellipse(256, 254, 9, 7, 0, 0, Math.PI * 2);
    ctx.fill();

    ctx.strokeStyle = '#fb7185';
    ctx.lineWidth = 5;
    ctx.beginPath();
    ctx.moveTo(256, 261);
    ctx.lineTo(256, 274);
    ctx.quadraticCurveTo(240, 288, 226, 278);
    ctx.moveTo(256, 274);
    ctx.quadraticCurveTo(272, 288, 286, 278);
    ctx.stroke();

    // Whiskers
    ctx.strokeStyle = '#334155';
    ctx.lineWidth = 4;
    [-14, 0, 14].forEach(dy => {
        ctx.beginPath();
        ctx.moveTo(135, 255 + dy);
        ctx.lineTo(75, 250 + dy * 1.3);
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(377, 255 + dy);
        ctx.lineTo(437, 250 + dy * 1.3);
        ctx.stroke();
    });

    return new THREE.CanvasTexture(canvas);
}

function createKobanTexture() {
    const canvas = document.createElement('canvas');
    canvas.width = 160;
    canvas.height = 280;
    const ctx = canvas.getContext('2d');

    ctx.fillStyle = '#f59e0b';
    ctx.fillRect(0, 0, 160, 280);

    ctx.strokeStyle = '#b45309';
    ctx.lineWidth = 8;
    ctx.strokeRect(6, 6, 148, 268);

    ctx.lineWidth = 3;
    for (let y = 30; y < 260; y += 18) {
        ctx.beginPath();
        ctx.moveTo(15, y);
        ctx.lineTo(145, y);
        ctx.stroke();
    }

    ctx.fillStyle = '#78350f';
    ctx.font = '900 46px "Shippori Mincho", "Noto Sans JP", serif';
    ctx.textAlign = 'center';
    ctx.fillText('千', 80, 80);
    ctx.fillText('万', 80, 148);
    ctx.fillText('両', 80, 216);

    return new THREE.CanvasTexture(canvas);
}

function createHamonTexture() {
    const canvas = document.createElement('canvas');
    canvas.width = 512;
    canvas.height = 64;
    const ctx = canvas.getContext('2d');

    ctx.fillStyle = '#e2e8f0';
    ctx.fillRect(0, 0, 512, 64);

    ctx.fillStyle = '#ffffff';
    ctx.beginPath();
    ctx.moveTo(0, 64);
    for (let x = 0; x <= 512; x += 16) {
        const wave = 28 + Math.sin(x * 0.12) * 8 + Math.cos(x * 0.25) * 5;
        ctx.lineTo(x, wave);
    }
    ctx.lineTo(512, 64);
    ctx.closePath();
    ctx.fill();

    const tex = new THREE.CanvasTexture(canvas);
    tex.wrapS = THREE.RepeatWrapping;
    tex.wrapT = THREE.ClampToEdgeWrapping;
    return tex;
}

function createStoneTexture() {
    const canvas = document.createElement('canvas');
    canvas.width = 256;
    canvas.height = 256;
    const ctx = canvas.getContext('2d');

    ctx.fillStyle = '#475569';
    ctx.fillRect(0, 0, 256, 256);

    for (let i = 0; i < 1800; i++) {
        const x = Math.random() * 256;
        const y = Math.random() * 256;
        const r = Math.random() * 2 + 0.5;
        const isDark = Math.random() > 0.5;
        ctx.fillStyle = isDark ? '#1e293b' : '#94a3b8';
        ctx.beginPath();
        ctx.arc(x, y, r, 0, Math.PI * 2);
        ctx.fill();
    }

    const tex = new THREE.CanvasTexture(canvas);
    tex.wrapS = THREE.RepeatWrapping;
    tex.wrapT = THREE.RepeatWrapping;
    return tex;
}

function createBarkTexture() {
    const canvas = document.createElement('canvas');
    canvas.width = 256;
    canvas.height = 512;
    const ctx = canvas.getContext('2d');

    ctx.fillStyle = '#261b17';
    ctx.fillRect(0, 0, 256, 512);

    ctx.strokeStyle = '#18100d';
    ctx.lineWidth = 4;
    for (let x = 0; x < 256; x += 12) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        for (let y = 0; y < 512; y += 40) {
            const shift = Math.sin((y + x) * 0.04) * 8;
            ctx.lineTo(x + shift, y);
        }
        ctx.stroke();
    }

    const tex = new THREE.CanvasTexture(canvas);
    tex.wrapS = THREE.RepeatWrapping;
    tex.wrapT = THREE.RepeatWrapping;
    return tex;
}

function createShimenawaTexture() {
    const canvas = document.createElement('canvas');
    canvas.width = 256;
    canvas.height = 256;
    const ctx = canvas.getContext('2d');

    ctx.fillStyle = '#b45309';
    ctx.fillRect(0, 0, 256, 256);

    ctx.strokeStyle = '#d97706';
    ctx.lineWidth = 6;
    for (let y = 0; y < 256; y += 16) {
        ctx.beginPath();
        ctx.moveTo(0, y);
        for (let x = 0; x < 256; x += 32) {
            ctx.lineTo(x + 16, y + 8);
            ctx.lineTo(x + 32, y);
        }
        ctx.stroke();
    }

    const tex = new THREE.CanvasTexture(canvas);
    tex.wrapS = THREE.RepeatWrapping;
    tex.wrapT = THREE.RepeatWrapping;
    return tex;
}

// ==========================================================================
// SCENE & ATMOSPHERE BUILDERS
// ==========================================================================

// 1. Cosmic Starfield
function buildStarfield() {
    const starCount = 1200;
    const starGeo = new THREE.BufferGeometry();
    const starPos = new Float32Array(starCount * 3);
    const starColors = new Float32Array(starCount * 3);

    const colorA = new THREE.Color(0xa5b4fc);
    const colorB = new THREE.Color(0xfbcfe8);

    for (let i = 0; i < starCount; i++) {
        const theta = Math.random() * Math.PI * 2;
        const phi = Math.acos(Math.random() * 0.85 + 0.1);
        const radius = 130 + Math.random() * 40;

        starPos[i * 3] = radius * Math.sin(phi) * Math.sin(theta);
        starPos[i * 3 + 1] = radius * Math.cos(phi);
        starPos[i * 3 + 2] = radius * Math.sin(phi) * Math.cos(theta);

        const mixColor = colorA.clone().lerp(colorB, Math.random());
        starColors[i * 3] = mixColor.r;
        starColors[i * 3 + 1] = mixColor.g;
        starColors[i * 3 + 2] = mixColor.b;
    }

    starGeo.setAttribute('position', new THREE.BufferAttribute(starPos, 3));
    starGeo.setAttribute('color', new THREE.BufferAttribute(starColors, 3));

    const starMat = new THREE.PointsMaterial({
        size: 0.65,
        vertexColors: true,
        transparent: true,
        opacity: 0.85
    });

    const starfield = new THREE.Points(starGeo, starMat);
    scene.add(starfield);
    models.starfield = starfield;
}

// 2. Full Moon and Soft Atmosphere
function buildFullMoonAndAtmosphere() {
    const moonGroup = new THREE.Group();
    moonGroup.name = 'fuji';
    moonGroup.position.set(4.5, 20.0, -42);

    const moonTex = createMoonTexture();
    const moonGeo = new THREE.CircleGeometry(5.8, 64);
    const moonMat = new THREE.MeshBasicMaterial({
        map: moonTex,
        transparent: true,
        opacity: 0.98
    });
    moonMesh = new THREE.Mesh(moonGeo, moonMat);
    moonGroup.add(moonMesh);

    const haloTex = createRadialGlowTexture('rgba(224, 231, 255, 0.95)', 'rgba(168, 85, 247, 0)');
    const haloGeo = new THREE.PlaneGeometry(24, 24);
    const haloMat = new THREE.MeshBasicMaterial({
        map: haloTex,
        transparent: true,
        blending: THREE.AdditiveBlending,
        depthWrite: false,
        opacity: 0.65
    });
    moonHaloMesh = new THREE.Mesh(haloGeo, haloMat);
    moonHaloMesh.position.z = -0.15;
    moonGroup.add(moonHaloMesh);

    const outerHaloGeo = new THREE.PlaneGeometry(42, 42);
    const outerHaloMat = new THREE.MeshBasicMaterial({
        map: haloTex,
        transparent: true,
        blending: THREE.AdditiveBlending,
        depthWrite: false,
        opacity: 0.3,
        color: 0x8b5cf6
    });
    const outerHalo = new THREE.Mesh(outerHaloGeo, outerHaloMat);
    outerHalo.position.z = -0.25;
    moonGroup.add(outerHalo);

    scene.add(moonGroup);
    models.moon = moonGroup;
}

// 3. Majestic Mount Fuji (Continuous Stratovolcano Slope with Integrated Snow Texture)
function buildMajesticMountFuji() {
    const fujiGroup = new THREE.Group();
    fujiGroup.name = 'fuji';
    fujiGroup.position.set(0, 0.2, -45);

    const slices = 64;
    const stacks = 32;
    const totalHeight = 24.5;
    const baseRadius = 38.0;

    const positions = [];
    const uvs = [];
    const indices = [];

    for (let j = 0; j <= stacks; j++) {
        const v = j / stacks;
        const y = v * totalHeight;
        const radius = 3.6 + (baseRadius - 3.6) * Math.pow(1 - v, 1.88);

        for (let i = 0; i <= slices; i++) {
            const u = i / slices;
            const theta = u * Math.PI * 2;
            const x = radius * Math.sin(theta);
            const z = radius * Math.cos(theta);
            const ridge = Math.sin(theta * 12) * 0.35 * (1 - v);

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

    const fujiGeo = new THREE.BufferGeometry();
    fujiGeo.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
    fujiGeo.setAttribute('uv', new THREE.Float32BufferAttribute(uvs, 2));
    fujiGeo.setIndex(indices);
    fujiGeo.computeVertexNormals();

    const fujiTex = createFujiTexture();
    const fujiMat = new THREE.MeshStandardMaterial({
        map: fujiTex,
        roughness: 0.85,
        metalness: 0.08
    });

    const fujiBody = new THREE.Mesh(fujiGeo, fujiMat);
    fujiBody.receiveShadow = true;
    fujiGroup.add(fujiBody);

    const ridgeMat = new THREE.MeshBasicMaterial({ color: 0x090616 });
    const ridgePoints = [
        -55, 0, -48, 7.5, -40, 4.8, -32, 9.5, -24, 5.8, -16, 8.8, -8, 4.8,
        0, 6.8, 8, 4.8, 16, 8.8, 24, 5.8, 32, 9.5, 40, 4.8, 48, 7.5, 55, 0
    ];
    const shape = new THREE.Shape();
    shape.moveTo(-60, -2);
    for (let i = 0; i < ridgePoints.length; i += 2) {
        shape.lineTo(ridgePoints[i], ridgePoints[i + 1]);
    }
    shape.lineTo(60, -2);
    shape.closePath();
    const ridgeMesh = new THREE.Mesh(new THREE.ShapeGeometry(shape), ridgeMat);
    ridgeMesh.position.set(0, 0, -20);
    fujiGroup.add(ridgeMesh);

    scene.add(fujiGroup);
    models.fuji = fujiGroup;
}

// 4. Shrine Ground, Sando Path & Weathered Steps
function buildShrineGroundAndSteps() {
    const groundGroup = new THREE.Group();

    const plateauGeo = new THREE.CylinderGeometry(55, 58, 1.5, 64);
    const plateauMat = new THREE.MeshStandardMaterial({
        color: 0x0f0b1e,
        roughness: 0.95,
        metalness: 0.05
    });
    const plateau = new THREE.Mesh(plateauGeo, plateauMat);
    plateau.position.y = -0.75;
    plateau.receiveShadow = true;
    groundGroup.add(plateau);

    const stoneNoiseTex = createStoneTexture();
    const stoneBorderMat = new THREE.MeshStandardMaterial({
        color: 0x242a38,
        map: stoneNoiseTex,
        roughness: 0.9
    });
    const stoneTerrace = new THREE.Mesh(new THREE.CylinderGeometry(13.0, 13.5, 0.3, 64), stoneBorderMat);
    stoneTerrace.position.y = 0.10;
    stoneTerrace.receiveShadow = true;
    groundGroup.add(stoneTerrace);

    const pathMat = new THREE.MeshStandardMaterial({
        color: 0x333d4d,
        map: stoneNoiseTex,
        roughness: 0.78,
        metalness: 0.12
    });
    const path = new THREE.Mesh(new THREE.PlaneGeometry(2.8, 24), pathMat);
    path.rotation.x = -Math.PI / 2;
    path.position.set(0, 0.23, 1.0);
    path.receiveShadow = true;
    groundGroup.add(path);

    const pebbleMat = new THREE.MeshStandardMaterial({
        color: 0x64748b,
        map: stoneNoiseTex,
        roughness: 0.88
    });
    [-1.75, 1.75].forEach(x => {
        const pebbles = new THREE.Mesh(new THREE.PlaneGeometry(0.7, 24), pebbleMat);
        pebbles.rotation.x = -Math.PI / 2;
        pebbles.position.set(x, 0.225, 1.0);
        pebbles.receiveShadow = true;
        groundGroup.add(pebbles);
    });

    const stepMat = new THREE.MeshStandardMaterial({
        color: 0x2e3846,
        map: stoneNoiseTex,
        roughness: 0.85
    });
    for (let s = 0; s < 4; s++) {
        const step = new THREE.Mesh(new THREE.BoxGeometry(3.8 - s * 0.15, 0.12, 0.75), stepMat);
        step.position.set(0, 0.1 + s * 0.11, 4.4 - s * 0.72);
        step.receiveShadow = true;
        step.castShadow = true;
        groundGroup.add(step);
    }

    scene.add(groundGroup);
    models.ground = groundGroup;
}

// 5. Grand Torii Shrine Entrance (Authentic Myōjin Torii with Curvature & Inscriptions)
function buildGrandToriiGate() {
    const torii = new THREE.Group();
    torii.name = 'torii';

    const vermilionMat = new THREE.MeshStandardMaterial({
        color: 0xa8201a, // Sacred deep Vermilion Shu-iro
        roughness: 0.42,
        metalness: 0.08
    });
    const blackLacquerMat = new THREE.MeshStandardMaterial({
        color: 0x0f1117,
        roughness: 0.25,
        metalness: 0.35
    });
    const stoneNoiseTex = createStoneTexture();
    const stoneBaseMat = new THREE.MeshStandardMaterial({
        color: 0x475569,
        map: stoneNoiseTex,
        roughness: 0.9
    });
    const goldMat = new THREE.MeshStandardMaterial({
        color: 0xf59e0b,
        roughness: 0.28,
        metalness: 0.82
    });
    const shimenawaTex = createShimenawaTexture();
    const shimenawaStrawMat = new THREE.MeshStandardMaterial({
        color: 0xd97706,
        map: shimenawaTex,
        roughness: 0.95
    });
    const whiteShideMat = new THREE.MeshStandardMaterial({
        color: 0xf8fafc,
        roughness: 0.55,
        side: THREE.DoubleSide
    });

    const dist = 2.25;
    const height = 4.8;
    const radius = 0.25;

    // 1. Two Pillars (Hashira) with Entasis Taper & Stone Kamebara Plinths
    [-dist, dist].forEach(x => {
        const plinth = new THREE.Mesh(new THREE.CylinderGeometry(0.44, 0.52, 0.42, 24), stoneBaseMat);
        plinth.position.set(x, 0.31, 0);
        plinth.castShadow = true;
        torii.add(plinth);

        const collar = new THREE.Mesh(new THREE.CylinderGeometry(0.33, 0.33, 0.35, 24), blackLacquerMat);
        collar.position.set(x, 0.67, 0);
        torii.add(collar);

        const goldRing = new THREE.Mesh(new THREE.CylinderGeometry(0.34, 0.34, 0.05, 24), goldMat);
        goldRing.position.set(x, 0.86, 0);
        torii.add(goldRing);

        const pillar = new THREE.Mesh(new THREE.CylinderGeometry(radius * 0.9, radius, height, 32), vermilionMat);
        pillar.position.set(x, height / 2 + 0.55, 0);
        pillar.rotation.z = x > 0 ? 0.035 : -0.035;
        pillar.castShadow = true;
        torii.add(pillar);

        const wedge = new THREE.Mesh(new THREE.BoxGeometry(0.12, 0.36, 0.62), vermilionMat);
        wedge.position.set(x, 4.02, 0);
        torii.add(wedge);
    });

    // 2. Kasagi & Shimaki (Sweeping Sori Upper Crossbeams)
    const kasagiCurve = new THREE.QuadraticBezierCurve3(
        new THREE.Vector3(-3.9, 5.58, 0),
        new THREE.Vector3(0, 5.25, 0),
        new THREE.Vector3(3.9, 5.58, 0)
    );
    const kasagi = new THREE.Mesh(new THREE.TubeGeometry(kasagiCurve, 48, 0.24, 12, false), blackLacquerMat);
    kasagi.scale.set(1, 1.25, 0.92);
    kasagi.castShadow = true;
    torii.add(kasagi);

    const shimakiCurve = new THREE.QuadraticBezierCurve3(
        new THREE.Vector3(-3.6, 5.15, 0),
        new THREE.Vector3(0, 4.88, 0),
        new THREE.Vector3(3.6, 5.15, 0)
    );
    const shimaki = new THREE.Mesh(new THREE.TubeGeometry(shimakiCurve, 48, 0.22, 12, false), vermilionMat);
    shimaki.scale.set(1, 1.15, 0.88);
    shimaki.castShadow = true;
    torii.add(shimaki);

    // 3. Nuki
    const nuki = new THREE.Mesh(new THREE.BoxGeometry(5.8, 0.28, 0.34), vermilionMat);
    nuki.position.set(0, 4.02, 0);
    nuki.castShadow = true;
    torii.add(nuki);

    // 4. Gakuzuka
    const gakuzukaTex = createToriiPlaqueTexture();
    const gakuzukaMat = new THREE.MeshStandardMaterial({
        map: gakuzukaTex,
        roughness: 0.3,
        metalness: 0.2
    });
    const gakuzuka = new THREE.Mesh(new THREE.BoxGeometry(0.55, 0.82, 0.12), gakuzukaMat);
    gakuzuka.position.set(0, 4.54, 0.16);
    torii.add(gakuzuka);

    const gakuzukaFrame = new THREE.Mesh(new THREE.BoxGeometry(0.59, 0.86, 0.08), goldMat);
    gakuzukaFrame.position.set(0, 4.54, 0.14);
    torii.add(gakuzukaFrame);

    // 5. Sacred Braided Shimenawa
    const ropeGroup = new THREE.Group();
    const ropeSegments = 36;
    for (let strand = 0; strand < 2; strand++) {
        const points = [];
        for (let i = 0; i <= ropeSegments; i++) {
            const u = i / ropeSegments;
            const x = (-dist + 0.2) + u * (dist * 2 - 0.4);
            const sag = Math.sin(u * Math.PI) * 0.48;
            const y = 3.86 - sag;
            const phase = u * Math.PI * 8 + strand * Math.PI;
            const rOffset = Math.sin(u * Math.PI) * 0.05 + 0.05;
            const z = 0.18 + Math.cos(phase) * rOffset;
            points.push(new THREE.Vector3(x, y + Math.sin(phase) * rOffset, z));
        }
        const ropeCurve = new THREE.CatmullRomCurve3(points);
        const ropeMesh = new THREE.Mesh(new THREE.TubeGeometry(ropeCurve, 40, 0.075, 8, false), shimenawaStrawMat);
        ropeMesh.castShadow = true;
        ropeGroup.add(ropeMesh);
    }
    torii.add(ropeGroup);

    [-1.2, -0.4, 0.4, 1.2].forEach(fx => {
        const fusa = new THREE.Mesh(new THREE.ConeGeometry(0.045, 0.28, 8), shimenawaStrawMat);
        const sag = Math.sin(((fx + dist) / (dist * 2)) * Math.PI) * 0.48;
        fusa.position.set(fx, 3.8 - sag - 0.14, 0.2);
        torii.add(fusa);
    });

    // 6. Hanging Shide
    const shidePositions = [-1.35, -0.48, 0.48, 1.35];
    models.shideMeshes = [];
    shidePositions.forEach(x => {
        const shideGroup = new THREE.Group();
        const sag = Math.sin(((x + dist) / (dist * 2)) * Math.PI) * 0.48;
        shideGroup.position.set(x, 3.82 - sag, 0.22);

        const seg1 = new THREE.Mesh(new THREE.BoxGeometry(0.13, 0.19, 0.015), whiteShideMat);
        seg1.rotation.z = 0.25;
        seg1.position.set(-0.03, -0.09, 0);
        shideGroup.add(seg1);

        const seg2 = new THREE.Mesh(new THREE.BoxGeometry(0.13, 0.19, 0.015), whiteShideMat);
        seg2.rotation.z = -0.25;
        seg2.position.set(0.03, -0.23, 0);
        shideGroup.add(seg2);

        const seg3 = new THREE.Mesh(new THREE.BoxGeometry(0.11, 0.17, 0.015), whiteShideMat);
        seg3.rotation.z = 0.2;
        seg3.position.set(-0.02, -0.36, 0);
        shideGroup.add(seg3);

        torii.add(shideGroup);
        models.shideMeshes.push(shideGroup);
    });

    scene.add(torii);
    models.torii = torii;
}

// 6. High-Performance Instanced Weeping Wisteria Trees
function buildWeepingWisteriaForest() {
    const wisteriaGroup = new THREE.Group();
    wisteriaGroup.name = 'wisteria';

    const barkTex = createBarkTexture();
    const barkMat = new THREE.MeshStandardMaterial({
        color: 0x3d2c25,
        map: barkTex,
        roughness: 0.92,
        metalness: 0.05
    });

    const canopyMat = new THREE.MeshStandardMaterial({
        color: 0x142e23,
        roughness: 0.88
    });

    // High-Performance Instanced Petal Geometry
    const petalGeo = new THREE.ConeGeometry(0.065, 0.15, 5);
    petalGeo.rotateX(Math.PI); // Tip points downward

    const blossomMat = new THREE.MeshStandardMaterial({
        color: 0xffffff, // Tinted via instance colors
        roughness: 0.42,
        metalness: 0.05,
        emissive: 0x7e22ce,
        emissiveIntensity: 0.22
    });

    wisteriaClustersData = [];
    wisteriaGlowLights = [];

    // Precalculate all cluster origins across the 4 trees
    const treeConfigs = [
        { x: -3.9, z: 2.2, archDir: -1, scale: 1.05 },
        { x: 4.0, z: 2.0, archDir: 1, scale: 1.0 },
        { x: -4.4, z: -1.8, archDir: -1, scale: 0.95 },
        { x: 4.3, z: -1.6, archDir: 1, scale: 0.95 }
    ];

    const clustersList = [];

    treeConfigs.forEach(tCfg => {
        const tree = new THREE.Group();
        tree.position.set(tCfg.x, 0.2, tCfg.z);
        tree.scale.set(tCfg.scale, tCfg.scale, tCfg.scale);

        // Twisted trunk
        const trunkCurve = new THREE.CatmullRomCurve3([
            new THREE.Vector3(0, 0, 0),
            new THREE.Vector3(tCfg.archDir * 0.45, 1.3, 0.1),
            new THREE.Vector3(tCfg.archDir * 0.85, 2.7, -0.2),
            new THREE.Vector3(tCfg.archDir * 1.35, 4.2, 0.15)
        ]);
        const trunk = new THREE.Mesh(new THREE.TubeGeometry(trunkCurve, 24, 0.32, 10, false), barkMat);
        trunk.castShadow = true;
        tree.add(trunk);

        const branchConfigs = [
            { end: new THREE.Vector3(tCfg.archDir * 2.2, 4.8, 0.9), count: 6 },
            { end: new THREE.Vector3(tCfg.archDir * 2.6, 4.5, -0.7), count: 7 },
            { end: new THREE.Vector3(tCfg.archDir * 1.4, 5.0, 0.4), count: 5 },
            { end: new THREE.Vector3(tCfg.archDir * 1.8, 5.1, -1.1), count: 6 }
        ];

        branchConfigs.forEach(bCfg => {
            const bCurve = new THREE.CatmullRomCurve3([
                new THREE.Vector3(tCfg.archDir * 1.35, 4.2, 0.15),
                new THREE.Vector3(tCfg.archDir * 1.8, 4.6, bCfg.end.z * 0.5),
                bCfg.end
            ]);
            const branch = new THREE.Mesh(new THREE.TubeGeometry(bCurve, 14, 0.16, 8, false), barkMat);
            branch.castShadow = true;
            tree.add(branch);

            const canopy = new THREE.Mesh(new THREE.SphereGeometry(1.1, 12, 10), canopyMat);
            canopy.position.set(bCfg.end.x, bCfg.end.y + 0.25, bCfg.end.z);
            canopy.scale.set(1.5, 0.6, 1.3);
            tree.add(canopy);

            for (let c = 0; c < bCfg.count; c++) {
                const ox = (Math.random() - 0.5) * 1.4;
                const oz = (Math.random() - 0.5) * 1.4;
                // World position
                const worldOrigin = new THREE.Vector3(
                    tCfg.x + (bCfg.end.x + ox) * tCfg.scale,
                    0.2 + (bCfg.end.y - 0.1) * tCfg.scale,
                    tCfg.z + (bCfg.end.z + oz) * tCfg.scale
                );
                clustersList.push({
                    origin: worldOrigin,
                    length: 0.85 + Math.random() * 0.45,
                    phase: Math.random() * Math.PI * 2,
                    speed: 1.2 + Math.random() * 0.5
                });
            }
        });

        const glowLight = new THREE.PointLight(0xa855f7, 1.5, 8);
        glowLight.position.set(tCfg.archDir * 1.8, 3.8, 0);
        tree.add(glowLight);
        wisteriaGlowLights.push(glowLight);

        wisteriaGroup.add(tree);
    });

    // Populate InstancedMesh for all flowers (Zero performance waste!)
    const tiersPerRaceme = 7;
    const petalsPerTier = 5;
    const petalsPerCluster = tiersPerRaceme * petalsPerTier; // 35 petals / raceme
    const totalPetals = clustersList.length * petalsPerCluster;

    wisteriaInstancedMesh = new THREE.InstancedMesh(petalGeo, blossomMat, totalPetals);
    wisteriaInstancedMesh.instanceMatrix.setUsage(THREE.DynamicDrawUsage);
    wisteriaInstanceCount = totalPetals;

    const dummy = new THREE.Object3D();
    const colorTop = new THREE.Color(0x6b21a8); // Deep royal violet
    const colorMid = new THREE.Color(0xa855f7); // Soft lavender
    const colorTip = new THREE.Color(0xf3e8ff); // Pale white lilac
    let instanceIdx = 0;

    clustersList.forEach((cluster, cIdx) => {
        const clusterBaseIdx = instanceIdx;
        cluster.baseIndex = clusterBaseIdx;
        cluster.petalTransforms = [];

        for (let t = 0; t < tiersPerRaceme; t++) {
            const v = t / (tiersPerRaceme - 1);
            const tierRadius = 0.16 * (1 - v * 0.65);
            const tierY = -t * 0.16 * cluster.length;

            const tierColor = v < 0.4 
                ? colorTop.clone().lerp(colorMid, v / 0.4) 
                : colorMid.clone().lerp(colorTip, (v - 0.4) / 0.6);

            for (let p = 0; p < petalsPerTier; p++) {
                const ang = (p / petalsPerTier) * Math.PI * 2 + v * 1.5;
                const px = Math.cos(ang) * tierRadius;
                const pz = Math.sin(ang) * tierRadius;
                const py = tierY;

                dummy.position.set(
                    cluster.origin.x + px,
                    cluster.origin.y + py,
                    cluster.origin.z + pz
                );
                dummy.rotation.set(0, ang, 0);
                dummy.scale.set(1 - v * 0.35, 1.0, 1 - v * 0.35);
                dummy.updateMatrix();

                wisteriaInstancedMesh.setMatrixAt(instanceIdx, dummy.matrix);
                wisteriaInstancedMesh.setColorAt(instanceIdx, tierColor);

                cluster.petalTransforms.push({
                    relX: px,
                    relY: py,
                    relZ: pz,
                    scale: 1 - v * 0.35,
                    ang: ang
                });

                instanceIdx++;
            }
        }
    });

    wisteriaInstancedMesh.instanceMatrix.needsUpdate = true;
    if (wisteriaInstancedMesh.instanceColor) wisteriaInstancedMesh.instanceColor.needsUpdate = true;

    wisteriaGroup.add(wisteriaInstancedMesh);
    wisteriaClustersData = clustersList;

    scene.add(wisteriaGroup);
    models.wisteria = wisteriaGroup;
}

// 7. Masterpiece Demon Slayer Nichirin Katana
function buildNichirinKatanaMasterpiece() {
    const katanaEnsemble = new THREE.Group();
    katanaEnsemble.name = 'katana';
    katanaEnsemble.position.set(2.3, 0.24, 1.2);

    const tableMat = new THREE.MeshStandardMaterial({
        color: 0x7f1d1d,
        roughness: 0.32,
        metalness: 0.15
    });
    const goldTrimMat = new THREE.MeshStandardMaterial({
        color: 0xf59e0b,
        roughness: 0.25,
        metalness: 0.88
    });
    const blackStandMat = new THREE.MeshStandardMaterial({
        color: 0x0f172a,
        roughness: 0.22,
        metalness: 0.3
    });

    // 1. Vermilion & Gold Lacquer Shrine Altar Table (Sanbō)
    const tableTop = new THREE.Mesh(new THREE.BoxGeometry(1.65, 0.08, 0.62), tableMat);
    tableTop.position.y = 0.42;
    tableTop.castShadow = true;
    tableTop.receiveShadow = true;
    katanaEnsemble.add(tableTop);

    [-0.8, 0.8].forEach(x => {
        [-0.29, 0.29].forEach(z => {
            const corner = new THREE.Mesh(new THREE.BoxGeometry(0.06, 0.09, 0.06), goldTrimMat);
            corner.position.set(x, 0.42, z);
            katanaEnsemble.add(corner);
        });
    });

    [-0.7, 0.7].forEach(x => {
        [-0.24, 0.24].forEach(z => {
            const leg = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.035, 0.42, 12), tableMat);
            leg.position.set(x, 0.21, z);
            leg.castShadow = true;
            katanaEnsemble.add(leg);
        });
    });

    // 2. Black Lacquer Katanakake Sword Stand
    const standBase = new THREE.Mesh(new THREE.BoxGeometry(1.08, 0.04, 0.28), blackStandMat);
    standBase.position.y = 0.48;
    standBase.castShadow = true;
    katanaEnsemble.add(standBase);

    [-0.28, 0.28].forEach(x => {
        const lowerBody = new THREE.Mesh(new THREE.BoxGeometry(0.06, 0.14, 0.16), blackStandMat);
        lowerBody.position.set(x, 0.57, 0);
        katanaEnsemble.add(lowerBody);

        const midBody = new THREE.Mesh(new THREE.BoxGeometry(0.06, 0.12, 0.14), blackStandMat);
        midBody.position.set(x, 0.73, 0);
        katanaEnsemble.add(midBody);

        const topFinial = new THREE.Mesh(new THREE.CylinderGeometry(0.035, 0.035, 0.05, 12), goldTrimMat);
        topFinial.position.set(x, 0.82, 0);
        katanaEnsemble.add(topFinial);
    });

    // 3. Nichirin Katana with Authentic Hamon & Flame Tsuba
    const y0 = 0.81;
    const curveSori = (x) => y0 + 0.045 * Math.pow((x + 0.38) / 1.06, 2);

    const bladeSegments = 24;
    const bladePositions = [];
    const bladeUVs = [];
    const bladeIndices = [];

    for (let i = 0; i <= bladeSegments; i++) {
        const u = i / bladeSegments;
        const x = -0.10 + u * (0.68 - (-0.10));
        const y = curveSori(x);
        const taper = 1 - u * 0.35;

        const dy = 0.09 * (x + 0.38) / Math.pow(1.06, 2);
        const theta = Math.atan(dy);
        const nx = -Math.sin(theta);
        const ny = Math.cos(theta);

        if (i === bladeSegments) {
            bladePositions.push(x + 0.03, y + dy * 0.03, 0);
            bladePositions.push(x, y + 0.003, 0.005 * taper);
            bladePositions.push(x, y + 0.003, -0.005 * taper);
            bladePositions.push(x - nx * 0.012 * taper, y - ny * 0.012 * taper, 0);
        } else {
            bladePositions.push(x, y + 0.010 * taper, 0);
            bladePositions.push(x, y + 0.004, 0.007 * taper);
            bladePositions.push(x, y + 0.004, -0.007 * taper);
            bladePositions.push(x - nx * 0.015 * taper, y - ny * 0.015 * taper, 0);
        }

        bladeUVs.push(u, 1);
        bladeUVs.push(u, 0.5);
        bladeUVs.push(u, 0.5);
        bladeUVs.push(u, 0);
    }

    for (let i = 0; i < bladeSegments; i++) {
        const r1 = i * 4;
        const r2 = (i + 1) * 4;

        bladeIndices.push(r1, r2, r2 + 1); bladeIndices.push(r1, r2 + 1, r1 + 1);
        bladeIndices.push(r1, r1 + 2, r2 + 2); bladeIndices.push(r1, r2 + 2, r2);

        bladeIndices.push(r1 + 1, r2 + 1, r2 + 3); bladeIndices.push(r1 + 1, r2 + 3, r1 + 3);
        bladeIndices.push(r1 + 2, r1 + 3, r2 + 3); bladeIndices.push(r1 + 2, r2 + 3, r2 + 2);
    }

    const bladeGeo = new THREE.BufferGeometry();
    bladeGeo.setAttribute('position', new THREE.Float32BufferAttribute(bladePositions, 3));
    bladeGeo.setAttribute('uv', new THREE.Float32BufferAttribute(bladeUVs, 2));
    bladeGeo.setIndex(bladeIndices);
    bladeGeo.computeVertexNormals();

    const hamonTex = createHamonTexture();
    const steelMat = new THREE.MeshStandardMaterial({
        color: 0xf1f5f9,
        map: hamonTex,
        metalness: 0.96,
        roughness: 0.12,
        emissive: 0x38bdf8,
        emissiveIntensity: 0.12
    });
    const bladeMesh = new THREE.Mesh(bladeGeo, steelMat);
    bladeMesh.castShadow = true;
    katanaEnsemble.add(bladeMesh);

    const habakiY = curveSori(-0.115);
    const habaki = new THREE.Mesh(new THREE.BoxGeometry(0.045, 0.040, 0.026), goldTrimMat);
    habaki.position.set(-0.115, habakiY, 0);
    katanaEnsemble.add(habaki);

    const tsubaY = curveSori(-0.14);
    const tsubaGroup = new THREE.Group();
    tsubaGroup.position.set(-0.14, tsubaY, 0);
    tsubaGroup.rotation.z = Math.PI / 2;

    const tsubaCore = new THREE.Mesh(new THREE.CylinderGeometry(0.09, 0.09, 0.016, 24), blackStandMat);
    tsubaGroup.add(tsubaCore);
    const tsubaRim = new THREE.Mesh(new THREE.TorusGeometry(0.09, 0.015, 12, 24), goldTrimMat);
    tsubaGroup.add(tsubaRim);
    katanaEnsemble.add(tsubaGroup);

    const tsukaLength = 0.25;
    const tsukaY = curveSori(-0.265);
    const tsukaMat = new THREE.MeshStandardMaterial({
        color: 0x09090b,
        roughness: 0.72
    });
    const tsuka = new THREE.Mesh(new THREE.CylinderGeometry(0.023, 0.025, tsukaLength, 16), tsukaMat);
    tsuka.position.set(-0.265, tsukaY, 0);
    tsuka.rotation.z = Math.PI / 2;
    tsuka.castShadow = true;
    katanaEnsemble.add(tsuka);

    const kashiraY = curveSori(-0.39);
    const kashira = new THREE.Mesh(new THREE.CylinderGeometry(0.026, 0.026, 0.028, 16), goldTrimMat);
    kashira.position.set(-0.39, kashiraY, 0);
    kashira.rotation.z = Math.PI / 2;
    katanaEnsemble.add(kashira);

    const sayaY0 = 0.65;
    const sayaCurveSori = (x) => sayaY0 + 0.045 * Math.pow((x + 0.38) / 1.06, 2);

    const sayaCurve = new THREE.QuadraticBezierCurve3(
        new THREE.Vector3(-0.36, sayaCurveSori(-0.36), 0),
        new THREE.Vector3(0.15, sayaCurveSori(0.15), 0),
        new THREE.Vector3(0.68, sayaCurveSori(0.68), 0)
    );
    const sayaMat = new THREE.MeshStandardMaterial({
        color: 0x09090b,
        roughness: 0.15,
        metalness: 0.25
    });
    const saya = new THREE.Mesh(new THREE.TubeGeometry(sayaCurve, 24, 0.028, 12, false), sayaMat);
    saya.castShadow = true;
    katanaEnsemble.add(saya);

    const kojiri = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.03, 0.04, 12), goldTrimMat);
    kojiri.position.set(0.68, sayaCurveSori(0.68), 0);
    kojiri.rotation.z = Math.PI / 2;
    katanaEnsemble.add(kojiri);

    scene.add(katanaEnsemble);
    models.katana = katanaEnsemble;
}

// 8. Kasuga Stone Lanterns with Hollow Washi Hibukuro & Flickering Flame
function buildKasugaStoneLanterns() {
    const stoneNoiseTex = createStoneTexture();
    const stoneMat = new THREE.MeshStandardMaterial({
        color: 0x475569,
        map: stoneNoiseTex,
        roughness: 0.88,
        metalness: 0.05
    });

    const washiPaperMat = new THREE.MeshBasicMaterial({
        color: 0xfef08a,
        transparent: true,
        opacity: 0.85
    });

    const candleFlameMat = new THREE.MeshBasicMaterial({
        color: 0xffa500
    });

    models.lanterns = [];
    lanternPointLights = [];

    [-2.6, 2.6].forEach((x, idx) => {
        const lantern = new THREE.Group();
        lantern.name = 'lantern';
        lantern.position.set(x, 0.24, 2.2);

        const base = new THREE.Mesh(new THREE.CylinderGeometry(0.44, 0.54, 0.35, 6), stoneMat);
        base.position.y = 0.175;
        base.castShadow = true;
        lantern.add(base);

        const shaft = new THREE.Mesh(new THREE.CylinderGeometry(0.16, 0.19, 1.15, 6), stoneMat);
        shaft.position.y = 0.92;
        shaft.castShadow = true;
        lantern.add(shaft);

        const chudai = new THREE.Mesh(new THREE.CylinderGeometry(0.52, 0.38, 0.22, 6), stoneMat);
        chudai.position.y = 1.58;
        chudai.castShadow = true;
        lantern.add(chudai);

        [-0.17, 0.17].forEach(px => {
            [-0.17, 0.17].forEach(pz => {
                const cornerPillar = new THREE.Mesh(new THREE.BoxGeometry(0.07, 0.44, 0.07), stoneMat);
                cornerPillar.position.set(px, 1.91, pz);
                lantern.add(cornerPillar);
            });
        });

        const washiBox = new THREE.Mesh(new THREE.BoxGeometry(0.32, 0.40, 0.32), washiPaperMat);
        washiBox.position.y = 1.91;
        lantern.add(washiBox);

        const flame = new THREE.Mesh(new THREE.ConeGeometry(0.04, 0.12, 8), candleFlameMat);
        flame.position.y = 1.88;
        lantern.add(flame);

        const roof = new THREE.Mesh(new THREE.ConeGeometry(0.72, 0.42, 6), stoneMat);
        roof.position.y = 2.34;
        roof.castShadow = true;
        lantern.add(roof);

        const hoju = new THREE.Mesh(new THREE.SphereGeometry(0.12, 12, 12), stoneMat);
        hoju.position.y = 2.60;
        lantern.add(hoju);

        const pLight = new THREE.PointLight(0xff9922, 2.4, 7.5);
        pLight.position.set(x, 2.15, 2.2);
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

// 9. Daruma Doll (だるま - Iconic Crane Brows, Turtle Moustache & "福" Belly)
function buildDarumaDoll() {
    const daruma = new THREE.Group();
    daruma.name = 'daruma';
    // Positioned forward on left terrace beside Maneki-Neko, facing camera clearly
    daruma.position.set(-1.4, 0.24, 1.8);

    const stoneNoiseTex = createStoneTexture();
    const altar = new THREE.Mesh(
        new THREE.CylinderGeometry(0.44, 0.50, 0.42, 16),
        new THREE.MeshStandardMaterial({ color: 0x334155, map: stoneNoiseTex, roughness: 0.9 })
    );
    altar.position.y = 0.21;
    altar.castShadow = true;
    daruma.add(altar);

    const darumaTex = createDarumaTexture();
    const bodyMat = new THREE.MeshStandardMaterial({
        map: darumaTex,
        roughness: 0.38,
        metalness: 0.08
    });

    const bodyGeo = new THREE.SphereGeometry(0.38, 32, 32);
    bodyGeo.scale(1.0, 1.15, 0.96);
    const body = new THREE.Mesh(bodyGeo, bodyMat);
    body.position.y = 0.65;
    body.rotation.y = -Math.PI / 2; // Face texture points directly towards front (+Z camera)
    body.castShadow = true;
    daruma.add(body);

    scene.add(daruma);
    models.daruma = daruma;
}

// 10. Porcelain Maneki-Neko (招き猫 - Calico Coat, Smiling Face & Senmanryō Coin)
function buildManekiNeko() {
    const neko = new THREE.Group();
    neko.name = 'neko';
    // Placed side-by-side with Daruma, clearly visible and easily selectable
    neko.position.set(-2.3, 0.24, 1.8);

    const stoneNoiseTex = createStoneTexture();
    const plinth = new THREE.Mesh(
        new THREE.CylinderGeometry(0.40, 0.46, 0.40, 16),
        new THREE.MeshStandardMaterial({ color: 0x334155, map: stoneNoiseTex, roughness: 0.9 })
    );
    plinth.position.y = 0.20;
    plinth.castShadow = true;
    neko.add(plinth);

    const nekoTex = createManekiNekoTexture();
    const nekoHeadMat = new THREE.MeshStandardMaterial({
        map: nekoTex,
        roughness: 0.16,
        metalness: 0.08
    });
    const whitePorcelainMat = new THREE.MeshStandardMaterial({
        color: 0xf8fafc,
        roughness: 0.18,
        metalness: 0.06
    });
    const goldMat = new THREE.MeshStandardMaterial({
        color: 0xf59e0b,
        roughness: 0.22,
        metalness: 0.88
    });
    const redCollarMat = new THREE.MeshStandardMaterial({
        color: 0xef4444,
        roughness: 0.35
    });

    // Body
    const body = new THREE.Mesh(new THREE.SphereGeometry(0.31, 24, 24), whitePorcelainMat);
    body.position.y = 0.58;
    body.scale.set(1.0, 1.25, 0.95);
    body.castShadow = true;
    neko.add(body);

    // Head
    const head = new THREE.Mesh(new THREE.SphereGeometry(0.24, 24, 24), nekoHeadMat);
    head.position.set(0, 0.94, 0.04);
    head.rotation.y = -Math.PI / 2;
    neko.add(head);

    // Ears
    [-0.11, 0.11].forEach(x => {
        const ear = new THREE.Mesh(new THREE.ConeGeometry(0.075, 0.14, 12), redCollarMat);
        ear.position.set(x, 1.13, 0.04);
        ear.rotation.z = x > 0 ? -0.28 : 0.28;
        neko.add(ear);
    });

    // Raised Welcoming Paw (Right Paw)
    const paw = new THREE.Mesh(new THREE.CylinderGeometry(0.045, 0.05, 0.22, 12), whitePorcelainMat);
    paw.position.set(0.22, 0.98, 0.14);
    paw.rotation.z = -0.65;
    paw.rotation.x = -0.2;
    neko.add(paw);

    // Red Collar & Golden Suzu Bell
    const collar = new THREE.Mesh(new THREE.TorusGeometry(0.18, 0.024, 12, 24), redCollarMat);
    collar.position.set(0, 0.77, 0.05);
    collar.rotation.x = Math.PI / 2;
    neko.add(collar);

    const bell = new THREE.Mesh(new THREE.SphereGeometry(0.042, 12, 12), goldMat);
    bell.position.set(0.02, 0.74, 0.22);
    neko.add(bell);

    // Golden Koban Coin ("千万両") in left hand
    const kobanTex = createKobanTexture();
    const kobanMat = new THREE.MeshStandardMaterial({
        map: kobanTex,
        roughness: 0.25,
        metalness: 0.85
    });
    const koban = new THREE.Mesh(new THREE.BoxGeometry(0.18, 0.32, 0.025), kobanMat);
    koban.position.set(-0.16, 0.66, 0.18);
    koban.rotation.z = 0.25;
    koban.rotation.y = 0.2;
    neko.add(koban);

    scene.add(neko);
    models.neko = neko;
}

// 11. Refined Ambient Particles (Soft Petals & Gentle Fireflies)
function buildDualParticleSystems() {
    const sakuraCount = 180;
    sakuraGeo = new THREE.BufferGeometry();
    const sakuraPos = new Float32Array(sakuraCount * 3);
    const sakuraSpeeds = new Float32Array(sakuraCount * 3);

    for (let i = 0; i < sakuraCount; i++) {
        sakuraPos[i * 3] = (Math.random() - 0.5) * 26;
        sakuraPos[i * 3 + 1] = Math.random() * 12;
        sakuraPos[i * 3 + 2] = (Math.random() - 0.5) * 26;

        sakuraSpeeds[i * 3] = (Math.random() - 0.5) * 0.012;
        sakuraSpeeds[i * 3 + 1] = -0.008 - Math.random() * 0.015;
        sakuraSpeeds[i * 3 + 2] = (Math.random() - 0.5) * 0.012;
    }

    sakuraGeo.setAttribute('position', new THREE.BufferAttribute(sakuraPos, 3));
    sakuraGeo.userData = { speeds: sakuraSpeeds };

    const sakuraTex = createPetalTexture('#fbcfe8', '#f472b6');
    const sakuraMat = new THREE.PointsMaterial({
        size: 0.16,
        map: sakuraTex,
        transparent: true,
        opacity: 0.75,
        depthWrite: false,
        blending: THREE.NormalBlending
    });

    sakuraParticles = new THREE.Points(sakuraGeo, sakuraMat);
    scene.add(sakuraParticles);
    models.sakura = sakuraParticles;

    const wisteriaCount = 140;
    wisteriaGeo = new THREE.BufferGeometry();
    const wisteriaPos = new Float32Array(wisteriaCount * 3);
    const wisteriaSpeeds = new Float32Array(wisteriaCount * 3);

    for (let i = 0; i < wisteriaCount; i++) {
        wisteriaPos[i * 3] = (Math.random() - 0.5) * 18;
        wisteriaPos[i * 3 + 1] = Math.random() * 8;
        wisteriaPos[i * 3 + 2] = (Math.random() - 0.5) * 18;

        wisteriaSpeeds[i * 3] = (Math.random() - 0.5) * 0.008;
        wisteriaSpeeds[i * 3 + 1] = 0.010 + Math.random() * 0.015;
        wisteriaSpeeds[i * 3 + 2] = (Math.random() - 0.5) * 0.008;
    }

    wisteriaGeo.setAttribute('position', new THREE.BufferAttribute(wisteriaPos, 3));
    wisteriaGeo.userData = { speeds: wisteriaSpeeds };

    const wisteriaTex = createRadialGlowTexture('rgba(216, 180, 254, 0.9)', 'rgba(147, 51, 234, 0)');
    const wisteriaMat = new THREE.PointsMaterial({
        size: 0.15,
        map: wisteriaTex,
        transparent: true,
        opacity: 0.65,
        blending: THREE.AdditiveBlending,
        depthWrite: false
    });

    wisteriaParticles = new THREE.Points(wisteriaGeo, wisteriaMat);
    scene.add(wisteriaParticles);

    const fireflyCount = 45;
    fireflyGeo = new THREE.BufferGeometry();
    const fireflyPos = new Float32Array(fireflyCount * 3);
    const fireflySpeeds = new Float32Array(fireflyCount * 3);

    for (let i = 0; i < fireflyCount; i++) {
        fireflyPos[i * 3] = (Math.random() - 0.5) * 10;
        fireflyPos[i * 3 + 1] = 0.4 + Math.random() * 2.5;
        fireflyPos[i * 3 + 2] = (Math.random() - 0.5) * 10;

        fireflySpeeds[i * 3] = (Math.random() - 0.5) * 0.01;
        fireflySpeeds[i * 3 + 1] = (Math.random() - 0.5) * 0.008;
        fireflySpeeds[i * 3 + 2] = (Math.random() - 0.5) * 0.01;
    }

    fireflyGeo.setAttribute('position', new THREE.BufferAttribute(fireflyPos, 3));
    fireflyGeo.userData = { speeds: fireflySpeeds };

    const fireflyTex = createRadialGlowTexture('rgba(254, 240, 138, 1)', 'rgba(234, 179, 8, 0)');
    const fireflyMat = new THREE.PointsMaterial({
        size: 0.22,
        map: fireflyTex,
        transparent: true,
        opacity: 0.82,
        blending: THREE.AdditiveBlending,
        depthWrite: false
    });

    fireflyParticles = new THREE.Points(fireflyGeo, fireflyMat);
    scene.add(fireflyParticles);
}

// ==========================================================================
// PROCEDURAL SHINTO CHIME & AUDIO
// ==========================================================================
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
        const freqs = [587.33, 880.00, 1174.66, 1760.00];

        freqs.forEach((freq, idx) => {
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();

            osc.type = idx === 0 ? 'sine' : 'triangle';
            osc.frequency.setValueAtTime(freq, now);

            gain.gain.setValueAtTime(0.07 / (idx + 1), now);
            gain.gain.exponentialRampToValueAtTime(0.0001, now + 2.8 + idx * 0.4);

            osc.connect(gain);
            gain.connect(audioCtx.destination);

            osc.start(now);
            osc.stop(now + 3.2 + idx * 0.4);
        });
    } catch (e) {
        // Safe fallback
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

// ==========================================================================
// LIGHTING VISUAL MODES
// ==========================================================================
function updateLightingVisuals() {
    const btn = document.getElementById('btnNightMode');

    if (isNight) {
        scene.background.setHex(0x0a0718);
        scene.fog.color.setHex(0x0e0a24);
        ambientLight.color.setHex(0x1a153b);
        ambientLight.intensity = 1.05;
        dirLight.color.setHex(0xb4c6fc);
        dirLight.intensity = 0.95;
        moonRimLight.intensity = 0.45;

        if (models.starfield) models.starfield.visible = true;
        if (models.moon) models.moon.visible = true;

        lanternPointLights.forEach(item => { item.light.intensity = item.baseIntensity; });
        wisteriaGlowLights.forEach(light => { light.intensity = 1.5; });

        if (btn) {
            btn.innerHTML = '<span class="dock-btn-icon">🌙</span><span class="dock-btn-label">Đêm Tử Đằng</span>';
            btn.classList.add('active');
        }
    } else {
        scene.background.setHex(0x271638);
        scene.fog.color.setHex(0x351a44);
        ambientLight.color.setHex(0x56305a);
        ambientLight.intensity = 1.25;
        dirLight.color.setHex(0xfde68a);
        dirLight.intensity = 1.30;
        moonRimLight.intensity = 0.25;

        if (models.starfield) models.starfield.visible = false;
        if (models.moon) models.moon.visible = true;

        lanternPointLights.forEach(item => { item.light.intensity = item.baseIntensity * 0.45; });
        wisteriaGlowLights.forEach(light => { light.intensity = 1.0; });

        if (btn) {
            btn.innerHTML = '<span class="dock-btn-icon">🌅</span><span class="dock-btn-label">Hừng Đông</span>';
            btn.classList.remove('active');
        }
    }
}

// ==========================================================================
// INTERACTIVE RAYCASTING & FOCUS GLIDE
// ==========================================================================
function onCanvasClick(e) {
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

function startCameraTransition(camEnd, targetEnd, duration = 950) {
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

    document.querySelectorAll('.obj-pill').forEach(p => p.classList.remove('active'));
    const activePill = document.getElementById(`pill-${key}`);
    if (activePill) {
        activePill.classList.add('active');
        activePill.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
    }

    startCameraTransition(data.camPos, data.lookAt, 950);
    playTempleChimeSound();
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
    currentActiveItem = item;

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

    modal.classList.add('open');
    modal.style.display = 'block';

    if (autoPlayAudio && window.speakText) {
        window.speakText(item.kana || item.kanji, document.getElementById('cardAudioBtn'));
    }
}

function closeModal() {
    const modal = document.getElementById('vocabModal');
    if (modal) {
        modal.classList.remove('open');
        modal.style.display = 'none';
    }
}

function speakCurrentCard() {
    if (currentActiveItem && window.speakText) {
        window.speakText(currentActiveItem.kana || currentActiveItem.kanji, document.getElementById('cardAudioBtn'));
    }
}

// ==========================================================================
// CINEMATIC DRONE ROAM & DOCK CONTROLS
// ==========================================================================
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

function syncAutoRotateUI() {
    const btn = document.getElementById('btnAutoRotate');
    if (btn) {
        btn.innerHTML = `<span class="dock-btn-icon">🔄</span><span class="dock-btn-label">Xoay 360°: ${autoRotate ? 'BẬT' : 'TẮT'}</span>`;
        btn.classList.toggle('active', autoRotate);
    }
}

function toggleAutoRotate() {
    autoRotate = !autoRotate;
    controls.autoRotate = autoRotate;
    syncAutoRotateUI();
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
    applyDefaultCameraPose();
    closeModal();
    const toriiPill = document.getElementById('pill-torii');
    if (toriiPill) toriiPill.classList.add('active');
    playTempleChimeSound();
}

function onWindowResize() {
    const aspect = window.innerWidth / window.innerHeight;
    camera.aspect = aspect;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

// ==========================================================================
// MAIN ANIMATION LOOP
// ==========================================================================
function animate() {
    requestAnimationFrame(animate);

    if (!isTabActive) return;

    const delta = clock.getDelta();
    const elapsedTime = clock.getElapsedTime();

    // 1. Camera Glide Transition or Cinematic Roam
    if (isTransitioning) {
        const now = performance.now();
        const elapsed = now - transitionStartTime;
        const t = Math.min(1.0, elapsed / transitionDuration);
        const ease = 1 - Math.pow(1 - t, 3);

        camera.position.lerpVectors(transitionStartCam, transitionEndCam, ease);
        controls.target.lerpVectors(transitionStartTarget, transitionEndTarget, ease);

        if (t >= 1.0) {
            isTransitioning = false;
            camera.position.copy(transitionEndCam);
            controls.target.copy(transitionEndTarget);
        }
    } else if (isCinematic) {
        cinematicAngle += 0.16 * delta;
        const camX = Math.sin(cinematicAngle) * cinematicRadius;
        const camZ = Math.cos(cinematicAngle) * cinematicRadius;
        const camY = cinematicHeight + Math.sin(cinematicAngle * 1.5) * 0.8;

        camera.position.set(camX, camY, camZ);
        controls.target.set(0, 2.8, 0);
    }

    // 2. Flickering Stone Lantern Fire Light
    lanternPointLights.forEach(item => {
        if (isNight) {
            const flicker = Math.sin(elapsedTime * 7 + item.flickerOffset) * 0.3 +
                            (Math.random() - 0.5) * 0.2;
            item.light.intensity = item.baseIntensity + flicker;
        }
    });

    // 3. Swaying Shide Paper Streamers & Wisteria Clusters
    if (models.shideMeshes) {
        models.shideMeshes.forEach((shide, idx) => {
            shide.rotation.z = Math.sin(elapsedTime * 2.2 + idx * 0.8) * 0.10;
            shide.rotation.x = Math.cos(elapsedTime * 1.8 + idx * 0.5) * 0.06;
        });
    }

    // 4. Subtle Breeze Sway for Instanced Wisteria Clusters
    if (wisteriaInstancedMesh && wisteriaClustersData.length > 0) {
        const dummy = new THREE.Object3D();
        let idx = 0;

        wisteriaClustersData.forEach(cluster => {
            const swayZ = Math.sin(elapsedTime * cluster.speed + cluster.phase) * 0.06;
            const swayX = Math.cos(elapsedTime * cluster.speed * 0.85 + cluster.phase) * 0.04;

            cluster.petalTransforms.forEach(pt => {
                // Sway amplifies down the length of the cluster
                const depthFactor = -pt.relY * 0.8;
                const curX = cluster.origin.x + pt.relX + swayX * depthFactor;
                const curY = cluster.origin.y + pt.relY;
                const curZ = cluster.origin.z + pt.relZ + swayZ * depthFactor;

                dummy.position.set(curX, curY, curZ);
                dummy.rotation.set(swayZ * 0.8, pt.ang, swayX * 0.8);
                dummy.scale.set(pt.scale, 1.0, pt.scale);
                dummy.updateMatrix();

                wisteriaInstancedMesh.setMatrixAt(idx, dummy.matrix);
                idx++;
            });
        });
        wisteriaInstancedMesh.instanceMatrix.needsUpdate = true;
    }

    // 5. Drifting Sakura Petals
    if (particlesActive && sakuraGeo) {
        const pos = sakuraGeo.attributes.position.array;
        const spd = sakuraGeo.userData.speeds;
        const count = pos.length / 3;

        for (let i = 0; i < count; i++) {
            pos[i * 3] += spd[i * 3] + Math.sin(elapsedTime * 0.8 + i) * 0.004;
            pos[i * 3 + 1] += spd[i * 3 + 1];
            pos[i * 3 + 2] += spd[i * 3 + 2];

            if (pos[i * 3 + 1] < 0) {
                pos[i * 3 + 1] = 12.0;
                pos[i * 3] = (Math.random() - 0.5) * 26;
                pos[i * 3 + 2] = (Math.random() - 0.5) * 26;
            }
        }
        sakuraGeo.attributes.position.needsUpdate = true;
    }

    // 6. Upward Swirling Wisteria Embers
    if (particlesActive && wisteriaGeo) {
        const pos = wisteriaGeo.attributes.position.array;
        const spd = wisteriaGeo.userData.speeds;
        const count = pos.length / 3;

        for (let i = 0; i < count; i++) {
            pos[i * 3] += spd[i * 3] + Math.cos(elapsedTime * 1.2 + i) * 0.005;
            pos[i * 3 + 1] += spd[i * 3 + 1];
            pos[i * 3 + 2] += spd[i * 3 + 2] + Math.sin(elapsedTime * 1.2 + i) * 0.005;

            if (pos[i * 3 + 1] > 8.0) {
                pos[i * 3 + 1] = 0.2;
                pos[i * 3] = (Math.random() - 0.5) * 18;
                pos[i * 3 + 2] = (Math.random() - 0.5) * 18;
            }
        }
        wisteriaGeo.attributes.position.needsUpdate = true;
    }

    // 7. Gentle Fireflies Dancing
    if (particlesActive && fireflyGeo) {
        const pos = fireflyGeo.attributes.position.array;
        const spd = fireflyGeo.userData.speeds;
        const count = pos.length / 3;

        for (let i = 0; i < count; i++) {
            pos[i * 3] += Math.sin(elapsedTime * 1.6 + i) * 0.005;
            pos[i * 3 + 1] += Math.cos(elapsedTime * 1.6 + i) * 0.004;
            pos[i * 3 + 2] += spd[i * 3 + 2];

            if (pos[i * 3 + 2] > 7.5) pos[i * 3 + 2] = -5.5;
        }
        fireflyGeo.attributes.position.needsUpdate = true;
    }

    // OrbitControls Update & Render
    controls.update();
    renderer.render(scene, camera);

    // Performance info logger for verification
    if (!window._loggedInfo) {
        window._infoFrame = (window._infoFrame || 0) + 1;
        if (window._infoFrame >= 5) {
            window._loggedInfo = true;
            console.log('REFINED_RENDERER_INFO:', JSON.stringify({
                calls: renderer.info.render.calls,
                triangles: renderer.info.render.triangles,
                points: renderer.info.render.points,
                lines: renderer.info.render.lines,
                geometries: renderer.info.memory.geometries,
                textures: renderer.info.memory.textures
            }));
        }
    }
}

// Auto-run on DOM ready
document.addEventListener('DOMContentLoaded', init);
