# Backend Setup Guide

## Technology Stack

- Python 3.9
- Poetry (dependency management)
- FastAPI (API framework)
- SQLAlchemy (ORM)
- PostgreSQL (database)

## Installation

1. Install Poetry:
   ```bash
   pip install poetry
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

## Development

Start development server:
```bash
poetry run python api/app.py
```

## Key Files

- `api/app.py`: Main application entry point
- `pyproject.toml`: Poetry configuration
- `requirements.txt`: Python dependencies
- `services/`: Core business logic
- `models/`: Database models

## Database Setup

1. Create PostgreSQL database
2. Set DATABASE_URL in .env file
3. Run migrations:
   ```bash
   poetry run alembic upgrade head
   ```

## Testing

Run tests:
```bash
poetry run pytest
