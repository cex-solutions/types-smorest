from http import HTTPStatus
from typing import Type  # noqa: Y022 # switching typing.type to builtins.type causes an import error
from typing import Callable

from _typeshed import Self
from marshmallow import Schema

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
    ) -> Callable[..., Self]: ...
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
    ) -> Callable[..., Self]: ...
