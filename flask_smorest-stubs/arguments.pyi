from typing import (  # noqa: Y022 # switching typing.type to builtins.type causes an import error
    Any,
    Callable,
    Literal,
    Type,
    TypeVar,
)

from marshmallow import Schema

_T = TypeVar("_T", bound=Callable[..., Any])

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
    ) -> Callable[[_T], _T]: ...
