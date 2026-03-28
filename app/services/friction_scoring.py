from __future__ import annotations

from app.schemas import FrictionDataset


def compute_category_scores(dataset: FrictionDataset) -> dict[str, float]:
    churn_values = [float(item.get("churn", 0.0)) for item in dataset.churn_hotspots] or [0.0]
    churn_avg = sum(churn_values) / len(churn_values)

    scores = {
        "missing_docs": max(0.0, min(100.0, 100.0 - dataset.doc_coverage_pct)),
        "slow_ci": max(0.0, min(100.0, dataset.ci_duration_min_avg * 1.2)),
        "flaky_tests": max(0.0, min(100.0, dataset.flaky_test_count * 5.0)),
        "review_latency": max(0.0, min(100.0, dataset.review_latency_hours_avg * 2.0)),
        "ownership_gaps": max(0.0, min(100.0, dataset.ownership_gap_count * 15.0)),
        "rollback_hotspots": max(0.0, min(100.0, dataset.rollback_count_30d * 10.0)),
        "churn_hotspots": max(0.0, min(100.0, churn_avg * 10.0)),
    }
    return {key: round(value, 2) for key, value in scores.items()}


def rank_categories(category_scores: dict[str, float]) -> list[dict]:
    ranked = sorted(category_scores.items(), key=lambda item: item[1], reverse=True)
    return [{"category": name, "score": score} for name, score in ranked]


def overall_score(category_scores: dict[str, float]) -> float:
    return round(sum(category_scores.values()) / max(1, len(category_scores)), 2)
