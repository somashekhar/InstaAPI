# InstaAPI

A RESTful API built with FastAPI for creating, managing, and interacting with social media posts

## Project Overview

InstaAPI is a robust backend service for a social media application, providing secure and efficient endpoints for user management, post operations, and social interactions. The API implements full authentication, comprehensive CRUD operations, data validation, and detailed API documentation.

## Features

- **User Management**
  - Registration with secure password hashing
  - Authentication using JWT tokens
  - User profile retrieval

- **Post Operations**
  - Create, read, update, and delete posts
  - Pagination and search functionality
  - Ownership validation for secured operations

- **Social Interactions**
  - Vote/like system for posts
  - Post metrics (vote count)

## Technical Stack

- **Backend**: [Python](https://www.python.org/) with [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: [PostgreSQL](https://www.postgresql.org/)
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
- **Migration**: [Alembic](https://alembic.sqlalchemy.org/)
- **Authentication**: JWT using [python-jose](https://python-jose.readthedocs.io/)
- **Containerization**: [Docker](https://www.docker.com/) and Docker Compose
- **Documentation**: Auto-generated with Swagger UI and ReDoc

## Getting Started

### Prerequisites

- Python 3.9+
- Docker and Docker Compose
- PostgreSQL 

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/InstaAPI.git
   cd InstaAPI
   ```

2. Set up environment variables:
   Create a `.env` file in the project root with the following variables:
   ```
   DATABASE_HOSTNAME=postgres
   DATABASE_PORT=5432
   DATABASE_NAME=InstaAPI
   DATABASE_USERNAME=yourusername
   DATABASE_PASSWORD=yourpassword
   SECRET_KEY=yoursecretkey
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=60
   ```

3. Run with Docker Compose (recommended):
   ```
   # For development
   docker compose -f docker-compose-dev.yaml up -d
   
   # For production
   docker compose -f docker-compose-prod.yaml up -d
   ```

4. Or set up a local development environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

5. Run database migrations:
   ```
   alembic upgrade head
   ```

## API Documentation

Once the server is running, access the interactive API documentation:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Development

### Database Migrations

```
# Create a new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

### Running Tests

```
pytest
```


## License

This project is licensed under the Apache License 2.0 - see the `LICENSE` file for details.
