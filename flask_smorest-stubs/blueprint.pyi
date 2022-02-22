from collections import abc
from typing import Any, Callable, TypeVar

from _typeshed import Self
from flask import Blueprint as FlaskBlueprint

from .arguments import ArgumentsMixin as ArgumentsMixin
from .etag import EtagMixin as EtagMixin
from .pagination import PaginationMixin as PaginationMixin
from .response import ResponseMixin as ResponseMixin

def __getattr__(name: str) -> Any: ...  # incomplete

_T = TypeVar("_T", bound=Callable[..., Any])

class Blueprint(FlaskBlueprint, ArgumentsMixin, ResponseMixin, PaginationMixin, EtagMixin):
    HTTP_METHODS: list[str]
    DEFAULT_LOCATION_CONTENT_TYPE_MAPPING: dict[str, str]
    DOCSTRING_INFO_DELIMITER: str

    def __init__(
        self,
        name: str,
        import_name: str,
        *args: Any,
        url_prefix: str | None = ...,
        description: str | None = ...,
        **kwargs: Any
    ) -> None: ...
    @staticmethod
    def doc(**kwargs: str | abc.Mapping[str, Any]) -> Callable[[_T], _T]: ...
    def route(self, rule: str, *, parameters: Any = ..., tags: Any = ..., **options: Any) -> Callable[[_T], _T]: ...
