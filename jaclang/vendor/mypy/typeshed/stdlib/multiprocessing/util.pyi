import threading
from _typeshed import ConvertibleToInt, Incomplete, Unused
from collections.abc import Callable, Iterable, Mapping, MutableMapping, Sequence
from logging import Logger, _Level as _LoggingLevel
from typing import Any

__all__ = [
    "sub_debug",
    "debug",
    "info",
    "sub_warning",
    "get_logger",
    "log_to_stderr",
    "get_temp_dir",
    "register_after_fork",
    "is_exiting",
    "Finalize",
    "ForkAwareThreadLock",
    "ForkAwareLocal",
    "close_all_fds_except",
    "SUBDEBUG",
    "SUBWARNING",
]

NOTSET: int
SUBDEBUG: int
DEBUG: int
INFO: int
SUBWARNING: int

LOGGER_NAME: str
DEFAULT_LOGGING_FORMAT: str

def sub_debug(msg: object, *args: object) -> None: ...
def debug(msg: object, *args: object) -> None: ...
def info(msg: object, *args: object) -> None: ...
def sub_warning(msg: object, *args: object) -> None: ...
def get_logger() -> Logger: ...
def log_to_stderr(level: _LoggingLevel | None = None) -> Logger: ...
def is_abstract_socket_namespace(address: str | bytes | None) -> bool: ...

abstract_sockets_supported: bool

def get_temp_dir() -> str: ...
def register_after_fork(
    obj: Incomplete, func: Callable[[Incomplete], object]
) -> None: ...

class Finalize:
    def __init__(
        self,
        obj: Incomplete | None,
        callback: Callable[..., Incomplete],
        args: Sequence[Any] = (),
        kwargs: Mapping[str, Any] | None = None,
        exitpriority: int | None = None,
    ) -> None: ...
    def __call__(
        self,
        wr: Unused = None,
        _finalizer_registry: MutableMapping[Incomplete, Incomplete] = {},
        sub_debug: Callable[..., object] = ...,
        getpid: Callable[[], int] = ...,
    ) -> Incomplete: ...
    def cancel(self) -> None: ...
    def still_active(self) -> bool: ...

def is_exiting() -> bool: ...

class ForkAwareThreadLock:
    acquire: Callable[[bool, float], bool]
    release: Callable[[], None]
    def __enter__(self) -> bool: ...
    def __exit__(self, *args: Unused) -> None: ...

class ForkAwareLocal(threading.local): ...

MAXFD: int

def close_all_fds_except(fds: Iterable[int]) -> None: ...
def spawnv_passfds(
    path: bytes, args: Sequence[ConvertibleToInt], passfds: Sequence[int]
) -> int: ...
