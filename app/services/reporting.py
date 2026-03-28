from __future__ import annotations


def build_summary(dataset_id: str, overall: float, top_points: list[str]) -> str:
    top = "; ".join(top_points) if top_points else "No major friction hotspots"
    return f"Dataset {dataset_id} friction score is {overall}. Top drivers: {top}."
