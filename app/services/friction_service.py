from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

from app.repositories.report_repo import ReportRepository
from app.schemas import FrictionDataset, FrictionReport, FrictionResponse
from app.services.friction_scoring import compute_category_scores, overall_score, rank_categories
from app.services.recommendations import generate_recommendations
from app.services.reporting import build_summary


class FrictionService:
    def __init__(self, repo: ReportRepository):
        self.repo = repo

    def analyze(self, dataset: FrictionDataset) -> FrictionResponse:
        category_scores = compute_category_scores(dataset)
        ranked = rank_categories(category_scores)
        overall = overall_score(category_scores)

        top_points = [f"{item['category']} ({item['score']})" for item in ranked[:3]]
        ownership_gaps = [
            item.get("path", "unknown")
            for item in dataset.churn_hotspots
            if not bool(item.get("owner_known", True))
        ]
        recs = generate_recommendations(category_scores)

        report = FrictionReport(
            report_id=f"friction_{uuid4().hex[:10]}",
            dataset_id=dataset.dataset_id,
            overall_friction_score=overall,
            ranked_categories=ranked,
            top_friction_points=top_points,
            prioritized_recommendations=recs["prioritized"],
            ownership_gaps=ownership_gaps,
            quick_wins=recs["quick_wins"],
            longer_fixes=recs["longer_fixes"],
            summary_memo=build_summary(dataset.dataset_id, overall, top_points),
            created_at=datetime.now(timezone.utc),
        )

        response = FrictionResponse(report=report, dataset=dataset)
        self.repo.save(report.report_id, dataset.dataset_id, response.model_dump_json())
        return response

    def latest_for_dataset(self, dataset_id: str) -> FrictionResponse | None:
        payload = self.repo.latest_for_dataset(dataset_id)
        return FrictionResponse.model_validate(payload) if payload else None

    def history(self) -> list[FrictionResponse]:
        return [FrictionResponse.model_validate(item) for item in self.repo.list_recent()]
