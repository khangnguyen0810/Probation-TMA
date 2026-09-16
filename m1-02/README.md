# M1-02 — FastAPI + Uvicorn

Goal: stand up a FastAPI app, understand what Uvicorn is doing under the hood, and touch the core building blocks (routing, validation, dependency injection, docs).

## Files in this repo

- `pyproject.toml` — adds `fastapi`, `uvicorn[standard]`, `pydantic`; dev group adds `pytest` + `httpx` for testing
- `main.py` — small app with path params, query params, request body validation, a response model, a dependency, and both sync/async endpoints
- `test_main.py` — tests using `TestClient` (in-process, no real server needed)

## Steps to do yourself

1. **Sync dependencies**
   `uv sync --group dev`

2. **Run the dev server**
   `uv run uvicorn main:app --reload`
   - `uvicorn` is the ASGI server that actually runs your app (FastAPI itself is just a framework — it needs a server to listen on a socket).
   - `main:app` means "in `main.py`, use the object named `app`".
   - `--reload` watches files and restarts the server on change (dev only — never use in production).

3. **Explore the interactive docs**
   Open `http://127.0.0.1:8000/docs` (Swagger UI) — FastAPI auto-generates this from your Pydantic models and type hints. Also check `/redoc` for the alternate doc UI.

4. **Try the endpoints manually**
   - `GET /health` — plain async endpoint
   - `POST /items` with body `{"name": "Mouse", "price": 9.99}` — creates an item, returns 201
   - `GET /items/1` — fetch it back
   - `GET /items/999` — see the 404 error handling
   - `POST /items` with a body missing `name` — see FastAPI's automatic 422 validation error

5. **Run the tests**
   `uv run pytest`

6. **Read the ASGI vs WSGI distinction**
   Research: what problem does ASGI solve that WSGI (used by Flask/Django classic) doesn't? (Hint: concurrency / async support.)

## Things worth checking with your mentor

- Whether this team runs Uvicorn directly in prod or behind Gunicorn (`gunicorn -k uvicorn.workers.UvicornWorker`) or behind something like Nginx
- What the team's convention is for splitting routes into routers (`APIRouter`) once the app grows past one file
- Whether they use `Depends()` for DB sessions/auth already, so I can look at a real example