# Contributing to Price Tracker & Alerter

Thank you for considering contributing to this project! 🎉

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/yourusername/price-tracker/issues)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Python/Node.js version
   - Error messages/logs

### Suggesting Features

1. Open an issue with the `enhancement` label
2. Describe the feature and its use case
3. Explain why it would be valuable

### Pull Requests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Write/update tests
5. Run tests: `pytest`
6. Commit with clear messages: `git commit -m "Add feature: description"`
7. Push: `git push origin feature/your-feature`
8. Open a Pull Request

## Development Setup

```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Frontend
cd frontend
npm install
```

## Code Style

### Python (Backend)
- Follow PEP 8
- Use type hints
- Write docstrings
- Maximum line length: 100 characters

### JavaScript (Frontend)
- Use ES6+ features
- Follow React best practices
- Use functional components with hooks

## Testing

```bash
# Backend tests
cd backend
pytest
pytest --cov=app tests/

# Frontend tests (when added)
cd frontend
npm test
```

## Adding New Scrapers

1. Create `backend/app/scrapers/yoursite.py`
2. Extend `BaseScraper` class
3. Implement `scrape()` method
4. Add tests in `tests/unit/test_scrapers.py`
5. Register in `scrapers/__init__.py`

Example:
```python
from app.scrapers.base import BaseScraper, ScraperResult

class YourSiteScraper(BaseScraper):
    def scrape(self) -> Optional[ScraperResult]:
        html = self.fetch_html()
        if not html:
            return None
        
        soup = self.parse_html(html)
        name = soup.select_one('.product-name').get_text()
        price = parse_price(soup.select_one('.price').get_text())
        
        return ScraperResult(name=name, price=price)
```

## Commit Message Guidelines

- Use present tense: "Add feature" not "Added feature"
- Use imperative mood: "Move cursor to..." not "Moves cursor to..."
- Limit first line to 72 characters
- Reference issues: "Fix #123"

Examples:
```
Add Amazon scraper support
Fix price parsing for EUR currency
Update documentation for API endpoints
Refactor alert comparison logic
```

## Questions?

Feel free to open an issue or reach out to the maintainers.

Thank you for contributing! 🚀
