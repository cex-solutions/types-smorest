from typing import Any

import marshmallow as ma

def __getattr__(self, name: str) -> Any: ...  # type: ignore[misc]  # incomplete

class Upload(ma.fields.Field):
    format: Any
    def __init__(self, format: str = ..., **kwargs) -> None: ...
