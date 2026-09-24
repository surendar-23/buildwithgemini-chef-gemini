"""Centralized Unit Normalization and Dimensional Integrity Engine."""

import math
from typing import Dict, Any, Tuple


class UnitConverter:
    """Provides dimensional normalization across mass, volume, temperature, pressure, and kinetic energy."""

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        if math.isnan(celsius) or math.isinf(celsius):
            raise ValueError("Temperature input must be a finite number.")
        return (celsius * 9.0 / 5.0) + 32.0

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        if math.isnan(fahrenheit) or math.isinf(fahrenheit):
            raise ValueError("Temperature input must be a finite number.")
        return (fahrenheit - 32.0) * 5.0 / 9.0

    @staticmethod
    def grams_to_ounces(grams: float) -> float:
        if math.isnan(grams) or math.isinf(grams) or grams < 0:
            raise ValueError("Mass input must be a non-negative finite number.")
        return grams * 0.03527396

    @staticmethod
    def mpa_to_bar(mpa: float) -> float:
        if math.isnan(mpa) or math.isinf(mpa) or mpa < 0:
            raise ValueError("Pressure input must be a non-negative finite number.")
        return mpa * 10.0

    @staticmethod
    def mpa_to_psi(mpa: float) -> float:
        if math.isnan(mpa) or math.isinf(mpa) or mpa < 0:
            raise ValueError("Pressure input must be a non-negative finite number.")
        return mpa * 145.0377

    @staticmethod
    def validate_non_negative(val: float, param_name: str) -> None:
        if math.isnan(val) or math.isinf(val) or val < 0:
            raise ValueError(f"Parameter '{param_name}' must be a non-negative finite number (got {val}).")

    @staticmethod
    def validate_range(val: float, min_val: float, max_val: float, param_name: str) -> None:
        if math.isnan(val) or math.isinf(val):
            raise ValueError(f"Parameter '{param_name}' must be a finite number.")
        if not (min_val <= val <= max_val):
            raise ValueError(f"Parameter '{param_name}' ({val}) is outside valid scientific range [{min_val}, {max_val}].")
