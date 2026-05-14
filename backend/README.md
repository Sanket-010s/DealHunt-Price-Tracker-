# Price Tracker Backend

FastAPI-based backend for tracking product prices and sending alerts.

## Features

- 🔍 Multi-site scraping (Amazon, Flipkart, BookDepository, Generic)
- 📊 Price history tracking
- 🔔 Multiple alert types (absolute, percentage, any drop)
- 📧 Email notifications via SMTP
- 💬 Discord webhook notifications
- ⏰ Scheduled price checks
- 🛡️ Anti-bot protection (rotating user agents, retry logic, exponential backoff)
- 🗄️ SQLite database with SQLAlchemy ORM
- 🔄 Database migrations with Alembic
- 🧪 Unit and integration tests
- 🖥️ CLI tools for management

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # For development
```

2. Copy `.env.example` to `.env` and configure:
```bash
cp .env.example .env
```

3. Initialize database:
```bash
python scripts/init_db.py
```

4. Run the server:
```bash
python -m uvicorn app.main:app --reload
```

Or use the CLI:
```bash
python cli/tracker.py run
```

## CLI Usage

```bash
# Add a product
python cli/tracker.py add "https://amazon.com/product-url" --name "Product Name"

# List products
python cli/tracker.py list

# Check prices
python cli/tracker.py check --id 1

# View price history
python cli/tracker.py history 1 --days 30

# Remove product
python cli/tracker.py remove 1
```

## API Endpoints

- `GET /api/v1/health` - Health check
- `GET /api/v1/products` - List products
- `POST /api/v1/products` - Add product
- `GET /api/v1/products/{id}` - Get product with history
- `POST /api/v1/products/{id}/check` - Manually check price
- `GET /api/v1/alerts` - List alerts
- `POST /api/v1/alerts` - Create alert
- `GET /api/v1/notifications` - List notifications
- `POST /api/v1/jobs/check-all` - Trigger check for all products

## Testing

```bash
pytest
pytest --cov=app tests/
```

## Configuration

See `.env.example` for all configuration options.

Key settings:
- `SCHEDULER_INTERVAL_MINUTES` - How often to check prices
- `SCRAPER_RETRY_COUNT` - Number of retry attempts
- `EMAIL_ENABLED` / `DISCORD_ENABLED` - Enable/disable notification channels
