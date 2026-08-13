/**
 * Scroll-Triggered Animated Number Counter
 * Cross-browser compatible (Edge, Chrome, Firefox, Safari)
 */

function initStatCounters() {
    const counterElements = document.querySelectorAll('.stat-number, .counter-number');
    if (!counterElements.length) return;

    /**
     * Animates a single counter element from 0 to its target value.
     * @param {HTMLElement} el 
     * @param {number} duration Duration in milliseconds (default 1500ms)
     */
    function animateNumberCounter(el, duration = 1500) {
        // Prevent double execution on the same element
        if (el.dataset.animating === 'true' || el.dataset.animated === 'true') return;
        el.dataset.animating = 'true';

        const rawText = (el.getAttribute('data-target') || el.textContent || '').trim();
        if (!rawText) {
            el.dataset.animating = 'false';
            return;
        }

        // Match leading digits/commas/decimals and trailing non-digit suffix (e.g. "400", "95%", "1,200+")
        const match = rawText.match(/^([0-9,.]+)(.*)$/);
        if (!match) {
            el.dataset.animating = 'false';
            return;
        }

        const targetVal = parseFloat(match[1].replace(/,/g, ''));
        if (isNaN(targetVal)) {
            el.dataset.animating = 'false';
            return;
        }

        const suffix = match[2] || '';
        const isFloat = match[1].includes('.');
        const decimals = isFloat ? (match[1].split('.')[1] || '').length : 0;
        
        const startTime = performance.now();
        // Smooth ease-out cubic animation
        const easeOutCubic = (t) => 1 - Math.pow(1 - t, 3);

        function step(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const easedProgress = easeOutCubic(progress);
            const currentVal = targetVal * easedProgress;

            if (isFloat) {
                el.textContent = currentVal.toFixed(decimals) + suffix;
            } else {
                el.textContent = Math.floor(currentVal).toLocaleString() + suffix;
            }

            if (progress < 1) {
                requestAnimationFrame(step);
            } else {
                // Ensure exact original text value is set upon completion
                el.textContent = rawText;
                el.dataset.animating = 'false';
                el.dataset.animated = 'true';
            }
        }

        // Initialize starting value to 0 before starting animation
        el.textContent = (isFloat ? (0).toFixed(decimals) : '0') + suffix;
        requestAnimationFrame(step);
    }

    // Set up IntersectionObserver to trigger animation when scrolled into viewport
    if ('IntersectionObserver' in window) {
        const observerOptions = {
            threshold: 0.05,
            rootMargin: '0px 0px 0px 0px'
        };

        const observer = new IntersectionObserver((entries, obs) => {
            entries.forEach(entry => {
                if (entry.isIntersecting || entry.intersectionRatio > 0) {
                    animateNumberCounter(entry.target, 1500);
                    obs.unobserve(entry.target);
                }
            });
        }, observerOptions);

        counterElements.forEach(el => {
            // If already in viewport on page load, trigger immediately
            const rect = el.getBoundingClientRect();
            if (rect.top >= 0 && rect.bottom <= (window.innerHeight || document.documentElement.clientHeight)) {
                animateNumberCounter(el, 1500);
            } else {
                observer.observe(el);
            }
        });
    } else {
        // Fallback for older browsers without IntersectionObserver
        counterElements.forEach(el => animateNumberCounter(el, 1500));
    }
}

// Ensure execution whether script runs before or after DOMContentLoaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initStatCounters);
} else {
    initStatCounters();
}
