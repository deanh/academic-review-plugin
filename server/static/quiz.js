/**
 * Quiz JavaScript - Handles quiz interaction and submission
 */

const RESULTS_QUEUE_KEY = 'pcv_results_queue';

class Quiz {
    constructor(data) {
        this.data = data;
        this.allQuestions = [...data.questions]; // preserve full set
        this.currentIndex = 0;
        this.answers = {};
        this.questionTimes = {};
        this.questionStartTime = Date.now();
        this.quizStartTime = Date.now();

        // Mastery mode state
        this.masteryMode = false;
        this.correctAnswerMap = {};  // {questionId: correctAnswer}
        this.batchNumber = 0;
        this.masteryHistory = [];    // [{batch, score, total}]
        this.wrongQuestionIds = [];

        this.init();
    }

    init() {
        this.renderQuestion();
        this.updateProgress();
        this.startTimer();
        this.bindEvents();
    }

    bindEvents() {
        document.getElementById('prev-btn').addEventListener('click', () => this.prev());
        document.getElementById('next-btn').addEventListener('click', () => this.next());
        document.getElementById('submit-btn').addEventListener('click', () => this.submit());
    }

    renderQuestion() {
        const q = this.data.questions[this.currentIndex];
        const content = document.getElementById('quiz-content');

        let html = `
            <div class="question">
                <div class="question-topic">${q.topic || ''}</div>
                <div class="question-text">${this.formatText(q.question)}</div>
        `;

        if (q.type === 'multiple_choice') {
            html += '<div class="options">';
            q.options.forEach((opt, i) => {
                const selected = this.answers[q.id]?.selected === i ? 'selected' : '';
                html += `<button class="option ${selected}" data-index="${i}">${this.formatText(opt)}</button>`;
            });
            html += '</div>';
        } else if (q.type === 'true_false') {
            const trueSelected = this.answers[q.id]?.selected === true ? 'selected' : '';
            const falseSelected = this.answers[q.id]?.selected === false ? 'selected' : '';
            html += `
                <div class="tf-options">
                    <button class="option ${trueSelected}" data-value="true">True</button>
                    <button class="option ${falseSelected}" data-value="false">False</button>
                </div>
            `;
        } else if (q.type === 'short_answer') {
            const text = this.answers[q.id]?.text || '';
            html += `<textarea class="short-answer-input" placeholder="Type your answer...">${text}</textarea>`;
        }

        html += '</div>';
        content.innerHTML = html;

        // Bind option clicks
        if (q.type === 'multiple_choice') {
            content.querySelectorAll('.option').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    const index = parseInt(e.target.dataset.index);
                    this.selectOption(q.id, index);
                });
            });
        } else if (q.type === 'true_false') {
            content.querySelectorAll('.option').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    const value = e.target.dataset.value === 'true';
                    this.selectTF(q.id, value);
                });
            });
        } else if (q.type === 'short_answer') {
            const textarea = content.querySelector('.short-answer-input');
            textarea.addEventListener('input', (e) => {
                this.updateShortAnswer(q.id, e.target.value);
            });
            // Focus textarea
            textarea.focus();
        }

        // Record time for previous question
        this.recordQuestionTime();
        this.questionStartTime = Date.now();
    }

    formatText(text) {
        // Escape HTML but preserve basic formatting
        text = text.replace(/</g, '&lt;').replace(/>/g, '&gt;');

        // Render LaTeX math with KaTeX if available
        if (typeof katex !== 'undefined') {
            // Display math ($$...$$) - must come before inline
            text = text.replace(/\$\$([^$]+)\$\$/g, (match, latex) => {
                try {
                    return katex.renderToString(latex, { displayMode: true, throwOnError: false });
                } catch (e) {
                    return `<code>${latex}</code>`;
                }
            });
            // Inline math ($...$)
            text = text.replace(/\$([^$]+)\$/g, (match, latex) => {
                try {
                    return katex.renderToString(latex, { displayMode: false, throwOnError: false });
                } catch (e) {
                    return `<code>${latex}</code>`;
                }
            });
        } else {
            // Fallback if KaTeX not loaded
            text = text.replace(/\$\$([^$]+)\$\$/g, '<div class="math-display"><code>$1</code></div>');
            text = text.replace(/\$([^$]+)\$/g, '<code>$1</code>');
        }
        return text;
    }

    selectOption(questionId, index) {
        this.answers[questionId] = { selected: index };
        // Update UI
        document.querySelectorAll('.option').forEach((btn, i) => {
            btn.classList.toggle('selected', i === index);
        });
    }

    selectTF(questionId, value) {
        this.answers[questionId] = { selected: value };
        // Update UI
        document.querySelectorAll('.option').forEach(btn => {
            const btnValue = btn.dataset.value === 'true';
            btn.classList.toggle('selected', btnValue === value);
        });
    }

    updateShortAnswer(questionId, text) {
        this.answers[questionId] = { text: text };
    }

    recordQuestionTime() {
        const q = this.data.questions[this.currentIndex];
        if (q) {
            const elapsed = Math.round((Date.now() - this.questionStartTime) / 1000);
            this.questionTimes[q.id] = (this.questionTimes[q.id] || 0) + elapsed;
        }
    }

    updateProgress() {
        document.getElementById('progress').textContent =
            `${this.currentIndex + 1} / ${this.data.questions.length}`;

        const prevBtn = document.getElementById('prev-btn');
        const nextBtn = document.getElementById('next-btn');
        const submitBtn = document.getElementById('submit-btn');

        prevBtn.disabled = this.currentIndex === 0;

        const isLast = this.currentIndex === this.data.questions.length - 1;
        nextBtn.classList.toggle('hidden', isLast);
        submitBtn.classList.toggle('hidden', !isLast);
    }

    prev() {
        if (this.currentIndex > 0) {
            this.recordQuestionTime();
            this.currentIndex--;
            this.renderQuestion();
            this.updateProgress();
        }
    }

    next() {
        if (this.currentIndex < this.data.questions.length - 1) {
            this.recordQuestionTime();
            this.currentIndex++;
            this.renderQuestion();
            this.updateProgress();
        }
    }

    startTimer() {
        setInterval(() => {
            const elapsed = Math.floor((Date.now() - this.quizStartTime) / 1000);
            const mins = Math.floor(elapsed / 60);
            const secs = elapsed % 60;
            document.getElementById('timer').textContent =
                `${mins}:${secs.toString().padStart(2, '0')}`;
        }, 1000);
    }

    // Queue result to localStorage for later sync
    queueResultOffline(submitData) {
        try {
            const queue = JSON.parse(localStorage.getItem(RESULTS_QUEUE_KEY) || '[]');
            submitData.queued_at = new Date().toISOString();
            queue.push(submitData);
            localStorage.setItem(RESULTS_QUEUE_KEY, JSON.stringify(queue));
            return true;
        } catch (e) {
            console.error('Failed to queue result:', e);
            return false;
        }
    }

    async submit() {
        if (this.masteryMode) {
            return this.submitRetry();
        }
        this.recordQuestionTime();

        const totalTime = Math.round((Date.now() - this.quizStartTime) / 1000);

        // Build answers array
        const answers = this.data.questions.map(q => {
            const answer = this.answers[q.id] || {};
            return {
                question_id: q.id,
                selected: answer.selected,
                text: answer.text,
                time_spent_sec: this.questionTimes[q.id] || 0
            };
        });

        const submitBtn = document.getElementById('submit-btn');
        submitBtn.disabled = true;
        submitBtn.textContent = 'Submitting...';

        const submitData = {
            quiz_id: this.data.id,
            course: this.data.course,
            quiz_topic: this.data.topic,
            quiz_lecture: this.data.lecture,
            answers: answers,
            total_time_sec: totalTime
        };

        try {
            // Use new unified submit endpoint
            const response = await fetch('/quiz/submit', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(submitData)
            });

            const result = await response.json();

            if (result.success) {
                // Store per-question details for mastery retries
                if (result.details) {
                    this.wrongQuestionIds = [];
                    for (const d of result.details) {
                        if (!d.correct) {
                            this.correctAnswerMap[d.id] = d.correct_answer;
                            this.wrongQuestionIds.push(d.id);
                        }
                    }
                }
                this.masteryHistory.push({
                    batch: this.batchNumber,
                    score: result.score,
                    total: result.total
                });
                this.showResults(result);
            } else {
                throw new Error('Server returned failure');
            }
        } catch (error) {
            console.error('Submit error:', error);

            // Queue for offline sync
            if (this.queueResultOffline(submitData)) {
                const answered = answers.filter(a => a.selected !== undefined || a.text).length;
                this.showResults({
                    offline: true,
                    answered: answered,
                    total: this.data.questions.length
                });
            } else {
                alert('Failed to save quiz results. Please try again.');
                submitBtn.disabled = false;
                submitBtn.textContent = 'Submit';
            }
        }
    }

    showResults(result) {
        const modal = document.getElementById('results-modal');
        const scoreEl = document.getElementById('final-score');
        const percentEl = document.getElementById('final-percentage');
        const totalEl = document.getElementById('final-total');
        const retryBtn = document.getElementById('retry-btn');
        const titleEl = document.getElementById('results-title');
        const batchIndicator = document.getElementById('batch-indicator');
        const masterySummary = document.getElementById('mastery-summary');

        // Reset mastery UI
        retryBtn.classList.add('hidden');
        batchIndicator.classList.add('hidden');
        masterySummary.classList.add('hidden');
        modal.querySelector('.modal-content').classList.remove('mastery-complete');
        titleEl.textContent = 'Quiz Complete!';

        if (result.offline) {
            scoreEl.textContent = result.answered;
            totalEl.textContent = `/ ${result.total} answered`;
            percentEl.textContent = 'Saved offline';
            percentEl.classList.add('offline-notice');

            const queue = JSON.parse(localStorage.getItem(RESULTS_QUEUE_KEY) || '[]');
            if (queue.length > 1) {
                percentEl.textContent = `Saved offline (${queue.length} pending)`;
            }
        } else {
            scoreEl.textContent = result.score;
            totalEl.textContent = `/ ${result.total}`;
            percentEl.textContent = `${result.percentage}%`;
            percentEl.classList.remove('offline-notice');

            // Show batch indicator for retry batches
            if (this.batchNumber > 0) {
                batchIndicator.textContent = `Batch ${this.batchNumber + 1}`;
                batchIndicator.classList.remove('hidden');
                titleEl.textContent = 'Batch Results';
            }

            // Show retry button if there are wrong answers
            const wrongCount = this.wrongQuestionIds.length;
            if (wrongCount > 0) {
                retryBtn.textContent = `Retry Wrong Answers (${wrongCount})`;
                retryBtn.classList.remove('hidden');
            }
        }

        modal.classList.remove('hidden');
    }

    startRetry() {
        // Filter to only the wrong questions from the full set
        const wrongQuestions = this.allQuestions.filter(
            q => this.wrongQuestionIds.includes(q.id)
        );

        // Shuffle the wrong questions
        for (let i = wrongQuestions.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [wrongQuestions[i], wrongQuestions[j]] = [wrongQuestions[j], wrongQuestions[i]];
        }

        // Reset quiz state for retry batch
        this.data.questions = wrongQuestions;
        this.currentIndex = 0;
        this.answers = {};
        this.questionTimes = {};
        this.questionStartTime = Date.now();
        this.masteryMode = true;
        this.batchNumber++;

        // Hide modal, re-enable footer, render first question
        document.getElementById('results-modal').classList.add('hidden');

        const submitBtn = document.getElementById('submit-btn');
        submitBtn.disabled = false;
        submitBtn.textContent = 'Submit';

        this.renderQuestion();
        this.updateProgress();
    }

    submitRetry() {
        this.recordQuestionTime();

        let score = 0;
        const total = this.data.questions.length;
        this.wrongQuestionIds = [];

        for (const q of this.data.questions) {
            const answer = this.answers[q.id];
            const correctAnswer = this.correctAnswerMap[q.id];
            let isCorrect = false;

            if (q.type === 'multiple_choice') {
                isCorrect = answer?.selected === correctAnswer;
            } else if (q.type === 'true_false') {
                isCorrect = answer?.selected === correctAnswer;
            }

            if (isCorrect) {
                score++;
            } else {
                this.wrongQuestionIds.push(q.id);
            }
        }

        const percentage = total > 0 ? Math.round(score / total * 100) : 0;

        this.masteryHistory.push({
            batch: this.batchNumber,
            score: score,
            total: total
        });

        if (this.wrongQuestionIds.length === 0) {
            this.showMasteryComplete();
        } else {
            this.showResults({ score, total, percentage });
        }
    }

    showMasteryComplete() {
        const modal = document.getElementById('results-modal');
        const scoreEl = document.getElementById('final-score');
        const percentEl = document.getElementById('final-percentage');
        const totalEl = document.getElementById('final-total');
        const retryBtn = document.getElementById('retry-btn');
        const titleEl = document.getElementById('results-title');
        const batchIndicator = document.getElementById('batch-indicator');
        const masterySummary = document.getElementById('mastery-summary');

        titleEl.textContent = 'Mastery Complete!';
        scoreEl.textContent = this.allQuestions.length;
        totalEl.textContent = `/ ${this.allQuestions.length}`;
        percentEl.textContent = '100%';
        percentEl.classList.remove('offline-notice');
        retryBtn.classList.add('hidden');
        batchIndicator.classList.add('hidden');

        // Build batch history summary
        let summaryHtml = '<div class="mastery-history">';
        for (const entry of this.masteryHistory) {
            const label = entry.batch === 0 ? 'Initial' : `Batch ${entry.batch + 1}`;
            summaryHtml += `<div class="mastery-history-row"><span>${label}</span><span>${entry.score}/${entry.total}</span></div>`;
        }
        summaryHtml += '</div>';
        masterySummary.innerHTML = summaryHtml;
        masterySummary.classList.remove('hidden');

        modal.classList.remove('hidden');
        modal.querySelector('.modal-content').classList.add('mastery-complete');
    }
}

// Initialize quiz when page loads
document.addEventListener('DOMContentLoaded', () => {
    if (typeof quizData !== 'undefined') {
        window.quizInstance = new Quiz(quizData);
    }
});
