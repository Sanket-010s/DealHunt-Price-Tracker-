# Project Structure Documentation

## Overview

This document explains the organization and purpose of each directory and file in the Price Tracker & Alerter project.

---

## Root Directory

```
price-tracker/
├── backend/              # Python FastAPI backend
├── frontend/             # React frontend
├── README.md            # Main project documentation
├── CONTRIBUTING.md      # Contribution guidelines
├── CHANGELOG.md         # Version history
├── LICENSE              # MIT License
├── INSTALL.md           # Installation guide
└── .gitignore          # Git ignore rules
```

---

## Backend Structure

### `/backend/app/` - Main Application

#### `/app/core/` - Core Business Logic
- `scraper.py` - Main scraping engine with retry logic
- `scheduler.py` - APScheduler for automated price checks
- `comparator.py` - Alert comparison logic
- `price_parser.py` - Price extraction and parsing utilities
- `anti_bot.py` - Anti-bot protection (user agents, backoff)

#### `/app/scrapers/` - Site-Specific Scrapers
- `base.py` - Base scraper class (abstract)
- `amazon.py` - Amazon scraper implementation
- `flipkart.py` - Flipkart scraper implementation
- `bookdepository.py` - BookDepository scraper
- `generic.py` - Generic scraper for other sites
- `__init__.py` - Scraper factory pattern

#### `/app/alerts/` - Notification System
- `base.py` - Base alerter class (abstract)
- `email_alerter.py` - SMTP email notifications
- `discord_alerter.py` - Discord webhook notifications
- `alert_manager.py` - Coordinates all alerters

#### `/app/db/` - Database Layer
- `base.py` - SQLAlchemy engine and session
- `models.py` - Database models (Product, PriceHistory, Alert, Notification)
- `crud.py` - CRUD operations
- `migrations/` - Alembic migration files

#### `/app/api/v1/` - REST API Endpoints
- `products.py` - Product CRUD endpoints
- `alerts.py` - Alert management endpoints
- `notifications.py` - Notification history endpoints
- `jobs.py` - Scheduler control endpoints
- `health.py` - Health check endpoint

#### `/app/schemas/` - Pydantic Schemas
- `product.py` - Product request/response models
- `alert.py` - Alert request/response models
- `notification.py` - Notification response models
- `common.py` - Shared schemas

#### `/app/utils/` - Utilities
- `logger.py` - Logging configuration
- `validators.py` - URL and email validation
- `helpers.py` - Helper functions (formatting, calculations)

#### `/app/templates/` - Email Templates
- `email_alert.html` - HTML email template
- `email_alert.txt` - Plain text email template

#### Root App Files
- `main.py` - FastAPI application entry point
- `config.py` - Configuration management (Pydantic Settings)
- `dependencies.py` - Dependency injection

---

### `/backend/cli/` - Command-Line Interface

#### `/cli/commands/` - CLI Commands
- `add.py` - Add product command
- `list.py` - List products command
- `remove.py` - Remove product command
- `check.py` - Check prices command
- `history.py` - View price history command
- `run.py` - Run server command

#### Root CLI Files
- `tracker.py` - Main CLI entry point (argparse)
- `utils.py` - CLI utilities (table formatting)

---

### `/backend/tests/` - Test Suite

#### `/tests/unit/` - Unit Tests
- `test_price_parser.py` - Price parsing tests
- `test_comparator.py` - Alert comparison tests
- `test_scrapers.py` - Scraper tests (mocked)
- `test_alert_manager.py` - Alert manager tests

#### `/tests/integration/` - Integration Tests
- `test_api.py` - API endpoint tests
- `test_alert_flow.py` - End-to-end alert flow
- `test_scrape_flow.py` - End-to-end scraping flow

#### `/tests/fixtures/` - Test Fixtures
- `sample_html/` - Sample HTML files for testing
- `mock_responses.json` - Mock API responses

#### Root Test Files
- `conftest.py` - Pytest configuration and fixtures

---

### `/backend/scripts/` - Utility Scripts
- `init_db.py` - Initialize database tables
- `seed_data.py` - Seed sample data
- `export_history.py` - Export price history (future)
- `proxy_validator.py` - Validate proxy list (future)

---

### `/backend/docs/` - Documentation
- `SETUP.md` - Detailed setup guide
- `API.md` - Complete API documentation
- `DEPLOYMENT.md` - Deployment guide (future)
- `CONTRIBUTING.md` - Contribution guidelines (future)

---

### `/backend/data/` - Runtime Data
- `tracker.db` - SQLite database
- `logs/tracker.log` - Application logs
- `proxies.txt` - Proxy list (optional)

---

### Backend Root Files
- `requirements.txt` - Production dependencies
- `requirements-dev.txt` - Development dependencies
- `pytest.ini` - Pytest configuration
- `alembic.ini` - Alembic migration configuration
- `.env` - Environment variables (not in git)
- `.env.example` - Environment template
- `.gitignore` - Git ignore rules
- `README.md` - Backend documentation
- `check_python.py` - Python version checker

---

## Frontend Structure

### `/frontend/src/` - Source Code

#### `/src/components/` - Reusable Components
- `ProductCard.jsx` - Product card display
- `ProductList.jsx` - Product list container
- `PriceChart.jsx` - Price history chart (Recharts)
- `AddProductModal.jsx` - Add product modal form
- `AlertBadge.jsx` - Alert type badge
- `NotificationLog.jsx` - Notification history display

#### `/src/pages/` - Route Pages
- `Dashboard.jsx` - Main dashboard page
- `ProductDetail.jsx` - Product detail with chart
- `Alerts.jsx` - Alert management page
- `Notifications.jsx` - Notification history page

#### `/src/services/` - API Clients
- `api.js` - Axios instance configuration
- `products.js` - Product API calls
- `alerts.js` - Alert API calls
- `notifications.js` - Notification API calls

#### `/src/hooks/` - Custom React Hooks
- `useProducts.js` - Product data fetching hook
- `usePriceHistory.js` - Price history fetching hook

#### `/src/utils/` - Utilities
- `constants.js` - Constants (API URL, alert types)
- `formatters.js` - Formatting functions (price, date)

#### `/src/styles/` - Styles
- `index.css` - Global styles with Tailwind directives

#### Root Source Files
- `App.jsx` - Main app component with routing
- `main.jsx` - React entry point

---

### `/frontend/public/` - Static Assets
- `favicon.ico` - Favicon

---

### Frontend Root Files
- `package.json` - NPM dependencies and scripts
- `vite.config.js` - Vite configuration
- `tailwind.config.js` - Tailwind CSS configuration
- `postcss.config.js` - PostCSS configuration
- `index.html` - HTML entry point
- `.gitignore` - Git ignore rules

---

## Design Patterns Used

### Backend
1. **Factory Pattern** - Scraper selection based on URL
2. **Strategy Pattern** - Different alert types
3. **Repository Pattern** - CRUD operations
4. **Dependency Injection** - FastAPI dependencies
5. **Template Method** - Base scraper class

### Frontend
1. **Container/Presentational** - Smart/dumb components
2. **Custom Hooks** - Reusable logic
3. **Service Layer** - API abstraction
4. **Composition** - Component composition

---

## Key Principles

### Separation of Concerns
- Business logic separated from API layer
- Database operations isolated in CRUD
- Scrapers are pluggable and independent

### Scalability
- Easy to add new scrapers
- Easy to add new alert channels
- Easy to add new API endpoints

### Maintainability
- Clear folder structure
- Consistent naming conventions
- Comprehensive documentation

### Testability
- Unit tests for core logic
- Integration tests for API
- Mock fixtures for external dependencies

---

## Adding New Features

### New Scraper
1. Create `app/scrapers/newsite.py`
2. Extend `BaseScraper`
3. Implement `scrape()` method
4. Register in `scrapers/__init__.py`
5. Add tests in `tests/unit/test_scrapers.py`

### New Alert Channel
1. Create `app/alerts/newalerter.py`
2. Extend `BaseAlerter`
3. Implement `send_alert()` method
4. Register in `alert_manager.py`
5. Add configuration in `config.py`

### New API Endpoint
1. Create route in `app/api/v1/newroute.py`
2. Define Pydantic schemas in `app/schemas/`
3. Add CRUD operations in `app/db/crud.py`
4. Register router in `app/api/v1/__init__.py`
5. Add tests in `tests/integration/test_api.py`

### New Frontend Page
1. Create component in `src/pages/NewPage.jsx`
2. Add route in `src/App.jsx`
3. Create API service in `src/services/`
4. Add custom hook if needed in `src/hooks/`

---

## Best Practices

### Backend
- Use type hints everywhere
- Write docstrings for functions
- Handle exceptions gracefully
- Log important events
- Validate input with Pydantic

### Frontend
- Use functional components
- Extract reusable logic to hooks
- Keep components small and focused
- Use constants for magic values
- Handle loading and error states

### Database
- Use migrations for schema changes
- Index frequently queried columns
- Use relationships properly
- Avoid N+1 queries

### Testing
- Test business logic thoroughly
- Mock external dependencies
- Test edge cases
- Maintain high coverage

---

This structure follows industry best practices and is designed for scalability, maintainability, and ease of contribution.
