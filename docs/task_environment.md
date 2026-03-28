# Task Environment

## 1. Rational objective
Identify and prioritize developer friction from workflow/repo-health signals.

## 2. PEAS
- Performance: ranking quality, explainability, actionable recommendations.
- Environment: synthetic engineering workflow dataset.
- Actuators: report generation and visualization.
- Sensors: cycle time, CI duration, flake counts, docs coverage, ownership and churn signals.

## 3. Environmental dimensions
Noisy socio-technical environment with changing constraints.

## 4. Problem formalization
Compute category subscores, aggregate friction score, and generate ranked action plan.

## 5. Architecture choice
FastAPI + SQLAlchemy + deterministic scoring/recommendation services.

## 6. Guardrails / workflow maturity
No hidden model authority and no confidential enterprise data.
