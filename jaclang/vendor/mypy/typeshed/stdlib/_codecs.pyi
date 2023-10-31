import codecs
import sys
from _typeshed import ReadableBuffer
from collections.abc import Callable
from typing import overload
from typing_extensions import Literal, TypeAlias

# This type is not exposed; it is defined in unicodeobject.c
class _EncodingMap:
    def size(self) -> int: ...

_CharMap: TypeAlias = dict[int, int] | _EncodingMap
_Handler: TypeAlias = Callable[[UnicodeError], tuple[str | bytes, int]]
_SearchFunction: TypeAlias = Callable[[str], codecs.CodecInfo | None]

def register(__search_function: _SearchFunction) -> None: ...

if sys.version_info >= (3, 10):
    def unregister(__search_function: _SearchFunction) -> None: ...

def register_error(__errors: str, __handler: _Handler) -> None: ...
def lookup_error(__name: str) -> _Handler: ...

# The type ignore on `encode` and `decode` is to avoid issues with overlapping overloads, for more details, see #300
# https://docs.python.org/3/library/codecs.html#binary-transforms
_BytesToBytesEncoding: TypeAlias = Literal[
    "base64",
    "base_64",
    "base64_codec",
    "bz2",
    "bz2_codec",
    "hex",
    "hex_codec",
    "quopri",
    "quotedprintable",
    "quoted_printable",
    "quopri_codec",
    "uu",
    "uu_codec",
    "zip",
    "zlib",
    "zlib_codec",
]
# https://docs.python.org/3/library/codecs.html#text-transforms
_StrToStrEncoding: TypeAlias = Literal["rot13", "rot_13"]

@overload
def encode(
    obj: ReadableBuffer, encoding: _BytesToBytesEncoding, errors: str = "strict"
) -> bytes: ...
@overload
def encode(obj: str, encoding: _StrToStrEncoding, errors: str = "strict") -> str: ...  # type: ignore[misc]
@overload
def encode(obj: str, encoding: str = "utf-8", errors: str = "strict") -> bytes: ...
@overload
def decode(obj: ReadableBuffer, encoding: _BytesToBytesEncoding, errors: str = "strict") -> bytes: ...  # type: ignore[misc]
@overload
def decode(obj: str, encoding: _StrToStrEncoding, errors: str = "strict") -> str: ...

# these are documented as text encodings but in practice they also accept str as input
@overload
def decode(
    obj: str,
    encoding: Literal[
        "unicode_escape", "unicode-escape", "raw_unicode_escape", "raw-unicode-escape"
    ],
    errors: str = "strict",
) -> str: ...

# hex is officially documented as a bytes to bytes encoding, but it appears to also work with str
@overload
def decode(
    obj: str, encoding: Literal["hex", "hex_codec"], errors: str = "strict"
) -> bytes: ...
@overload
def decode(
    obj: ReadableBuffer, encoding: str = "utf-8", errors: str = "strict"
) -> str: ...
def lookup(__encoding: str) -> codecs.CodecInfo: ...
def charmap_build(__map: str) -> _CharMap: ...
def ascii_decode(
    __data: ReadableBuffer, __errors: str | None = None
) -> tuple[str, int]: ...
def ascii_encode(__str: str, __errors: str | None = None) -> tuple[bytes, int]: ...
def charmap_decode(
    __data: ReadableBuffer,
    __errors: str | None = None,
    __mapping: _CharMap | None = None,
) -> tuple[str, int]: ...
def charmap_encode(
    __str: str, __errors: str | None = None, __mapping: _CharMap | None = None
) -> tuple[bytes, int]: ...
def escape_decode(
    __data: str | ReadableBuffer, __errors: str | None = None
) -> tuple[str, int]: ...
def escape_encode(__data: bytes, __errors: str | None = None) -> tuple[bytes, int]: ...
def latin_1_decode(
    __data: ReadableBuffer, __errors: str | None = None
) -> tuple[str, int]: ...
def latin_1_encode(__str: str, __errors: str | None = None) -> tuple[bytes, int]: ...

if sys.version_info >= (3, 9):
    def raw_unicode_escape_decode(
        __data: str | ReadableBuffer, __errors: str | None = None, __final: bool = True
    ) -> tuple[str, int]: ...

else:
    def raw_unicode_escape_decode(
        __data: str | ReadableBuffer, __errors: str | None = None
    ) -> tuple[str, int]: ...

def raw_unicode_escape_encode(
    __str: str, __errors: str | None = None
) -> tuple[bytes, int]: ...
def readbuffer_encode(
    __data: str | ReadableBuffer, __errors: str | None = None
) -> tuple[bytes, int]: ...

if sys.version_info >= (3, 9):
    def unicode_escape_decode(
        __data: str | ReadableBuffer, __errors: str | None = None, __final: bool = True
    ) -> tuple[str, int]: ...

else:
    def unicode_escape_decode(
        __data: str | ReadableBuffer, __errors: str | None = None
    ) -> tuple[str, int]: ...

def unicode_escape_encode(
    __str: str, __errors: str | None = None
) -> tuple[bytes, int]: ...

if sys.version_info < (3, 8):
    def unicode_internal_decode(
        __obj: str | ReadableBuffer, __errors: str | None = None
    ) -> tuple[str, int]: ...
    def unicode_internal_encode(
        __obj: str | ReadableBuffer, __errors: str | None = None
    ) -> tuple[bytes, int]: ...

def utf_16_be_decode(
    __data: ReadableBuffer, __errors: str | None = None, __final: bool = False
) -> tuple[str, int]: ...
def utf_16_be_encode(__str: str, __errors: str | None = None) -> tuple[bytes, int]: ...
def utf_16_decode(
    __data: ReadableBuffer, __errors: str | None = None, __final: bool = False
) -> tuple[str, int]: ...
def utf_16_encode(
    __str: str, __errors: str | None = None, __byteorder: int = 0
) -> tuple[bytes, int]: ...
def utf_16_ex_decode(
    __data: ReadableBuffer,
    __errors: str | None = None,
    __byteorder: int = 0,
    __final: bool = False,
) -> tuple[str, int, int]: ...
def utf_16_le_decode(
    __data: ReadableBuffer, __errors: str | None = None, __final: bool = False
) -> tuple[str, int]: ...
def utf_16_le_encode(__str: str, __errors: str | None = None) -> tuple[bytes, int]: ...
def utf_32_be_decode(
    __data: ReadableBuffer, __errors: str | None = None, __final: bool = False
) -> tuple[str, int]: ...
def utf_32_be_encode(__str: str, __errors: str | None = None) -> tuple[bytes, int]: ...
def utf_32_decode(
    __data: ReadableBuffer, __errors: str | None = None, __final: bool = False
) -> tuple[str, int]: ...
def utf_32_encode(
    __str: str, __errors: str | None = None, __byteorder: int = 0
) -> tuple[bytes, int]: ...
def utf_32_ex_decode(
    __data: ReadableBuffer,
    __errors: str | None = None,
    __byteorder: int = 0,
    __final: bool = False,
) -> tuple[str, int, int]: ...
def utf_32_le_decode(
    __data: ReadableBuffer, __errors: str | None = None, __final: bool = False
) -> tuple[str, int]: ...
def utf_32_le_encode(__str: str, __errors: str | None = None) -> tuple[bytes, int]: ...
def utf_7_decode(
    __data: ReadableBuffer, __errors: str | None = None, __final: bool = False
) -> tuple[str, int]: ...
def utf_7_encode(__str: str, __errors: str | None = None) -> tuple[bytes, int]: ...
def utf_8_decode(
    __data: ReadableBuffer, __errors: str | None = None, __final: bool = False
) -> tuple[str, int]: ...
def utf_8_encode(__str: str, __errors: str | None = None) -> tuple[bytes, int]: ...

if sys.platform == "win32":
    def mbcs_decode(
        __data: ReadableBuffer, __errors: str | None = None, __final: bool = False
    ) -> tuple[str, int]: ...
    def mbcs_encode(__str: str, __errors: str | None = None) -> tuple[bytes, int]: ...
    def code_page_decode(
        __codepage: int,
        __data: ReadableBuffer,
        __errors: str | None = None,
        __final: bool = False,
    ) -> tuple[str, int]: ...
    def code_page_encode(
        __code_page: int, __str: str, __errors: str | None = None
    ) -> tuple[bytes, int]: ...
    def oem_decode(
        __data: ReadableBuffer, __errors: str | None = None, __final: bool = False
    ) -> tuple[str, int]: ...
    def oem_encode(__str: str, __errors: str | None = None) -> tuple[bytes, int]: ...
