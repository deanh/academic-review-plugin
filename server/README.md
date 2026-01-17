# Quiz Server Deployment

Flask-based quiz server for mobile-friendly academic quizzes.

## Server Setup (Digital Ocean)

### 1. Create directory structure

```bash
sudo mkdir -p /var/www/quizzes
sudo chown $USER:www-data /var/www/quizzes
cd /var/www/quizzes
```

### 2. Copy files to server

From your local machine:
```bash
rsync -avz server/ user@your-server:/var/www/quizzes/
```

### 3. Set up Python environment

```bash
cd /var/www/quizzes
python3 -m venv venv
./venv/bin/pip install flask
```

### 4. Create data directories

```bash
mkdir -p data results
chown www-data:www-data data results
chmod 775 data results
```

### 5. Set up logging

```bash
sudo mkdir -p /var/log/quiz-server
sudo chown www-data:www-data /var/log/quiz-server
```

### 6. Install systemd service

```bash
sudo cp deploy/quiz-server.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable quiz-server
sudo systemctl start quiz-server
```

### 7. Configure nginx

Add to your existing nginx config or create new:
```bash
# Option A: Add location block to existing site
sudo nano /etc/nginx/sites-available/default
# Add contents of deploy/nginx-quizzes.conf inside server { }

# Option B: Create standalone config
sudo cp deploy/nginx-quizzes.conf /etc/nginx/sites-available/quizzes
sudo ln -s /etc/nginx/sites-available/quizzes /etc/nginx/sites-enabled/
```

Test and reload:
```bash
sudo nginx -t
sudo systemctl reload nginx
```

## Local Setup

### Configure sync scripts

Edit `scripts/sync_quizzes.sh` and `scripts/sync_results.sh`:
```bash
SERVER_USER="your-username"
SERVER_HOST="your-server.com"
```

### Test the workflow

1. Generate a quiz (Claude will do this):
   ```bash
   # Quiz JSON saved to .cache/web-quizzes/
   ```

2. Sync to server:
   ```bash
   ./scripts/sync_quizzes.sh
   ```

3. Take quiz on phone:
   ```
   https://your-server.com/quizzes/
   ```

4. Sync results back:
   ```bash
   ./scripts/sync_results.sh
   ```

5. Review with Claude:
   ```
   /academic-review
   > Review my web quiz results
   ```

## Troubleshooting

### Check service status
```bash
sudo systemctl status quiz-server
sudo journalctl -u quiz-server -f
```

### Test Flask directly
```bash
cd /var/www/quizzes
./venv/bin/python server.py
# Visit http://server-ip:5000
```

### Check permissions
```bash
ls -la /var/www/quizzes/
ls -la /var/www/quizzes/data/
ls -la /var/www/quizzes/results/
```

## File Structure

```
/var/www/quizzes/
├── server.py           # Flask application
├── venv/               # Python virtual environment
├── templates/
│   ├── index.html      # Quiz list page
│   └── quiz.html       # Quiz taking page
├── static/
│   ├── style.css       # Mobile-friendly styles
│   └── quiz.js         # Quiz logic
├── data/               # Quiz JSON files (synced from local)
├── results/            # Result JSON files (synced to local)
└── deploy/
    ├── nginx-quizzes.conf
    └── quiz-server.service
```
