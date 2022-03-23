from builtins import type
from typing import Any

import marshmallow as ma
from werkzeug.exceptions import HTTPException

class ErrorSchema(ma.Schema):
    code: int
    status: str
    message: str
    errors: dict[str, Any]

class ErrorHandlerMixin:
    ERROR_SCHEMA: type[ErrorSchema]

    def handle_http_exception(self, error: HTTPException): ...
