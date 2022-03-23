from typing import Any, Optional

import marshmallow as ma
from werkzeug.exceptions import HTTPException

class ErrorSchema(ma.Schema):
    code: int
    status: str
    message: str
    errors: dict[str, Any]

class ErrorHandlerMixin:
    ERROR_SCHEMA: type[ErrorSchema]

    def handle_http_exception(self, error: HTTPException) -> tuple[dict[str, Any], Optional[int], dict[str, Any]]: ...
