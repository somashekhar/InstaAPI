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

# References
- [[HTTP Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)]
- [API Documentation](https://www.postman.com/api-platform/api-documentation/)
- [FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [Postgres Data Types](https://www.postgresql.org/docs/current/datatype.html)
- [SQLAlchemy 1.4](https://docs.sqlalchemy.org/en/14/)

