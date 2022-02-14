from typing import Any

from flask_smorest.exceptions import MissingAPIParameterError as MissingAPIParameterError
from flask_smorest.utils import prepare_response as prepare_response

from .constants import DEFAULT_REQUEST_BODY_CONTENT_TYPE as DEFAULT_REQUEST_BODY_CONTENT_TYPE
from .constants import DEFAULT_RESPONSE_CONTENT_TYPE as DEFAULT_RESPONSE_CONTENT_TYPE
from .field_converters import uploadfield2properties as uploadfield2properties
from .plugins import FlaskPlugin as FlaskPlugin

def __getattr__(name: str) -> Any: ...  # incomplete

class DocBlueprintMixin: ...

class APISpecMixin(DocBlueprintMixin):
    DEFAULT_ERROR_RESPONSE_NAME: str
    def register_converter(self, converter, func) -> None: ...
    def register_field(self, field, *args) -> None: ...

openapi_cli: Any

def print_openapi_doc() -> None: ...
def write_openapi_doc(output_file) -> None: ...
