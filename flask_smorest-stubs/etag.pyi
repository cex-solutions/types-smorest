from typing import Any

from .exceptions import NotModified as NotModified
from .exceptions import PreconditionFailed as PreconditionFailed
from .exceptions import PreconditionRequired as PreconditionRequired
from .utils import deepupdate as deepupdate
from .utils import get_appcontext as get_appcontext

def __getattr__(name: str) -> Any: ...  # incomplete
