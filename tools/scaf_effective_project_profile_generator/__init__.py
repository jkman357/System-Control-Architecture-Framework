"""Deterministic validated SCAF Effective Project Profile generation."""

from __future__ import annotations

from importlib import import_module
from typing import Any

__all__ = (
    "EffectiveProjectProfileGenerationError",
    "generate_effective_project_profile",
)


def __getattr__(name: str) -> Any:
    """Lazily expose the supported API without preloading the CLI module."""
    if name not in __all__:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    generator_module = import_module(f"{__name__}.generator")
    value = getattr(generator_module, name)
    globals()[name] = value
    return value


def __dir__() -> list[str]:
    return sorted(set(globals()) | set(__all__))
