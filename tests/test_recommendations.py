from app.services.recommendations import generate_recommendations


def test_recommendation_generation() -> None:
    scores = {
        "missing_docs": 60,
        "slow_ci": 70,
        "flaky_tests": 50,
        "review_latency": 55,
        "ownership_gaps": 45,
        "rollback_hotspots": 40,
        "churn_hotspots": 30,
    }
    recs = generate_recommendations(scores)
    assert recs["prioritized"]
    assert recs["quick_wins"]
