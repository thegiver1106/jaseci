import sys
import types
from abc import ABCMeta, abstractmethod
from collections.abc import Callable
from typing import Any
from typing_extensions import Literal, Self

from .events import AbstractEventLoop, BaseDefaultEventLoopPolicy
from .selector_events import BaseSelectorEventLoop

# This is also technically not available on Win,
# but other parts of typeshed need this definition.
# So, it is special cased.
class AbstractChildWatcher:
    @abstractmethod
    def add_child_handler(
        self, pid: int, callback: Callable[..., object], *args: Any
    ) -> None: ...
    @abstractmethod
    def remove_child_handler(self, pid: int) -> bool: ...
    @abstractmethod
    def attach_loop(self, loop: AbstractEventLoop | None) -> None: ...
    @abstractmethod
    def close(self) -> None: ...
    @abstractmethod
    def __enter__(self) -> Self: ...
    @abstractmethod
    def __exit__(
        self,
        typ: type[BaseException] | None,
        exc: BaseException | None,
        tb: types.TracebackType | None,
    ) -> None: ...
    if sys.version_info >= (3, 8):
        @abstractmethod
        def is_active(self) -> bool: ...

if sys.platform != "win32":
    if sys.version_info >= (3, 9):
        __all__ = (
            "SelectorEventLoop",
            "AbstractChildWatcher",
            "SafeChildWatcher",
            "FastChildWatcher",
            "PidfdChildWatcher",
            "MultiLoopChildWatcher",
            "ThreadedChildWatcher",
            "DefaultEventLoopPolicy",
        )
    elif sys.version_info >= (3, 8):
        __all__ = (
            "SelectorEventLoop",
            "AbstractChildWatcher",
            "SafeChildWatcher",
            "FastChildWatcher",
            "MultiLoopChildWatcher",
            "ThreadedChildWatcher",
            "DefaultEventLoopPolicy",
        )
    else:
        __all__ = (
            "SelectorEventLoop",
            "AbstractChildWatcher",
            "SafeChildWatcher",
            "FastChildWatcher",
            "DefaultEventLoopPolicy",
        )

    # Doesn't actually have ABCMeta metaclass at runtime, but mypy complains if we don't have it in the stub.
    # See discussion in #7412
    class BaseChildWatcher(AbstractChildWatcher, metaclass=ABCMeta):
        def close(self) -> None: ...
        if sys.version_info >= (3, 8):
            def is_active(self) -> bool: ...

        def attach_loop(self, loop: AbstractEventLoop | None) -> None: ...

    class SafeChildWatcher(BaseChildWatcher):
        def __enter__(self) -> Self: ...
        def __exit__(
            self,
            a: type[BaseException] | None,
            b: BaseException | None,
            c: types.TracebackType | None,
        ) -> None: ...
        def add_child_handler(
            self, pid: int, callback: Callable[..., object], *args: Any
        ) -> None: ...
        def remove_child_handler(self, pid: int) -> bool: ...

    class FastChildWatcher(BaseChildWatcher):
        def __enter__(self) -> Self: ...
        def __exit__(
            self,
            a: type[BaseException] | None,
            b: BaseException | None,
            c: types.TracebackType | None,
        ) -> None: ...
        def add_child_handler(
            self, pid: int, callback: Callable[..., object], *args: Any
        ) -> None: ...
        def remove_child_handler(self, pid: int) -> bool: ...

    class _UnixSelectorEventLoop(BaseSelectorEventLoop): ...

    class _UnixDefaultEventLoopPolicy(BaseDefaultEventLoopPolicy):
        def get_child_watcher(self) -> AbstractChildWatcher: ...
        def set_child_watcher(self, watcher: AbstractChildWatcher | None) -> None: ...
    SelectorEventLoop = _UnixSelectorEventLoop

    DefaultEventLoopPolicy = _UnixDefaultEventLoopPolicy

    if sys.version_info >= (3, 8):
        from typing import Protocol

        class _Warn(Protocol):
            def __call__(
                self,
                message: str,
                category: type[Warning] | None = ...,
                stacklevel: int = ...,
                source: Any | None = ...,
            ) -> object: ...

        class MultiLoopChildWatcher(AbstractChildWatcher):
            def is_active(self) -> bool: ...
            def close(self) -> None: ...
            def __enter__(self) -> Self: ...
            def __exit__(
                self,
                exc_type: type[BaseException] | None,
                exc_val: BaseException | None,
                exc_tb: types.TracebackType | None,
            ) -> None: ...
            def add_child_handler(
                self, pid: int, callback: Callable[..., object], *args: Any
            ) -> None: ...
            def remove_child_handler(self, pid: int) -> bool: ...
            def attach_loop(self, loop: AbstractEventLoop | None) -> None: ...

        class ThreadedChildWatcher(AbstractChildWatcher):
            def is_active(self) -> Literal[True]: ...
            def close(self) -> None: ...
            def __enter__(self) -> Self: ...
            def __exit__(
                self,
                exc_type: type[BaseException] | None,
                exc_val: BaseException | None,
                exc_tb: types.TracebackType | None,
            ) -> None: ...
            def __del__(self, _warn: _Warn = ...) -> None: ...
            def add_child_handler(
                self, pid: int, callback: Callable[..., object], *args: Any
            ) -> None: ...
            def remove_child_handler(self, pid: int) -> bool: ...
            def attach_loop(self, loop: AbstractEventLoop | None) -> None: ...

    if sys.version_info >= (3, 9):
        class PidfdChildWatcher(AbstractChildWatcher):
            def __enter__(self) -> Self: ...
            def __exit__(
                self,
                exc_type: type[BaseException] | None,
                exc_val: BaseException | None,
                exc_tb: types.TracebackType | None,
            ) -> None: ...
            def is_active(self) -> bool: ...
            def close(self) -> None: ...
            def attach_loop(self, loop: AbstractEventLoop | None) -> None: ...
            def add_child_handler(
                self, pid: int, callback: Callable[..., object], *args: Any
            ) -> None: ...
            def remove_child_handler(self, pid: int) -> bool: ...
