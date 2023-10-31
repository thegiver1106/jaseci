from _typeshed import Unused
from types import ModuleType
from typing import Any
from typing_extensions import Self

__all__ = ["run_module", "run_path"]

class _TempModule:
    mod_name: str
    module: ModuleType
    def __init__(self, mod_name: str) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: Unused) -> None: ...

class _ModifiedArgv0:
    value: Any
    def __init__(self, value: Any) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args: Unused) -> None: ...

def run_module(
    mod_name: str,
    init_globals: dict[str, Any] | None = None,
    run_name: str | None = None,
    alter_sys: bool = False,
) -> dict[str, Any]: ...
def run_path(
    path_name: str,
    init_globals: dict[str, Any] | None = None,
    run_name: str | None = None,
) -> dict[str, Any]: ...
