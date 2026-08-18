"""Validated deterministic read-only views over SCAF Project Application data."""

from __future__ import annotations

from importlib import import_module
from typing import Any

__all__ = (
    "ProjectApplicationViewError",
    "query_record",
    "query_authority",
    "query_scope",
)


def __getattr__(name: str) -> Any:
    """Lazily expose the supported API without preloading the CLI target module."""
    if name not in __all__:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    query_module = import_module(f"{__name__}.query")
    value = getattr(query_module, name)
    globals()[name] = value
    return value


def __dir__() -> list[str]:
    return sorted(set(globals()) | set(__all__))
