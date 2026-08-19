"""Deterministic SCAF Consumption Selection builder package."""

from __future__ import annotations

from typing import Any

__all__ = (
    "ConsumptionSelectionBuildError",
    "build_consumption_selection",
)


def __getattr__(name: str) -> Any:
    if name in __all__:
        from .builder import (
            ConsumptionSelectionBuildError,
            build_consumption_selection,
        )

        return {
            "ConsumptionSelectionBuildError": ConsumptionSelectionBuildError,
            "build_consumption_selection": build_consumption_selection,
        }[name]
    raise AttributeError(name)
