"""Centralized Unit Normalization and Dimensional Integrity Engine."""

from typing import Dict, Any, Tuple


class UnitConverter:
    """Provides dimensional normalization across mass, volume, temperature, pressure, and kinetic energy."""

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        return (celsius * 9.0 / 5.0) + 32.0

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        return (fahrenheit - 32.0) * 5.0 / 9.0

    @staticmethod
    def grams_to_ounces(grams: float) -> float:
        return grams * 0.03527396

    @staticmethod
    def mpa_to_bar(mpa: float) -> float:
        return mpa * 10.0

    @staticmethod
    def mpa_to_psi(mpa: float) -> float:
        return mpa * 145.0377

    @staticmethod
    def validate_non_negative(val: float, param_name: str) -> None:
        if val < 0:
            raise ValueError(f"Parameter '{param_name}' cannot be negative ({val}).")

    @staticmethod
    def validate_range(val: float, min_val: float, max_val: float, param_name: str) -> None:
        if not (min_val <= val <= max_val):
            raise ValueError(f"Parameter '{param_name}' ({val}) is outside valid scientific range [{min_val}, {max_val}].")
