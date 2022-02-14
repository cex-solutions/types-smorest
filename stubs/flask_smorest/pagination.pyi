from typing import Any

import marshmallow as ma

from .utils import unpack_tuple_response as unpack_tuple_response

def __getattr__(self, name: str) -> Any: ...  # incomplete

class PaginationParameters:
    page: Any
    page_size: Any
    item_count: Any
    def __init__(self, page, page_size) -> None: ...
    @property
    def first_item(self): ...
    @property
    def last_item(self): ...

class Page:
    collection: Any
    page_params: Any
    def __init__(self, collection, page_params) -> None: ...
    @property
    def items(self): ...
    @property
    def item_count(self): ...

class PaginationMetadataSchema(ma.Schema):
    total: Any
    total_pages: Any
    first_page: Any
    last_page: Any
    page: Any
    previous_page: Any
    next_page: Any

    class Meta:
        ordered: bool

PAGINATION_HEADER: Any

class PaginationMixin:
    PAGINATION_ARGUMENTS_PARSER: Any
    PAGINATION_HEADER_NAME: str
    DEFAULT_PAGINATION_PARAMETERS: Any
    def paginate(
        self,
        pager: Any | None = ...,
        *,
        page: Any | None = ...,
        page_size: Any | None = ...,
        max_page_size: Any | None = ...
    ): ...
