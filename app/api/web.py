from __future__ import annotations

from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.db import get_db
from app.repositories.report_repo import ReportRepository
from app.services.data_loader import DataLoader
from app.services.friction_service import FrictionService

router = APIRouter(tags=["web"])
templates = Jinja2Templates(directory="app/templates")


def _service(db: Session) -> FrictionService:
    return FrictionService(ReportRepository(db))


@router.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    loader = DataLoader()
    rows = []
    service = _service(db)
    for dataset_id in loader.list_dataset_ids():
        latest = service.latest_for_dataset(dataset_id)
        rows.append({"dataset_id": dataset_id, "report": latest.report if latest else None})
    return templates.TemplateResponse("index.html", {"request": request, "rows": rows})


@router.get("/report/{dataset_id}")
def detail(dataset_id: str, request: Request, db: Session = Depends(get_db)):
    loader = DataLoader()
    dataset = loader.load(dataset_id)
    service = _service(db)
    item = service.latest_for_dataset(dataset_id)
    if not item:
        item = service.analyze(dataset)
    return templates.TemplateResponse("detail.html", {"request": request, "item": item})
