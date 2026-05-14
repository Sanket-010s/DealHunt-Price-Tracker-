# Setup Guide

## Prerequisites

**Important:** This project requires **Python 3.10, 3.11, or 3.12**. Python 3.14 is too new and lacks pre-built wheels for some dependencies.

### Option 1: Install Python 3.12 (Recommended)

Download and install Python 3.12 from [python.org](https://www.python.org/downloads/)

### Option 2: Use Python 3.11 or 3.10

If you have Python 3.11 or 3.10 installed, use that version.

## Backend Setup

### Step 1: Create Virtual Environment

```bash
cd backend

# Create virtual environment with Python 3.12
python3.12 -m venv venv

# Or if python3.12 is your default:
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On Linux/Mac:
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 3: Configure Environment

```bash
# Copy example environment file
copy .env.example .env

# Edit .env with your settings (use notepad or any text editor)
notepad .env
```

### Step 4: Initialize Database

```bash
python scripts/init_db.py
```

### Step 5: Run the Server

```bash
# Using uvicorn directly
python -m uvicorn app.main:app --reload

# Or using the CLI
python cli/tracker.py run
```

The API will be available at:
- API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Frontend Setup

### Step 1: Install Node.js

Download and install Node.js 18+ from [nodejs.org](https://nodejs.org/)

### Step 2: Install Dependencies

```bash
cd frontend
npm install
```

### Step 3: Run Development Server

```bash
npm run dev
```

The frontend will be available at: http://localhost:5173

## Troubleshooting

### Issue: "Failed building wheel for pydantic-core"

**Solution:** You're using Python 3.14 which is too new. Install Python 3.10, 3.11, or 3.12 and create a new virtual environment.

### Issue: "Module not found" errors

**Solution:** Make sure you're in the virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Issue: Database errors

**Solution:** Delete the database and reinitialize:
```bash
# Delete database
del data\tracker.db  # Windows
rm data/tracker.db   # Linux/Mac

# Reinitialize
python scripts/init_db.py
```

### Issue: SMTP/Email not working

**Solution:** 
1. Use an app-specific password (not your regular email password)
2. For Gmail: Enable 2FA and create an app password at https://myaccount.google.com/apppasswords
3. Set `EMAIL_ENABLED=false` in .env to disable email notifications

### Issue: Port already in use

**Solution:** Change the port in .env:
```env
API_PORT=8001  # Change from 8000
```

## Testing

```bash
cd backend

# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/unit/test_price_parser.py
```

## CLI Usage Examples

```bash
# Add a product
python cli/tracker.py add "https://www.amazon.com/dp/B08N5WRWNW" --name "Product Name"

# List all products
python cli/tracker.py list

# List only active products
python cli/tracker.py list --active-only

# Check price for specific product
python cli/tracker.py check --id 1

# Check all products
python cli/tracker.py check

# View price history
python cli/tracker.py history 1 --days 30

# Remove a product
python cli/tracker.py remove 1
```

## Production Deployment

### Backend

```bash
# Install dependencies
pip install -r requirements.txt

# Initialize database
python scripts/init_db.py

# Run with gunicorn (install first: pip install gunicorn)
gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Frontend

```bash
# Build for production
npm run build

# The dist/ folder can be served with any static file server
# Example with Python:
cd dist
python -m http.server 5173

# Or with nginx, Apache, etc.
```

## Environment Variables Reference

### Database
- `DATABASE_URL` - SQLite database path

### Scraper
- `SCRAPER_TIMEOUT` - Request timeout in seconds (default: 30)
- `SCRAPER_RETRY_COUNT` - Number of retry attempts (default: 3)
- `SCRAPER_DELAY` - Delay between retries in seconds (default: 2)

### Scheduler
- `SCHEDULER_INTERVAL_MINUTES` - How often to check prices (default: 60)

### Email
- `SMTP_HOST` - SMTP server hostname
- `SMTP_PORT` - SMTP server port (usually 587)
- `SMTP_USER` - Email address
- `SMTP_PASSWORD` - Email password or app password
- `SMTP_FROM` - From email address
- `EMAIL_ENABLED` - Enable/disable email notifications (true/false)

### Discord
- `DISCORD_WEBHOOK_URL` - Discord webhook URL
- `DISCORD_ENABLED` - Enable/disable Discord notifications (true/false)

### API
- `API_HOST` - API host (default: 0.0.0.0)
- `API_PORT` - API port (default: 8000)
- `CORS_ORIGINS` - Comma-separated list of allowed origins

### Logging
- `LOG_LEVEL` - Logging level (DEBUG, INFO, WARNING, ERROR)
- `LOG_FILE` - Log file path
