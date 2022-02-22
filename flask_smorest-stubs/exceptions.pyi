from typing import Any

import werkzeug.exceptions as wexc

def __getattr__(name: str) -> Any: ...  # incomplete
