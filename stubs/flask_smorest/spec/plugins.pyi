from typing import Any

from apispec import BasePlugin  # type: ignore[import] # noqa: 723

def __getattr__(name: str) -> Any: ...  # incomplete

RE_URL: Any

def baseconverter2paramschema(converter): ...
def unicodeconverter2paramschema(converter): ...
def integerconverter2paramschema(converter): ...
def floatconverter2paramschema(converter): ...
def anyconverter2paramschema(converter): ...
def uuidconverter2paramschema(converter): ...

DEFAULT_CONVERTER_MAPPING: Any

class FlaskPlugin(BasePlugin):
    converter_mapping: Any
    openapi_version: Any
    def __init__(self) -> None: ...
    def init_spec(self, spec) -> None: ...
    @staticmethod
    def flaskpath2openapi(path): ...
    def register_converter(self, converter, func) -> None: ...
    def rule_to_params(self, rule): ...
    def path_helper(self, rule, operations, parameters, **kwargs): ...
