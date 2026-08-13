/**
 * Scroll-Triggered Animated Number Counter
 * Triggers counting animation when the stats card container is scrolled into view.
 */

function initStatCounters() {
    const statsCards = document.querySelectorAll('.stats-card-container, .metrics-grid');
    const counterElements = document.querySelectorAll('.stat-number, .counter-number');
    
    if (!counterElements.length) return;

    /**
     * Animates a single counter element from 0 to its target value.
     * @param {HTMLElement} el 
     * @param {number} duration Duration in milliseconds (default 1500ms)
     */
    function animateSingleCounter(el, duration = 1500) {
        if (el.dataset.animated === 'true') return;
        el.dataset.animated = 'true';

        const rawText = (el.getAttribute('data-target') || el.textContent || '').trim();
        if (!rawText) return;

        const match = rawText.match(/^([0-9,.]+)(.*)$/);
        if (!match) return;

        const targetVal = parseFloat(match[1].replace(/,/g, ''));
        if (isNaN(targetVal)) return;

        const suffix = match[2] || '';
        const isFloat = match[1].includes('.');
        const decimals = isFloat ? (match[1].split('.')[1] || '').length : 0;

        const startTime = performance.now();
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
                // Ensure exact original target value is set upon completion
                el.textContent = rawText;
            }
        }

        requestAnimationFrame(step);
    }

    function triggerCardCounters(container) {
        const counters = container.querySelectorAll('.stat-number, .counter-number');
        counters.forEach((el, index) => {
            // Subtle 60ms stagger delay for a premium modern feel
            setTimeout(() => {
                animateSingleCounter(el, 1500);
            }, index * 60);
        });
    }

    // Set initial displayed text to 0 for all counters before scrolling into view
    counterElements.forEach(el => {
        const rawText = (el.getAttribute('data-target') || el.textContent || '').trim();
        const match = rawText.match(/^([0-9,.]+)(.*)$/);
        if (match) {
            const suffix = match[2] || '';
            const isFloat = match[1].includes('.');
            const decimals = isFloat ? (match[1].split('.')[1] || '').length : 0;
            el.textContent = (isFloat ? (0).toFixed(decimals) : '0') + suffix;
        }
    });

    if ('IntersectionObserver' in window) {
        const observerOptions = {
            threshold: 0.2, // Triggers when 20% of the glass card is visible
            rootMargin: '0px 0px -20px 0px'
        };

        const observer = new IntersectionObserver((entries, obs) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    triggerCardCounters(entry.target);
                    obs.unobserve(entry.target);
                }
            });
        }, observerOptions);

        if (statsCards.length > 0) {
            statsCards.forEach(card => observer.observe(card));
        } else {
            // Fallback: observe individual elements
            counterElements.forEach(el => {
                const singleObs = new IntersectionObserver((entries, sObs) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            animateSingleCounter(entry.target, 1500);
                            sObs.unobserve(entry.target);
                        }
                    });
                }, observerOptions);
                singleObs.observe(el);
            });
        }
    } else {
        // Fallback for browsers without IntersectionObserver support
        counterElements.forEach(el => animateSingleCounter(el, 1500));
    }
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initStatCounters);
} else {
    initStatCounters();
}
