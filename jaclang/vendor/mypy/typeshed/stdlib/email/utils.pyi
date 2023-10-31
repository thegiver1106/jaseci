import datetime
import sys
from _typeshed import Unused
from email import _ParamType
from email.charset import Charset
from typing import overload
from typing_extensions import TypeAlias

__all__ = [
    "collapse_rfc2231_value",
    "decode_params",
    "decode_rfc2231",
    "encode_rfc2231",
    "formataddr",
    "formatdate",
    "format_datetime",
    "getaddresses",
    "make_msgid",
    "mktime_tz",
    "parseaddr",
    "parsedate",
    "parsedate_tz",
    "parsedate_to_datetime",
    "unquote",
]

_PDTZ: TypeAlias = tuple[int, int, int, int, int, int, int, int, int, int | None]

def quote(str: str) -> str: ...
def unquote(str: str) -> str: ...
def parseaddr(addr: str | None) -> tuple[str, str]: ...
def formataddr(
    pair: tuple[str | None, str], charset: str | Charset = "utf-8"
) -> str: ...
def getaddresses(fieldvalues: list[str]) -> list[tuple[str, str]]: ...
@overload
def parsedate(data: None) -> None: ...
@overload
def parsedate(
    data: str,
) -> tuple[int, int, int, int, int, int, int, int, int] | None: ...
@overload
def parsedate_tz(data: None) -> None: ...
@overload
def parsedate_tz(data: str) -> _PDTZ | None: ...

if sys.version_info >= (3, 10):
    @overload
    def parsedate_to_datetime(data: None) -> None: ...
    @overload
    def parsedate_to_datetime(data: str) -> datetime.datetime: ...

else:
    def parsedate_to_datetime(data: str) -> datetime.datetime: ...

def mktime_tz(data: _PDTZ) -> int: ...
def formatdate(
    timeval: float | None = None, localtime: bool = False, usegmt: bool = False
) -> str: ...
def format_datetime(dt: datetime.datetime, usegmt: bool = False) -> str: ...

if sys.version_info >= (3, 12):
    def localtime(
        dt: datetime.datetime | None = None, isdst: Unused = None
    ) -> datetime.datetime: ...

else:
    def localtime(
        dt: datetime.datetime | None = None, isdst: int = -1
    ) -> datetime.datetime: ...

def make_msgid(idstring: str | None = None, domain: str | None = None) -> str: ...
def decode_rfc2231(
    s: str,
) -> tuple[
    str | None, str | None, str
]: ...  # May return list[str]. See issue #10431 for details.
def encode_rfc2231(
    s: str, charset: str | None = None, language: str | None = None
) -> str: ...
def collapse_rfc2231_value(
    value: _ParamType, errors: str = "replace", fallback_charset: str = "us-ascii"
) -> str: ...
def decode_params(params: list[tuple[str, str]]) -> list[tuple[str, _ParamType]]: ...
