from http import HTTPStatus
from typing import (  # noqa: Y022 # switching typing.type to builtins.type causes an import error
    Any,
    Callable,
    Type,
    TypeVar,
)

from marshmallow import Schema

_T = TypeVar("_T", bound=Callable[..., Any])

class ResponseMixin:
    def response(
        self,
        status_code: int | str | HTTPStatus,
        schema: Schema | Type[Schema] | None = ...,
        *,
        description: str | None = ...,
        example: dict[str, object] | None = ...,
        examples: dict[str, object] | None = ...,
        headers: dict[str, object] | None = ...
    ) -> Callable[[_T], _T]: ...
    def alt_response(
        self,
        status_code: int | str | HTTPStatus,
        response: str | None = ...,
        *,
        schema: Schema | Type[Schema] | None = ...,
        description: str | None = ...,
        example: dict[str, object] | None = ...,
        examples: dict[str, object] | None = ...,
        headers: dict[str, object] | None = ...,
        success: bool = ...
    ) -> Callable[[_T], _T]: ...
