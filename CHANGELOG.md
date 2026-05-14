# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-01-XX

### Added
- Initial release of Price Tracker & Alerter
- Multi-site scraping support (Amazon, Flipkart, BookDepository, Generic)
- Price history tracking with SQLite database
- Three alert types: absolute price, percentage drop, any drop
- Email notifications via SMTP with HTML templates
- Discord webhook notifications with rich embeds
- Automated price checking with APScheduler
- FastAPI REST API with auto-generated documentation
- React frontend with Tailwind CSS
- Interactive price charts with Recharts
- Dark mode support
- CLI tools for product management
- Anti-bot protection (rotating user agents, retry logic, exponential backoff)
- Database migrations with Alembic
- Unit and integration tests with pytest
- Comprehensive documentation

### Features
- **Backend**: Python 3.10-3.12, FastAPI, SQLAlchemy, APScheduler
- **Frontend**: React 18, Vite, Tailwind CSS, Recharts
- **Database**: SQLite with Alembic migrations
- **Notifications**: Email (SMTP) and Discord webhooks
- **Scraping**: BeautifulSoup4 with anti-bot measures
- **Testing**: pytest with coverage reporting

### Documentation
- README.md with comprehensive setup guide
- CONTRIBUTING.md for contributors
- API documentation at /docs endpoint
- CLI help commands
- Setup troubleshooting guide

## [Unreleased]

### Planned
- Docker support with docker-compose
- PostgreSQL/MySQL support
- Playwright integration for dynamic websites
- Telegram notifications
- Price prediction with ML
- Mobile app (React Native)
- Browser extension
- Bulk product import
- Export price history to CSV/Excel
- Advanced filtering and search
- User authentication and multi-user support
- Webhook support for custom integrations

---

## Version History

- **1.0.0** - Initial release with core features
