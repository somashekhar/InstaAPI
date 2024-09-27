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

# References
- [[HTTP Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)]
- [API Documentation](https://www.postman.com/api-platform/api-documentation/)
- [FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

