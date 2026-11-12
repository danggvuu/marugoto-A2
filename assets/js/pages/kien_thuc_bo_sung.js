/* Extracted page script for kien_thuc_bo_sung.html */
function toggleTestsDropdown(e) {
    if (e) { e.preventDefault(); e.stopPropagation(); }
    const m = document.getElementById('testsDropdownMenu');
    if (m) m.classList.toggle('show');
    const lm = document.getElementById('lessonsDropdownMenu');
    if (lm) lm.classList.remove('show');
}

function toggleLessonsDropdown(e) {
    if (e) { e.preventDefault(); e.stopPropagation(); }
    const m = document.getElementById('lessonsDropdownMenu');
    if (m) m.classList.toggle('show');
    const tm = document.getElementById('testsDropdownMenu');
    if (tm) tm.classList.remove('show');
}

window.addEventListener('click', function (e) {
    if (e && e.target && e.target.closest && e.target.closest('.hub-dropdown')) return;
    const lm = document.getElementById('lessonsDropdownMenu');
    if (lm) lm.classList.remove('show');
    const tm = document.getElementById('testsDropdownMenu');
    if (tm) tm.classList.remove('show');
});

// Speech synthesis
function speakJP(text) {
    if (!('speechSynthesis' in window)) {
        alert('Trình duyệt của bạn không hỗ trợ phát âm Audio.');
        return;
    }
    window.speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = 'ja-JP';
    u.rate = 0.9;
    window.speechSynthesis.speak(u);
}

// Toggle furigana
function toggleFurigana() {
    document.body.classList.toggle('hide-furigana');
}

// Mini Quiz Verification
function checkMiniQuiz(btn, isCorrect, explanation) {
    const container = btn.closest('.mini-quiz-box');
    const feedback = container.querySelector('.quiz-feedback');
    const allBtns = container.querySelectorAll('.btn-quiz-opt');

    allBtns.forEach(b => {
        b.classList.remove('correct', 'wrong');
    });

    if (isCorrect) {
        btn.classList.add('correct');
        feedback.style.display = 'block';
        feedback.style.background = '#dcfce7';
        feedback.style.color = '#15803d';
        feedback.innerHTML = '🎉 ' + explanation;
    } else {
        btn.classList.add('wrong');
        feedback.style.display = 'block';
        feedback.style.background = '#fee2e2';
        feedback.style.color = '#b91c1c';
        feedback.innerHTML = '❌ ' + explanation;
    }
}

// Live Search Filter
const searchInput = document.getElementById('searchInput');
if (searchInput) {
    searchInput.addEventListener('input', function (e) {
        const q = e.target.value.toLowerCase().trim();
        const cards = document.querySelectorAll('.topic-card');
        cards.forEach(card => {
            const text = (card.innerText + ' ' + (card.getAttribute('data-keywords') || '')).toLowerCase();
            if (!q || text.includes(q)) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    });
}

// Highlight active chip on scroll
window.addEventListener('scroll', () => {
    const sections = document.querySelectorAll('.topic-card');
    const chips = document.querySelectorAll('.sec-chip');
    let current = '';

    sections.forEach(sec => {
        const top = sec.offsetTop - 140;
        if (window.pageYOffset >= top) {
            current = sec.getAttribute('id');
        }
    });

    chips.forEach(chip => {
        chip.classList.remove('active');
        if (chip.getAttribute('href') === '#' + current) {
            chip.classList.add('active');
        }
    });
});
