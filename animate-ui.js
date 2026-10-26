/**
 * Animate UI (Vanilla Runtime Engine)
 * High-performance 60fps/120fps micro-interactions, spotlight, tilt & springs.
 * https://github.com/imskyleen/animate-ui
 */

(function () {
  'use strict';

  // Check if reduced motion is requested
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /**
   * 1. Ripple Effect on Click/Tap (Animate UI Button / Click Primitive)
   */
  function initRipple() {
    if (prefersReducedMotion) return;

    document.addEventListener('pointerdown', (e) => {
      const target = e.target.closest(
        'button, .btn, .dock-pill, .dock-action-btn, .quiz-opt, .sheet-lesson-link, .fc-speaker-btn, .tab-btn, a[class*="btn"]'
      );
      if (!target || target.disabled) return;

      target.classList.add('aui-ripple-host');
      const rect = target.getBoundingClientRect();
      const wave = document.createElement('span');
      wave.className = 'aui-ripple-wave';

      const diameter = Math.max(rect.width, rect.height);
      const x = e.clientX - rect.left - diameter / 2;
      const y = e.clientY - rect.top - diameter / 2;

      wave.style.width = `${diameter}px`;
      wave.style.height = `${diameter}px`;
      wave.style.left = `${x}px`;
      wave.style.top = `${y}px`;

      target.appendChild(wave);
      wave.addEventListener('animationend', () => wave.remove(), { once: true });
    }, { passive: true });
  }

  /**
   * 2. Card Spotlight & 3D Tilt Engine (RAF throttled for 120fps smoothness)
   */
  function initCardSpotlightAndTilt() {
    if (prefersReducedMotion) return;

    const CARD_SELECTORS = '.card, .fc-card, .grammar-box, .test-card, .lesson-card, .summary-box, .table-card, .sheet-topic-card, .vocab-card';
    const MAX_TILT = 4.5; // degrees

    let activeCard = null;
    let rafId = null;
    let mouseX = 0, mouseY = 0;

    function updateTilt() {
      if (!activeCard) return;
      const rect = activeCard.getBoundingClientRect();
      const x = mouseX - rect.left;
      const y = mouseY - rect.top;

      // Update spotlight position
      activeCard.style.setProperty('--aui-mouse-x', `${x}px`);
      activeCard.style.setProperty('--aui-mouse-y', `${y}px`);

      // 3D Tilt calculation
      const cx = rect.width / 2;
      const cy = rect.height / 2;
      const tiltX = ((y - cy) / cy) * -MAX_TILT;
      const tiltY = ((x - cx) / cx) * MAX_TILT;

      activeCard.style.setProperty('--aui-tilt-x', `${tiltX.toFixed(2)}deg`);
      activeCard.style.setProperty('--aui-tilt-y', `${tiltY.toFixed(2)}deg`);
      activeCard.classList.add('aui-tilt-active');
      rafId = null;
    }

    document.addEventListener('pointermove', (e) => {
      const card = e.target.closest(CARD_SELECTORS);
      if (!card) {
        if (activeCard) {
          activeCard.classList.remove('aui-tilt-active');
          activeCard.style.removeProperty('--aui-tilt-x');
          activeCard.style.removeProperty('--aui-tilt-y');
          activeCard = null;
        }
        return;
      }

      activeCard = card;
      mouseX = e.clientX;
      mouseY = e.clientY;

      if (!rafId) {
        rafId = requestAnimationFrame(updateTilt);
      }
    }, { passive: true });

    document.addEventListener('pointerleave', (e) => {
      const card = e.target.closest(CARD_SELECTORS);
      if (card) {
        card.classList.remove('aui-tilt-active');
        card.style.removeProperty('--aui-tilt-x');
        card.style.removeProperty('--aui-tilt-y');
        if (activeCard === card) activeCard = null;
      }
    }, true);
  }

  /**
   * 3. Viewport Scroll Reveal (IntersectionObserver with Stagger)
   */
  function initScrollReveal() {
    if (prefersReducedMotion || !('IntersectionObserver' in window)) return;

    const targets = document.querySelectorAll(
      '.grammar-box, .fc-card, .test-card, .summary-box, .lesson-card, .table-card, .hero-banner'
    );

    const observer = new IntersectionObserver(
      (entries, obs) => {
        entries.forEach((entry, idx) => {
          if (entry.isIntersecting) {
            const el = entry.target;
            // Stagger animation
            setTimeout(() => {
              el.classList.add('aui-reveal-shown');
            }, Math.min(idx * 30, 200));
            obs.unobserve(el);
          }
        });
      },
      { root: null, rootMargin: '0px 0px -40px 0px', threshold: 0.08 }
    );

    targets.forEach((el) => {
      el.classList.add('aui-reveal-init');
      observer.observe(el);
    });
  }

  /**
   * 4. Audio Playing Pulse Indicator
   */
  function initAudioEffects() {
    document.addEventListener('click', (e) => {
      const btn = e.target.closest('.fc-speaker-btn, [onclick*="play"], [onclick*="speak"], [onclick*="Sound"]');
      if (!btn) return;

      btn.classList.add('aui-audio-playing');
      setTimeout(() => {
        btn.classList.remove('aui-audio-playing');
      }, 1600);
    });
  }

  /**
   * 5. Quiz Micro-Interactions (CheckPop & Shake)
   */
  function initQuizFeedback() {
    document.addEventListener('click', (e) => {
      const opt = e.target.closest('.quiz-opt, .opt-btn, .choice-btn, label[class*="opt"]');
      if (!opt) return;

      setTimeout(() => {
        if (opt.classList.contains('correct') || opt.classList.contains('is-correct')) {
          opt.classList.remove('aui-check-pop');
          void opt.offsetWidth; // trigger reflow
          opt.classList.add('aui-check-pop');
        } else if (opt.classList.contains('wrong') || opt.classList.contains('is-wrong') || opt.classList.contains('incorrect')) {
          opt.classList.remove('aui-shake');
          void opt.offsetWidth;
          opt.classList.add('aui-shake');
        }
      }, 60);
    });
  }

  /**
   * 6. Mega Sheet Drawer Keyboard & Outside Click Support
   */
  function initDrawerAccessibility() {
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        const sheet = document.querySelector('.global-mega-sheet.open');
        const toolsMenu = document.querySelector('.dock-tools-menu[style*="display: block"]');
        if (sheet) sheet.classList.remove('open');
        if (toolsMenu) toolsMenu.style.display = 'none';
      }
    });
  }

  // Initialize all modules when DOM is ready
  function init() {
    initRipple();
    initCardSpotlightAndTilt();
    initScrollReveal();
    initAudioEffects();
    initQuizFeedback();
    initDrawerAccessibility();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
