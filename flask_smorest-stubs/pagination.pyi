from typing import Any

import marshmallow as ma

from .utils import unpack_tuple_response as unpack_tuple_response

def __getattr__(name: str) -> Any: ...  # incomplete
