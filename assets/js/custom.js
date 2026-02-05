// HydroSense Custom Controls
// Font size and theme toggle

(function() {
  'use strict';

  // Initialize on page load
  document.addEventListener('DOMContentLoaded', function() {
    initFontSizeControls();
    initThemeToggle();
  });

  // Font size controls
  function initFontSizeControls() {
    const sizes = ['small', 'medium', 'large'];
    const currentSize = localStorage.getItem('fontSize') || 'medium';

    // Apply saved font size
    document.body.classList.add('font-' + currentSize);

    // Create controls container
    const controls = document.createElement('div');
    controls.className = 'font-size-controls';
    controls.setAttribute('aria-label', 'Font size controls');
    controls.innerHTML = `
      <button class="font-btn" data-size="small" title="Small text" aria-label="Small font size">A</button>
      <button class="font-btn" data-size="medium" title="Medium text" aria-label="Medium font size">A</button>
      <button class="font-btn" data-size="large" title="Large text" aria-label="Large font size">A</button>
    `;

    // Add controls to header
    const header = document.querySelector('.site-header');
    if (header) {
      // Create container for all controls
      let controlsContainer = header.querySelector('.site-controls');
      if (!controlsContainer) {
        controlsContainer = document.createElement('div');
        controlsContainer.className = 'site-controls';

        // Insert before aux-nav if it exists, otherwise append
        const auxNav = header.querySelector('.aux-nav');
        if (auxNav) {
          auxNav.parentNode.insertBefore(controlsContainer, auxNav);
        } else {
          header.appendChild(controlsContainer);
        }
      }
      controlsContainer.appendChild(controls);
    }

    // Mark current size as active
    updateFontButtons(currentSize);

    // Handle clicks
    controls.querySelectorAll('.font-btn').forEach(btn => {
      btn.addEventListener('click', function() {
        const size = this.dataset.size;

        // Remove all font size classes
        document.body.classList.remove('font-small', 'font-medium', 'font-large');

        // Add new size class
        document.body.classList.add('font-' + size);

        // Save preference
        localStorage.setItem('fontSize', size);

        // Update button states
        updateFontButtons(size);
      });
    });
  }

  function updateFontButtons(activeSize) {
    document.querySelectorAll('.font-btn').forEach(btn => {
      if (btn.dataset.size === activeSize) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
  }

  // Theme toggle (dark/light mode)
  function initThemeToggle() {
    // Get current theme from localStorage or default to light
    const currentTheme = localStorage.getItem('theme') || 'hydrosense';

    // Apply saved theme
    applyTheme(currentTheme);

    // Create toggle button
    const toggle = document.createElement('div');
    toggle.className = 'theme-toggle';
    toggle.setAttribute('aria-label', 'Theme toggle');
    toggle.innerHTML = `
      <button class="theme-btn" data-theme="hydrosense" title="Light theme" aria-label="Light theme">☀️</button>
      <button class="theme-btn" data-theme="hydrosense_dark" title="Dark theme" aria-label="Dark theme">🌙</button>
    `;

    // Add to controls container
    const header = document.querySelector('.site-header');
    if (header) {
      let controlsContainer = header.querySelector('.site-controls');
      if (!controlsContainer) {
        controlsContainer = document.createElement('div');
        controlsContainer.className = 'site-controls';
        const auxNav = header.querySelector('.aux-nav');
        if (auxNav) {
          auxNav.parentNode.insertBefore(controlsContainer, auxNav);
        } else {
          header.appendChild(controlsContainer);
        }
      }
      controlsContainer.appendChild(toggle);
    }

    // Mark current theme as active
    updateThemeButtons(currentTheme);

    // Handle clicks
    toggle.querySelectorAll('.theme-btn').forEach(btn => {
      btn.addEventListener('click', function() {
        const theme = this.dataset.theme;
        applyTheme(theme);
        localStorage.setItem('theme', theme);
        updateThemeButtons(theme);
      });
    });
  }

  function applyTheme(theme) {
    // Remove existing theme classes
    document.documentElement.classList.remove('hydrosense', 'hydrosense_dark');

    // Add new theme class
    document.documentElement.classList.add(theme);

    // Update color-scheme meta tag for better browser integration
    document.documentElement.setAttribute('data-color-scheme', theme);
  }

  function updateThemeButtons(activeTheme) {
    document.querySelectorAll('.theme-btn').forEach(btn => {
      if (btn.dataset.theme === activeTheme) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
  }
})();
