/**
 * Quiz JavaScript - Handles quiz interaction and submission
 */

class Quiz {
    constructor(data) {
        this.data = data;
        this.currentIndex = 0;
        this.answers = {};
        this.questionTimes = {};
        this.questionStartTime = Date.now();
        this.quizStartTime = Date.now();

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
        // Convert LaTeX-style formulas to basic representation
        text = text.replace(/\$([^$]+)\$/g, '<code>$1</code>');
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

    async submit() {
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

        try {
            const response = await fetch(`/quiz/${this.data.id}/submit`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    answers: answers,
                    total_time_sec: totalTime
                })
            });

            const result = await response.json();

            if (result.success) {
                this.showResults(result);
            } else {
                alert('Failed to submit quiz. Please try again.');
                submitBtn.disabled = false;
                submitBtn.textContent = 'Submit';
            }
        } catch (error) {
            console.error('Submit error:', error);
            alert('Failed to submit quiz. Please check your connection.');
            submitBtn.disabled = false;
            submitBtn.textContent = 'Submit';
        }
    }

    showResults(result) {
        document.getElementById('final-score').textContent = result.score;
        document.getElementById('final-percentage').textContent = `${result.percentage}%`;
        document.getElementById('results-modal').classList.remove('hidden');
    }
}

// Initialize quiz when page loads
document.addEventListener('DOMContentLoaded', () => {
    if (typeof quizData !== 'undefined') {
        new Quiz(quizData);
    }
});
