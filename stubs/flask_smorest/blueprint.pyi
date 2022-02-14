from collections import abc
from typing import Any, Callable

from _typeshed import Self
from flask import Blueprint as FlaskBlueprint

from .arguments import ArgumentsMixin as ArgumentsMixin
from .etag import EtagMixin as EtagMixin
from .pagination import PaginationMixin as PaginationMixin
from .response import ResponseMixin as ResponseMixin

class Blueprint(FlaskBlueprint, ArgumentsMixin, ResponseMixin, PaginationMixin, EtagMixin):
    def __getattr__(self, name: str) -> Any: ...  # incomplete
    HTTP_METHODS: list[str]
    DEFAULT_LOCATION_CONTENT_TYPE_MAPPING: dict[str, str]
    DOCSTRING_INFO_DELIMITER: str
    description: str

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def add_url_rule(
        self,
        rule,
        endpoint: Any | None = ...,
        view_func: Any | None = ...,
        provide_automatic_options: Any | None = ...,
        *,
        parameters: Any | None = ...,
        tags: Any | None = ...,
        **options
    ) -> None: ...
    def route(self, rule, *, parameters: Any | None = ..., tags: Any | None = ..., **options): ...
    def register_views_in_doc(self, api, app, spec, name, parameters) -> None: ...
    @staticmethod
    def doc(**kwargs: str | abc.Mapping) -> Callable[..., Self]: ...
