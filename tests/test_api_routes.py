
def test_health(client) -> None:
    response = client.get("/api/health")
    assert response.status_code == 200


def test_analyze_sample(client) -> None:
    response = client.post("/api/analyze/sample/team_alpha")
    assert response.status_code == 200
    assert "overall_friction_score" in response.json()["report"]


def test_web_routes(client) -> None:
    assert client.get("/").status_code == 200
    assert client.get("/report/team_alpha").status_code == 200
