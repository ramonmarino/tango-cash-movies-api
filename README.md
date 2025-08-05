# Tango Cash Movies API

A FastAPI project to manage a movie database using SQLite and clean architecture principles.

## Features

- Full CRUD operations for movies
- Pydantic validation for data integrity
- Modular structure: routes, controllers, services, repositories, models
- Async database interactions with `databases` and SQLAlchemy
- Easy to extend and maintain

## Requirements

- Python 3.10+
- SQLite (comes bundled with Python)
- Dependencies listed in `requirements.txt`

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ramonmarino/tango-cash-movies-api.git
   cd tango-cash-movies-api
Create and activate a virtual environment:

bash

python -m venv .venv
source .venv/bin/activate  
# Linux/Mac
.venv\Scripts\activate     
# Windows

Install dependencies:
bash

pip install -r requirements.txt
Create the database and tables:

bash

python create_db.py
Run the FastAPI server:

bash

uvicorn main:app --reload
API Endpoints
Method	Endpoint	Description
GET	/movies/	List all movies
POST	/movies/	Add a new movie
GET	/movies/{id}	Get movie by ID
PUT	/movies/{id}	Update movie by ID
DELETE	/movies/{id}	Delete movie by ID

Validation
Movie names accept letters, numbers, and spaces only.

Name length between 1 and 100 characters.

License
MIT License © Ramon Marino
