# Order Management API (FastAPI + Docker + CI)
A minimal backend demonstrating REST APIs, persistence, containers, and CI.
## Features
- Create, fetch, and list orders
- FastAPI with automatic docs at `/docs`
- SQLAlchemy + SQLite (override with `DATABASE_URL`)
- Dockerfile and docker-compose for local runs
- GitHub Actions CI (tests + Docker build)
## Run locally (Python)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open http://localhost:8000/docs
## Run with Docker
```bash
docker compose up --build
```
Open http://localhost:8000/docs
## API Examples
Create:
```bash
curl -X POST http://localhost:8000/orders -H "Content-Type: application/json" -d '{"item":"Brake Pads","quantity":2}'
```
Get by id:
```bash
curl http://localhost:8000/orders/1
```
List:
```bash
curl http://localhost:8000/orders
```
## Env
- `DATABASE_URL` (default: `sqlite:///./app.db`)
## Tests
```bash
pytest -q
```
