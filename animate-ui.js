/**
 * Animate UI (Ultra-High Performance 120fps Engine)
 * Zero-Jank Micro-Interactions, Instant Feedback & Tactile Springs
 * Optimized for Large Datasets (1,200+ Vocab & 144+ Kanji Cards)
 */

(function () {
  'use strict';

  // Check if reduced motion is requested
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /**
   * 1. Audio Playing Pulse Indicator
   */
  function initAudioEffects() {
    document.addEventListener('click', (e) => {
      const btn = e.target.closest('.fc-speaker-btn, .table-speaker-btn, [onclick*="speak"], [onclick*="Play"]');
      if (!btn) return;

      btn.classList.add('aui-audio-playing');
      setTimeout(() => {
        btn.classList.remove('aui-audio-playing');
      }, 1400);
    }, { passive: true });
  }

  /**
   * 2. Quiz Micro-Interactions (Instant CheckPop & Shake)
   */
  function initQuizFeedback() {
    if (prefersReducedMotion) return;

    document.addEventListener('click', (e) => {
      const opt = e.target.closest('.quiz-opt, .opt-btn, .choice-btn, label[class*="opt"]');
      if (!opt) return;

      requestAnimationFrame(() => {
        if (opt.classList.contains('correct') || opt.classList.contains('is-correct')) {
          opt.classList.remove('aui-check-pop');
          void opt.offsetWidth; // trigger reflow
          opt.classList.add('aui-check-pop');
        } else if (opt.classList.contains('wrong') || opt.classList.contains('is-wrong') || opt.classList.contains('incorrect')) {
          opt.classList.remove('aui-shake');
          void opt.offsetWidth;
          opt.classList.add('aui-shake');
        }
      });
    }, { passive: true });
  }

  /**
   * 3. Drawer & Modal Keyboard Accessibility (Escape to Close)
   */
  function initAccessibility() {
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        const sheet = document.querySelector('.global-mega-sheet.open');
        const toolsMenu = document.querySelector('.dock-tools-menu[style*="display: block"]');
        const lessonMenu = document.getElementById('lessonsDropdownMenu.show');
        if (sheet) sheet.classList.remove('open');
        if (toolsMenu) toolsMenu.style.display = 'none';
        if (lessonMenu) lessonMenu.classList.remove('show');
      }
    });
  }

  function init() {
    initAudioEffects();
    initQuizFeedback();
    initAccessibility();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
