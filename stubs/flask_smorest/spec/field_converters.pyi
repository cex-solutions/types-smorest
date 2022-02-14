from typing import Any

from flask_smorest.fields import Upload as Upload

def __getattr__(self, name: str) -> Any: ...  # type: ignore[misc]  # incomplete
def uploadfield2properties(self, field, **kwargs): ...
