# Audio Analysis Service

Upload audio files, analyze them in a background worker (tempo, beats, spectral features, energy), and serve the results to a browser visualizer.

> **Status:** Week 1 — FastAPI skeleton. See the roadmap below.

## Tech stack (planned)

| Layer | Choice |
|---|---|
| API | Python, FastAPI |
| Database | PostgreSQL |
| File storage | AWS S3 (presigned uploads) |
| Background jobs | Queue (e.g. SQS) + Python worker |
| Front end | React + TypeScript |
| Infra | Docker, GitHub Actions CI, AWS |

## Project layout

```
app/
  main.py            # create_app() factory, registers routers
  core/config.py     # settings from environment variables / .env
  api/router.py      # collects versioned (/api/v1) routes
  api/routes/        # one module per feature (health, uploads, tracks, ...)
tests/               # pytest tests, using FastAPI's in-memory TestClient
```

## Running locally

Requires Python 3.11+.

**Windows (PowerShell)**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
copy .env.example .env
uvicorn app.main:app --reload
```

**macOS / Linux**

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
uvicorn app.main:app --reload
```

Then open:

- http://127.0.0.1:8000/health — health check
- http://127.0.0.1:8000/docs — interactive API docs (Swagger UI)

## Tests and linting

```bash
pytest
ruff check .
```

## Roadmap

- [x] FastAPI skeleton, config, health check, first tests
- [ ] PostgreSQL via Docker Compose
- [ ] GitHub Actions CI (lint + tests on every PR)
- [ ] Data model, migrations, user auth
- [ ] Upload flow: presigned URL to S3
- [ ] Job queue + analysis worker
- [ ] React + TypeScript front end with visualizer
- [ ] AWS deployment

## Design decisions

Recorded as the project grows, so the reasoning behind each choice is easy to find.

- **App factory (`create_app`)** — tests build a fresh app instance instead of sharing global state.
- **Unversioned `/health`, versioned `/api/v1`** — infrastructure checks stay stable while the public API can evolve.
- **Settings from environment variables** — the same code runs locally, in CI, and on AWS; secrets never live in the repo.
