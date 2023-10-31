import sys
from _typeshed import ReadableBuffer
from collections.abc import Mapping, MutableMapping
from datetime import datetime
from enum import Enum
from typing import IO, Any
from typing_extensions import Self

if sys.version_info >= (3, 9):
    __all__ = [
        "InvalidFileException",
        "FMT_XML",
        "FMT_BINARY",
        "load",
        "dump",
        "loads",
        "dumps",
        "UID",
    ]
elif sys.version_info >= (3, 8):
    __all__ = [
        "readPlist",
        "writePlist",
        "readPlistFromBytes",
        "writePlistToBytes",
        "Data",
        "InvalidFileException",
        "FMT_XML",
        "FMT_BINARY",
        "load",
        "dump",
        "loads",
        "dumps",
        "UID",
    ]
else:
    __all__ = [
        "readPlist",
        "writePlist",
        "readPlistFromBytes",
        "writePlistToBytes",
        "Data",
        "InvalidFileException",
        "FMT_XML",
        "FMT_BINARY",
        "load",
        "dump",
        "loads",
        "dumps",
    ]

class PlistFormat(Enum):
    FMT_XML: int
    FMT_BINARY: int

FMT_XML = PlistFormat.FMT_XML
FMT_BINARY = PlistFormat.FMT_BINARY

if sys.version_info >= (3, 9):
    def load(
        fp: IO[bytes],
        *,
        fmt: PlistFormat | None = None,
        dict_type: type[MutableMapping[str, Any]] = ...,
    ) -> Any: ...
    def loads(
        value: ReadableBuffer,
        *,
        fmt: PlistFormat | None = None,
        dict_type: type[MutableMapping[str, Any]] = ...,
    ) -> Any: ...

else:
    def load(
        fp: IO[bytes],
        *,
        fmt: PlistFormat | None = None,
        use_builtin_types: bool = True,
        dict_type: type[MutableMapping[str, Any]] = ...,
    ) -> Any: ...
    def loads(
        value: ReadableBuffer,
        *,
        fmt: PlistFormat | None = None,
        use_builtin_types: bool = True,
        dict_type: type[MutableMapping[str, Any]] = ...,
    ) -> Any: ...

def dump(
    value: Mapping[str, Any]
    | list[Any]
    | tuple[Any, ...]
    | str
    | bool
    | float
    | bytes
    | bytearray
    | datetime,
    fp: IO[bytes],
    *,
    fmt: PlistFormat = ...,
    sort_keys: bool = True,
    skipkeys: bool = False,
) -> None: ...
def dumps(
    value: Mapping[str, Any]
    | list[Any]
    | tuple[Any, ...]
    | str
    | bool
    | float
    | bytes
    | bytearray
    | datetime,
    *,
    fmt: PlistFormat = ...,
    skipkeys: bool = False,
    sort_keys: bool = True,
) -> bytes: ...

if sys.version_info < (3, 9):
    def readPlist(pathOrFile: str | IO[bytes]) -> Any: ...
    def writePlist(value: Mapping[str, Any], pathOrFile: str | IO[bytes]) -> None: ...
    def readPlistFromBytes(data: ReadableBuffer) -> Any: ...
    def writePlistToBytes(value: Mapping[str, Any]) -> bytes: ...

if sys.version_info < (3, 9):
    class Data:
        data: bytes
        def __init__(self, data: bytes) -> None: ...

if sys.version_info >= (3, 8):
    class UID:
        data: int
        def __init__(self, data: int) -> None: ...
        def __index__(self) -> int: ...
        def __reduce__(self) -> tuple[type[Self], tuple[int]]: ...
        def __hash__(self) -> int: ...
        def __eq__(self, other: object) -> bool: ...

class InvalidFileException(ValueError):
    def __init__(self, message: str = "Invalid file") -> None: ...
