# developer-friction-analyzer

Tool for deterministic developer-friction scoring over synthetic workflow and repo-health data.

## Overview
Computes friction subscores (docs, CI, flakes, review latency, ownership, rollbacks, churn) and outputs a prioritized improvement plan.

## Architecture
- Data loader: `app/services/data_loader.py`
- Scoring: `app/services/friction_scoring.py`
- Recommendations: `app/services/recommendations.py`
- Reporting: `app/services/friction_service.py`

## Local setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API
- `POST /api/analyze/sample/{dataset_id}`
- `GET /api/health`

## Heroku
`Procfile` and `runtime.txt` included.
