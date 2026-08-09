/* Core Client-Side Quiz Engine: Pagination, Timers, Local Caching & Modals */

document.addEventListener('DOMContentLoaded', function() {
    const quizForm = document.getElementById('quiz-attempt-form');
    if (!quizForm) return;

    const attemptId = quizForm.dataset.attemptId;
    const timeLimitSeconds = parseInt(quizForm.dataset.timeLimitSeconds);
    let timeRemaining = parseInt(quizForm.dataset.timeRemaining);
    
    const questions = document.querySelectorAll('.question-container');
    const totalQuestions = questions.length;
    let currentIndex = 0;
    
    // SVG circle timer configuration
    const timerFill = document.querySelector('.timer-fill');
    const timerText = document.getElementById('timer-text');
    const timerCard = document.querySelector('.timer-container');
    const totalCircumference = 377; // 2 * pi * r (r=60)
    
    // Navigator boxes
    const navBoxes = document.querySelectorAll('.nav-box');
    
    // Modal controls
    const submitBtn = document.getElementById('submit-quiz-btn');
    const confirmModal = document.getElementById('submit-confirm-modal');
    const modalDesc = document.getElementById('modal-unanswered-desc');
    const modalCancel = document.getElementById('modal-cancel');
    const modalConfirm = document.getElementById('modal-confirm');
    
    // Pagination Controls
    const prevBtn = document.getElementById('prev-q-btn');
    const nextBtn = document.getElementById('next-q-btn');
    const skipBtn = document.getElementById('skip-q-btn');
    const indexTracker = document.getElementById('current-index-tracker');
    const progressFill = document.getElementById('quiz-progress-fill');

    // Initialize selections from sessionStorage
    restoreAnswers();
    updateNavigator();
    showQuestion(0);
    
    // Option Card click logic
    const optionCards = document.querySelectorAll('.option-card');
    optionCards.forEach(card => {
        card.addEventListener('click', function() {
            const container = this.closest('.question-container');
            const qId = container.dataset.questionId;
            const optionVal = this.dataset.option;
            
            // Unselect others
            container.querySelectorAll('.option-card').forEach(c => c.classList.remove('selected'));
            
            // Select this one
            this.classList.add('selected');
            const radio = this.querySelector('input[type="radio"]');
            if (radio) radio.checked = true;
            
            // Save selection to sessionStorage
            sessionStorage.setItem(`attempt_${attemptId}_q_${qId}`, optionVal);
            
            updateNavigator();
            updateProgressBar();
        });
    });

    // Pagination Click Listeners
    if (prevBtn) {
        prevBtn.addEventListener('click', function() {
            if (currentIndex > 0) {
                showQuestion(currentIndex - 1);
            }
        });
    }
    
    if (nextBtn) {
        nextBtn.addEventListener('click', function() {
            if (currentIndex < totalQuestions - 1) {
                showQuestion(currentIndex + 1);
            }
        });
    }
    
    if (skipBtn) {
        skipBtn.addEventListener('click', function() {
            const container = questions[currentIndex];
            const qId = container.dataset.questionId;
            
            // If nothing is selected, mark explicitly as skipped in session cache
            if (!sessionStorage.getItem(`attempt_${attemptId}_q_${qId}`)) {
                sessionStorage.setItem(`attempt_${attemptId}_q_${qId}`, 'skipped');
            }
            
            updateNavigator();
            if (currentIndex < totalQuestions - 1) {
                showQuestion(currentIndex + 1);
            } else {
                triggerSubmissionModal();
            }
        });
    }
    
    // Navigator click navigation
    navBoxes.forEach(box => {
        box.addEventListener('click', function() {
            const targetIndex = parseInt(this.dataset.index);
            showQuestion(targetIndex);
        });
    });
    
    // Form Submit Intercept
    if (submitBtn) {
        submitBtn.addEventListener('click', function(e) {
            e.preventDefault();
            triggerSubmissionModal();
        });
    }
    
    if (modalCancel) {
        modalCancel.addEventListener('click', function() {
            confirmModal.classList.remove('active');
        });
    }
    
    if (modalConfirm) {
        modalConfirm.addEventListener('click', function() {
            // Clear cache on submission
            clearAttemptCache();
            quizForm.submit();
        });
    }

    // Timer Logic
    if (timerFill && timerText) {
        // Initial SVG setup
        timerFill.style.strokeDasharray = totalCircumference;
        updateTimerDisplay();
        
        const timerInterval = setInterval(function() {
            timeRemaining--;
            
            if (timeRemaining <= 0) {
                clearInterval(timerInterval);
                timerText.innerText = "00:00";
                showToast("Time's up! Submitting your quiz automatically...", 'warning');
                setTimeout(() => {
                    clearAttemptCache();
                    quizForm.submit();
                }, 1000);
            } else {
                updateTimerDisplay();
            }
        }, 1000);
    }
    
    function updateTimerDisplay() {
        const minutes = Math.floor(timeRemaining / 60);
        const seconds = timeRemaining % 60;
        
        // Display Text
        const displayMin = minutes < 10 ? '0' + minutes : minutes;
        const displaySec = seconds < 10 ? '0' + seconds : seconds;
        timerText.innerText = `${displayMin}:${displaySec}`;
        
        // Stroke offset
        const fraction = timeRemaining / timeLimitSeconds;
        const offset = totalCircumference - (fraction * totalCircumference);
        timerFill.style.strokeDashoffset = offset;
        
        // Visual Urgency (< 20% remaining)
        if (fraction <= 0.2) {
            timerCard.classList.add('timer-urgent');
        } else {
            timerCard.classList.remove('timer-urgent');
        }
    }
    
    // Pagination layout updates
    function showQuestion(index) {
        questions[currentIndex].classList.remove('active');
        questions[index].classList.add('active');
        currentIndex = index;
        
        // Disable actions at limits
        if (prevBtn) prevBtn.disabled = (currentIndex === 0);
        if (nextBtn) nextBtn.style.display = (currentIndex === totalQuestions - 1) ? 'none' : 'inline-flex';
        if (skipBtn) skipBtn.style.display = (currentIndex === totalQuestions - 1) ? 'none' : 'inline-flex';
        if (submitBtn) submitBtn.style.display = (currentIndex === totalQuestions - 1) ? 'inline-flex' : 'none';
        
        // Index update
        if (indexTracker) {
            indexTracker.innerText = `Question ${currentIndex + 1} of ${totalQuestions}`;
        }
        
        // Focus state in navigator
        navBoxes.forEach(b => b.classList.remove('active'));
        if (navBoxes[currentIndex]) {
            navBoxes[currentIndex].classList.add('active');
        }
        
        updateProgressBar();
    }
    
    function updateProgressBar() {
        if (!progressFill) return;
        const answeredCount = Array.from(questions).filter(q => {
            const qId = q.dataset.questionId;
            const selection = sessionStorage.getItem(`attempt_${attemptId}_q_${qId}`);
            return selection && selection !== 'skipped';
        }).length;
        
        const pct = (answeredCount / totalQuestions) * 100;
        progressFill.style.width = `${pct}%`;
        
        const pctText = document.getElementById('quiz-progress-percent');
        if (pctText) {
            pctText.innerText = `${Math.round(pct)}% answered`;
        }
    }
    
    function updateNavigator() {
        questions.forEach((q, i) => {
            const qId = q.dataset.questionId;
            const val = sessionStorage.getItem(`attempt_${attemptId}_q_${qId}`);
            const box = navBoxes[i];
            if (!box) return;
            
            box.className = 'nav-box'; // reset
            if (i === currentIndex) {
                box.classList.add('active');
            }
            
            if (val && val !== 'skipped') {
                box.classList.add('answered');
            } else if (val === 'skipped') {
                box.classList.add('skipped');
            } else {
                box.classList.add('unanswered');
            }
        });
    }
    
    function triggerSubmissionModal() {
        // Count unanswered questions
        let unansweredCount = 0;
        questions.forEach(q => {
            const qId = q.dataset.questionId;
            const val = sessionStorage.getItem(`attempt_${attemptId}_q_${qId}`);
            if (!val || val === 'skipped') {
                unansweredCount++;
            }
        });
        
        if (unansweredCount > 0) {
            modalDesc.innerText = `You have left ${unansweredCount} of ${totalQuestions} questions unanswered. We recommend reviewing them before submitting.`;
        } else {
            modalDesc.innerText = "You have answered all questions. Are you ready to see your final score?";
        }
        
        confirmModal.classList.add('active');
    }
    
    function restoreAnswers() {
        questions.forEach(q => {
            const qId = q.dataset.questionId;
            const cachedVal = sessionStorage.getItem(`attempt_${attemptId}_q_${qId}`);
            if (cachedVal && cachedVal !== 'skipped') {
                const targetCard = q.querySelector(`.option-card[data-option="${cachedVal}"]`);
                if (targetCard) {
                    targetCard.classList.add('selected');
                    const radio = targetCard.querySelector('input[type="radio"]');
                    if (radio) radio.checked = true;
                }
            }
        });
    }
    
    function clearAttemptCache() {
        questions.forEach(q => {
            const qId = q.dataset.questionId;
            sessionStorage.removeItem(`attempt_${attemptId}_q_${qId}`);
        });
    }
});
