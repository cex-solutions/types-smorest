from typing import Any

from flask_smorest.fields import Upload as Upload

def __getattr__(name: str) -> Any: ...  # incomplete
