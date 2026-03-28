from __future__ import annotations

import json
from pathlib import Path

from app.schemas import FrictionDataset


class DataLoader:
    def __init__(self, root: str = "data/datasets"):
        self.root = Path(root)

    def list_dataset_ids(self) -> list[str]:
        return sorted(path.stem for path in self.root.glob("*.json"))

    def load(self, dataset_id: str) -> FrictionDataset:
        payload = json.loads((self.root / f"{dataset_id}.json").read_text(encoding="utf-8"))
        return FrictionDataset.model_validate(payload)
