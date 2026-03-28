from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.repositories.report_repo import ReportRepository
from app.services.data_loader import DataLoader
from app.services.friction_service import FrictionService

router = APIRouter(prefix="/api", tags=["api"])


def _service(db: Session) -> FrictionService:
    return FrictionService(ReportRepository(db))


@router.get("/health")
def health() -> dict:
    return {"status": "ok"}


@router.post("/analyze/sample/{dataset_id}")
def analyze_sample(dataset_id: str, db: Session = Depends(get_db)) -> dict:
    dataset = DataLoader().load(dataset_id)
    return _service(db).analyze(dataset).model_dump(mode="json")
