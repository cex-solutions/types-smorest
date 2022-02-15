from typing import Any

from apispec import BasePlugin  # type: ignore[import] # noqa: 723

def __getattr__(name: str) -> Any: ...  # incomplete
