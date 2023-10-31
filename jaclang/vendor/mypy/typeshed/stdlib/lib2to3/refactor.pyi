from _typeshed import FileDescriptorOrPath, StrPath, SupportsGetItem
from collections.abc import Container, Generator, Iterable, Mapping
from logging import Logger, _ExcInfoType
from multiprocessing import JoinableQueue
from multiprocessing.synchronize import Lock
from typing import Any, ClassVar, NoReturn, overload
from typing_extensions import Final

from .btm_matcher import BottomMatcher
from .fixer_base import BaseFix
from .pgen2.driver import Driver
from .pgen2.grammar import Grammar
from .pytree import Node

def get_all_fix_names(fixer_pkg: str, remove_prefix: bool = True) -> list[str]: ...
def get_fixers_from_package(pkg_name: str) -> list[str]: ...

class FixerError(Exception): ...

class RefactoringTool:
    CLASS_PREFIX: ClassVar[str]
    FILE_PREFIX: ClassVar[str]
    fixers: Iterable[str]
    explicit: Container[str]
    options: dict[str, Any]
    grammar: Grammar
    write_unchanged_files: bool
    errors: list[tuple[str, Iterable[str], dict[str, _ExcInfoType]]]
    logger: Logger
    fixer_log: list[str]
    wrote: bool
    driver: Driver
    pre_order: list[BaseFix]
    post_order: list[BaseFix]
    files: list[StrPath]
    BM: BottomMatcher
    bmi_pre_order: list[BaseFix]
    bmi_post_order: list[BaseFix]
    def __init__(
        self,
        fixer_names: Iterable[str],
        options: Mapping[str, object] | None = None,
        explicit: Container[str] | None = None,
    ) -> None: ...
    def get_fixers(self) -> tuple[list[BaseFix], list[BaseFix]]: ...
    def log_error(
        self, msg: str, *args: Iterable[str], **kwargs: _ExcInfoType
    ) -> NoReturn: ...
    @overload
    def log_message(self, msg: object) -> None: ...
    @overload
    def log_message(self, msg: str, *args: object) -> None: ...
    @overload
    def log_debug(self, msg: object) -> None: ...
    @overload
    def log_debug(self, msg: str, *args: object) -> None: ...
    def print_output(
        self, old_text: str, new_text: str, filename: StrPath, equal: bool
    ) -> None: ...
    def refactor(
        self, items: Iterable[str], write: bool = False, doctests_only: bool = False
    ) -> None: ...
    def refactor_dir(
        self, dir_name: str, write: bool = False, doctests_only: bool = False
    ) -> None: ...
    def _read_python_source(
        self, filename: FileDescriptorOrPath
    ) -> tuple[str, str]: ...
    def refactor_file(
        self, filename: StrPath, write: bool = False, doctests_only: bool = False
    ) -> None: ...
    def refactor_string(self, data: str, name: str) -> Node | None: ...
    def refactor_stdin(self, doctests_only: bool = False) -> None: ...
    def refactor_tree(self, tree: Node, name: str) -> bool: ...
    def traverse_by(
        self,
        fixers: SupportsGetItem[int, Iterable[BaseFix]] | None,
        traversal: Iterable[Node],
    ) -> None: ...
    def processed_file(
        self,
        new_text: str,
        filename: StrPath,
        old_text: str | None = None,
        write: bool = False,
        encoding: str | None = None,
    ) -> None: ...
    def write_file(
        self,
        new_text: str,
        filename: FileDescriptorOrPath,
        old_text: str,
        encoding: str | None = None,
    ) -> None: ...
    PS1: Final = ">>> "
    PS2: Final = "... "
    def refactor_docstring(self, input: str, filename: StrPath) -> str: ...
    def refactor_doctest(
        self, block: list[str], lineno: int, indent: int, filename: StrPath
    ) -> list[str]: ...
    def summarize(self) -> None: ...
    def parse_block(self, block: Iterable[str], lineno: int, indent: int) -> Node: ...
    def wrap_toks(
        self, block: Iterable[str], lineno: int, indent: int
    ) -> Generator[
        tuple[int, str, tuple[int, int], tuple[int, int], str], None, None
    ]: ...
    def gen_lines(
        self, block: Iterable[str], indent: int
    ) -> Generator[str, None, None]: ...

class MultiprocessingUnsupported(Exception): ...

class MultiprocessRefactoringTool(RefactoringTool):
    queue: JoinableQueue[None | tuple[Iterable[str], bool | int]] | None
    output_lock: Lock | None
    def refactor(
        self,
        items: Iterable[str],
        write: bool = False,
        doctests_only: bool = False,
        num_processes: int = 1,
    ) -> None: ...
