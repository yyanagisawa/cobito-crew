from __future__ import annotations

from pathlib import Path


def load_phase0_template(repo_root: Path) -> str:
    template_path = repo_root / "docs" / "advances" / "templates" / "phase0.md"
    return template_path.read_text(encoding="utf-8")
