/**
 * Animate UI (Ultra-High Performance 120fps Engine)
 * Zero-Jank Micro-Interactions, Instant Feedback & Tactile Springs
 * Optimized for Large Datasets (1,200+ Vocab & 144+ Kanji Cards)
 */

(function () {
  'use strict';

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
    initAccessibility();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
