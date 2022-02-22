from typing import Any, NoReturn

from apispec import APISpec  # type: ignore[import] # noqa: 723
from flask import Flask, Response

from .blueprint import Blueprint as Blueprint
from .error_handler import ErrorHandlerMixin
from .pagination import Page as Page
from .spec import APISpecMixin

__all__ = ["abort", "Api"]

def abort(http_status_code: int | Response, exc: Exception | None = ..., **kwargs: Any) -> NoReturn: ...

class Api(APISpecMixin, ErrorHandlerMixin):
    spec: APISpec

    def __init__(self, app: Flask | None = ..., *, spec_kwargs: Any = ...) -> None: ...
    def init_app(self, app: Flask, *, spec_kwargs: Any = ...) -> None: ...
    def register_blueprint(self, blp: Blueprint, *, parameters: list[Any] | None = ..., **options: Any) -> None: ...
