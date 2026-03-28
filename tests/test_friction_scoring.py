from app.services.data_loader import DataLoader
from app.services.friction_scoring import compute_category_scores, overall_score, rank_categories


def test_category_ranking_shape() -> None:
    dataset = DataLoader().load("team_beta")
    scores = compute_category_scores(dataset)
    ranked = rank_categories(scores)
    assert ranked[0]["score"] >= ranked[-1]["score"]
    assert overall_score(scores) > 0
