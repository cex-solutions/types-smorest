from typing import Type  # noqa: Y022 # switching typing.type to builtins.type causes an import error
from typing import Any, Callable, Literal

from _typeshed import Self
from marshmallow import Schema

class ArgumentsMixin:
    ARGUMENTS_PARSER: Any

    def arguments(
        self,
        schema: Schema | Type[Schema],
        *,
        location: Literal["json", "query", "querrystring", "path", "form", "headers", "cookies", "files"] = ...,
        content_type: str | None = ...,
        required: bool = ...,
        description: str | None = ...,
        example: dict[str, object] | None = ...,
        examples: dict[str, object] | None = ...,
        **kwargs: Any
    ) -> Callable[..., Self]: ...
