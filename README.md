# Backend Demo

## What is this API?

Campaign Analytics API is a modular FastAPI backend demonstrating clean architecture, transactional integrity, and scalable service design.

---

## Tech Stack

- FastAPI  
- SQLAlchemy  
- PostgreSQL  
- Alembic  
- Docker  

---

## Architecture Overview

This project follows a layered, feature based architecture:

- **Feature-based modular design** (e.g., `advertisers/`)
- **Thin routers** responsible only for HTTP handling
- **Service layer** containing business logic

---

## How to Run

### Local

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

### Docker

 docker compose up --build


## API Endpoints

POST /advertisers
GET /advertisers

