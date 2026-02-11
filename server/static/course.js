/**
 * Course Page JavaScript - Handles per-course offline caching and status display
 */

const RESULTS_KEY = 'pcv_results_queue';  // Shared across all courses

function getCacheKey(courseId) {
    return `quiz_cache_${courseId}`;
}

class OfflineManager {
    constructor(courseId) {
        this.courseId = courseId;
        this.cacheKey = getCacheKey(courseId);
        this.statusEl = document.getElementById('offline-status');
        this.downloadBtn = document.getElementById('download-btn');
        this.offlineInfo = document.getElementById('offline-info');
        this.cachedCountEl = document.getElementById('cached-count');
        this.lastSyncedEl = document.getElementById('last-synced');

        this.init();
    }

    init() {
        this.updateStatus();
        this.bindEvents();
        this.syncPendingResults();
    }

    bindEvents() {
        this.downloadBtn.addEventListener('click', () => this.downloadQuestions());
    }

    updateStatus() {
        const cache = this.getCache();

        if (cache && cache.questions) {
            // Count total questions
            let total = 0;
            for (const topicId in cache.questions) {
                total += cache.questions[topicId].length;
            }

            this.cachedCountEl.textContent = total;
            this.lastSyncedEl.textContent = this.formatDate(cache.generated);
            this.offlineInfo.classList.remove('hidden');

            this.statusEl.textContent = 'Offline Ready';
            this.statusEl.className = 'offline-status ready';

            this.downloadBtn.innerHTML = '<span class="download-icon">&#8635;</span> Update Cache';
        } else {
            this.offlineInfo.classList.add('hidden');
            this.statusEl.textContent = '';
        }

        // Check for pending results to sync (for this course)
        const pendingResults = this.getPendingResults();
        const courseResults = pendingResults.filter(r =>
            r.quiz_id && r.quiz_id.startsWith(this.courseId + '_')
        );
        if (courseResults.length > 0) {
            this.statusEl.textContent = `${courseResults.length} results pending sync`;
            this.statusEl.className = 'offline-status pending';
        }
    }

    formatDate(isoString) {
        if (!isoString) return 'Never';
        const date = new Date(isoString);
        const now = new Date();
        const diffMs = now - date;
        const diffMins = Math.floor(diffMs / 60000);
        const diffHours = Math.floor(diffMs / 3600000);
        const diffDays = Math.floor(diffMs / 86400000);

        if (diffMins < 1) return 'Just now';
        if (diffMins < 60) return `${diffMins}m ago`;
        if (diffHours < 24) return `${diffHours}h ago`;
        if (diffDays < 7) return `${diffDays}d ago`;
        return date.toLocaleDateString();
    }

    async downloadQuestions() {
        this.downloadBtn.disabled = true;
        this.downloadBtn.innerHTML = '<span class="download-icon">&#8987;</span> Downloading...';

        try {
            const response = await fetch(`/api/course/${this.courseId}/questions/all`);
            if (!response.ok) throw new Error('Failed to fetch questions');

            const data = await response.json();
            localStorage.setItem(this.cacheKey, JSON.stringify(data));

            this.downloadBtn.innerHTML = '<span class="download-icon">&#10003;</span> Downloaded!';
            setTimeout(() => {
                this.updateStatus();
                this.downloadBtn.disabled = false;
            }, 1500);
        } catch (error) {
            console.error('Download failed:', error);
            this.downloadBtn.innerHTML = '<span class="download-icon">&#10007;</span> Failed - Retry';
            this.downloadBtn.disabled = false;
        }
    }

    getCache() {
        try {
            const cached = localStorage.getItem(this.cacheKey);
            return cached ? JSON.parse(cached) : null;
        } catch (e) {
            return null;
        }
    }

    getPendingResults() {
        try {
            const results = localStorage.getItem(RESULTS_KEY);
            return results ? JSON.parse(results) : [];
        } catch (e) {
            return [];
        }
    }

    async syncPendingResults() {
        const pending = this.getPendingResults();
        if (pending.length === 0) return;

        const synced = [];
        for (const result of pending) {
            try {
                const response = await fetch('/quiz/submit', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(result)
                });
                if (response.ok) {
                    synced.push(result.quiz_id);
                }
            } catch (e) {
                // Network error, stop trying
                break;
            }
        }

        if (synced.length > 0) {
            // Remove synced results from queue
            const remaining = pending.filter(r => !synced.includes(r.quiz_id));
            localStorage.setItem(RESULTS_KEY, JSON.stringify(remaining));
            this.updateStatus();
        }
    }
}

// Initialize when page loads
document.addEventListener('DOMContentLoaded', () => {
    if (typeof COURSE_ID !== 'undefined') {
        new OfflineManager(COURSE_ID);
    }
});
