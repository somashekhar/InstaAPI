# Table of contents

## Development environment setup
- Install python version3.
- Install and configure VSCode and python plugin
- Setup virtual environment
```
    python3 --version
    python3 -m venv .venv
    source .venv/bin/activate
```


## FastAPI
- Install dependencies with pip
- Start FastAPI
- Path Operations (decorators, json)
- Path Operations Order (yes, it matters)
- Schema validation with Pydantic and Typing
- CRUD Operations
- Storing posts in an Array
- Creating posts
- Path order matters
- Changing response Status Codes
- Deleting Posts
- Updating Posts
- Automatic Documentation
- Python Packages
```
    pip install "fastapi[all]"
    pip freeze
    uvicorn main:app --reload (restart server with each change)
    uvicorn main:app (in production)
    uvicorn app.main:app --reload (inside app package)
```

## Postman
- Introduction to Postman
- HTTP Requests
- Postman collection and Saving requests
- Retrive one post
- Postman advanced features

## Databases
- Database Introduction
- Bring up database in docker compose
- Set up PostgreSQL Explorer plugin in VSCode
- Database schemas and tables
- Managing Postgres with PgAdmin GUI
- Your First SQL Query
- Filter results with WHERE
- SQL Operators
- IN 
- Pattern matching with LIKE
- Ordering results
- LIMIT & OFFSET
- Modifying Data

## Python + Raw SQL
- Setup App Database
- Connecting to database with Python
- Database CRUD

## ORMs
- ORM Introduction 
- SQLALCHEMY setup
- Adding Created at column
- Get All
- Create
- Get By ID
- Delete
- Update

## Pydantic Models
- Pydantic and ORM Models
- Pydantic Models Deep Dive
- Response Model

## Authentication and Users
- Creating Users Table
- User Registration Path Operation
- Hashing User Passwords
- Refactor Hashing Logic
- Get User by ID
- FastAPI Routers
- Router Prefix
- Router Tags
- JWT Token Basics
- Login Process
- Creating a token
- OAuth2 PasswordRequestForm
- Verify User is logged in
- Fixing Bugs
- Protecting Routes
- Test Expired Token
- Fetching User in protected routes

## Relationships
- SQL Relationship Basics
- Postgres Foreign Keys
- SQL Alchemy Foreign Keys
- Update Post Schema to include User
- Assigning Owner ID when creating new post
- Delete and Update only your own posts
- Only Retrieving Logged in User's posts
- Sqlalchemy Relationships
- Query Parameters
    ```
        {{URL}}posts?limit=10&skip=1&search=of%20post
    ```
- Clean up your main.py file
- Environment Variables
    ```
        export MY_DB_LOCAL="localhost:5432"
        printenv
        echo $MY_DB_LOCAL
    ```

## Voting/Like System
- Vote/Like Theory
- Votes Table
- Votes Sqlalchemy
- Votes Route
- SQL Joins
- Joins in Sqlalchemy
- Get One Post with Joins

## Database Migration with Alembic
- What is database migration tool
- Alembic setup
    ```
        alembic init alembic
        alembic revision -m "create posts table"
        alembic current
        alembic upgrade <revision id>
        alembic upgrade head
        alembic revision --autogenerate -m "message"
    ```
- Alembic first revision
- Alembic rollback database schema
- Alembic finishing up the rest of the schema
- Disable SqlAlchemy create engine

## Pre Deployment Checklist
- What is CQRS ?
- Git PreReqs
- Git Install
- Github

## Deployment Heroku
- Heroku Introduction
- Create Heroku Application
    ```
    heroku login
    heroku create insta-api-som
    git push heroku main

    ```
- Heroku Procfile
- Adding a postgres database
- Environment variables in Heroku
- Alembic Migrations on Heroku Postgres instance
- Pushing changes to production

## Deployment Ubuntu
- Create an Ubuntu VM
- Update packages
- Install Python
- Install Postgres and setup password
- Postgres Config
- Create new user and setup python environment
- Environment Variables
- Alembic migrations on production database
- Gunicorn
- Creating a Systemd service
- NGINX 
- Setting up Domain name
- SSL/HTTPS
- NGINX enable 
- Firewall 
- Pushing code changes to Production

## Docker
- Dockerfile
    ```
        docker build -t instaapi .
        docker image ls
    ```
- Docker Compose
- Postgres Container
- Bind Mounts
- Dockerhub
    ```
        docker login
        docker image tag instaapi-api sombidari/instaapi-api
        docker push sombidari/instaapi-api
    ```
- Production vs Deployment
    ```
        docker compose -f docker-compose-dev.yaml up -d
        docker compose -f docker-compose-prod.yaml up -d
        docker compose -f docker-compose-dev.yaml down
    ```


## Testing
- Testing Introduction
- Writing your first test
- The -s & -v flags
- Testing more functions
- Parametrize 
- Testing Classes 
- Fixtures 
- Combining Fixtures + Parametrize
- Testing Exceptions
- FastAPI TestClient
- Pytest flags
- Test create user
- Setup testing database
- Create & destroy database after each test
- More Fixtures to handle database interaction
- Trailing slashes in path 15:50:35
- Fixture scope 15:53:12
- Test user fixture 16:07:50
- Test/validate token 16:14:40
- Conftest.py 16:18:59
- Failed login test 16:22:09
- Get all posts test 16:28:28
- Posts fixture to create test posts 16:29:34
- Unauthorized Get Posts test 16:51:33
- Get one post test 16:55:16
- Create post test 16:59:19
- Delete post test 17:08:05
- Update post 17:15:17
- Voting tests 17:22:09


# References
- [[HTTP Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)]
- [API Documentation](https://www.postman.com/api-platform/api-documentation/)
- [FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [Postgres Data Types](https://www.postgresql.org/docs/current/datatype.html)
- [SQLAlchemy 1.4](https://docs.sqlalchemy.org/en/14/)
- [OAuth JWT](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
- [PostgreSQL](https://www.postgresqltutorial.com/index.html)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [CORS](https://fastapi.tiangolo.com/tutorial/cors/)
- [Heroku](https://devcenter.heroku.com/articles/heroku-cli)

# Video Reference
- [Python API Development - Comprehensive Course for Beginners](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=18483s)