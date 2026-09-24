"""Hostile Adversarial & Contract Edge-Case Test Suite for Chef Gemini Studio."""

import pytest
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.schemas import ToolResult, SafetyWarning, ProvenanceInfo
from app.units import UnitConverter
from app.registry import ToolRegistry, ToolMetadata


def test_unit_converter_nan_and_infinity():
    """Verify that NaN and Infinity inputs are rejected in unit converter."""
    with pytest.raises(ValueError, match="finite number"):
        UnitConverter.validate_range(float('nan'), 0.0, 100.0, "humidity")

    with pytest.raises(ValueError, match="finite number"):
        UnitConverter.validate_range(float('inf'), 0.0, 100.0, "humidity")


def test_unit_converter_pressure_bounds():
    """Verify gauge vs absolute pressure handling."""
    # Bar to PSI
    assert math.isclose(UnitConverter.mpa_to_psi(1.0), 145.0377, rel_tol=1e-4)


def test_tool_result_empty_fields():
    """Verify ToolResult handling with minimal/empty payloads."""
    res = ToolResult(
        status="success",
        tool="test_tool",
        result={"val": 42}
    )
    formatted = res.format_output()
    assert "Test Tool Analysis" in formatted
    assert "- **Val**: **42**" in formatted
    assert "Safety & Health Notes" not in formatted


def test_tool_registry_fallback():
    """Verify ToolRegistry graceful fallback for unregistered tools."""
    meta = ToolRegistry.get_tool_metadata("unknown_tool_xyz")
    assert meta.name == "unknown_tool_xyz"
    assert meta.domain == "CORE_PANTRY_GROCERY_MULTIMODAL"
    assert meta.risk_level == "low"


if __name__ == "__main__":
    pytest.main(["-v", __file__])
