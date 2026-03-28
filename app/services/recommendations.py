from __future__ import annotations


def generate_recommendations(category_scores: dict[str, float]) -> dict[str, list[str]]:
    prioritized: list[str] = []
    quick_wins: list[str] = []
    longer_fixes: list[str] = []

    if category_scores["missing_docs"] > 40:
        prioritized.append("Establish docs checklist in PR template")
        quick_wins.append("Create docs ownership for top 3 services")

    if category_scores["slow_ci"] > 50:
        prioritized.append("Reduce CI runtime via test sharding")
        longer_fixes.append("Refactor integration test setup for parallelism")

    if category_scores["flaky_tests"] > 35:
        prioritized.append("Quarantine and stabilize high-flake tests")
        quick_wins.append("Introduce flaky test triage rotation")

    if category_scores["review_latency"] > 50:
        prioritized.append("Set review SLOs and rotate reviewer coverage")
        longer_fixes.append("Adjust team capacity for review bottlenecks")

    if category_scores["ownership_gaps"] > 30:
        prioritized.append("Close ownership gaps with explicit maintainers")
        quick_wins.append("Backfill ownership file for high-risk paths")

    if category_scores["rollback_hotspots"] > 30:
        prioritized.append("Investigate rollback-prone areas before feature expansion")
        longer_fixes.append("Redesign unstable deployment pathways")

    if not prioritized:
        prioritized.append("Maintain current process and monitor trend drift")

    return {
        "prioritized": prioritized,
        "quick_wins": quick_wins or ["Maintain existing quick-win practices"],
        "longer_fixes": longer_fixes or ["No major long-horizon fixes required currently"],
    }
