/**
 * Scroll-Triggered Animated Number Counter
 * Animates numerical values in stat elements when scrolled into view.
 */

document.addEventListener('DOMContentLoaded', () => {
    const counterElements = document.querySelectorAll('.stat-number, .counter-number');
    if (!counterElements.length) return;

    /**
     * Animates a single counter element from 0 to its target value.
     * @param {HTMLElement} el 
     * @param {number} duration Duration in milliseconds (default 1500ms)
     */
    function animateNumberCounter(el, duration = 1500) {
        const rawText = el.getAttribute('data-target') || el.textContent.trim();
        if (!rawText) return;

        // Match leading digits/commas/decimals and trailing non-digit suffix (e.g. "400", "95%", "1,200+")
        const match = rawText.match(/^([0-9,.]+)(.*)$/);
        if (!match) return;

        const targetVal = parseFloat(match[1].replace(/,/g, ''));
        if (isNaN(targetVal)) return;

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
            }
        }

        // Initialize starting value to 0 before starting animation
        el.textContent = (isFloat ? (0).toFixed(decimals) : '0') + suffix;
        requestAnimationFrame(step);
    }

    // Set up IntersectionObserver to trigger animation when scrolled into viewport
    if ('IntersectionObserver' in window) {
        const observerOptions = {
            threshold: 0.15,
            rootMargin: '0px 0px -30px 0px'
        };

        const observer = new IntersectionObserver((entries, obs) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateNumberCounter(entry.target, 1500);
                    obs.unobserve(entry.target);
                }
            });
        }, observerOptions);

        counterElements.forEach(el => observer.observe(el));
    } else {
        // Fallback for environments without IntersectionObserver
        counterElements.forEach(el => animateNumberCounter(el, 1500));
    }
});
