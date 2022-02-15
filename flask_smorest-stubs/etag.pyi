from typing import Any

from .exceptions import NotModified as NotModified
from .exceptions import PreconditionFailed as PreconditionFailed
from .exceptions import PreconditionRequired as PreconditionRequired
from .utils import deepupdate as deepupdate
from .utils import get_appcontext as get_appcontext

def __getattr__(name: str) -> Any: ...  # incomplete

IF_NONE_MATCH_HEADER: Any
IF_MATCH_HEADER: Any
ETAG_HEADER: Any

class EtagMixin:
    METHODS_CHECKING_NOT_MODIFIED: Any
    METHODS_NEEDING_CHECK_ETAG: Any
    METHODS_ALLOWING_SET_ETAG: Any
    ETAG_INCLUDE_HEADERS: Any
    def etag(self, etag_schema: Any | None = ...): ...
    def check_etag(self, etag_data, etag_schema: Any | None = ...) -> None: ...
    def set_etag(self, etag_data, etag_schema: Any | None = ...) -> None: ...
