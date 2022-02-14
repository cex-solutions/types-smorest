from typing import Any

import marshmallow as ma

def __getattr__(name: str) -> Any: ...  # incomplete

class ErrorSchema(ma.Schema):
    code: Any
    status: Any
    message: Any
    errors: Any

class ErrorHandlerMixin:
    ERROR_SCHEMA: Any
    def handle_http_exception(self, error): ...
