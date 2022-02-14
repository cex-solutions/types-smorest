from typing import Any

import werkzeug.exceptions as wexc

def __getattr__(name: str) -> Any: ...  # incomplete

class FlaskSmorestError(Exception): ...
class MissingAPIParameterError(FlaskSmorestError): ...

class NotModified(wexc.HTTPException, FlaskSmorestError):
    code: int
    description: str

class PreconditionRequired(wexc.PreconditionRequired, FlaskSmorestError):
    description: str

class PreconditionFailed(wexc.PreconditionFailed, FlaskSmorestError): ...
