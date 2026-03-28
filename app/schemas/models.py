from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class FrictionDataset(BaseModel):
    dataset_id: str
    pr_cycle_hours_avg: float
    ci_duration_min_avg: float
    flaky_test_count: int
    doc_coverage_pct: float
    ownership_gap_count: int
    review_latency_hours_avg: float
    rollback_count_30d: int
    churn_hotspots: list[dict] = Field(default_factory=list)


class FrictionReport(BaseModel):
    report_id: str
    dataset_id: str
    overall_friction_score: float
    ranked_categories: list[dict]
    top_friction_points: list[str]
    prioritized_recommendations: list[str]
    ownership_gaps: list[str]
    quick_wins: list[str]
    longer_fixes: list[str]
    summary_memo: str
    created_at: datetime


class FrictionResponse(BaseModel):
    report: FrictionReport
    dataset: FrictionDataset
