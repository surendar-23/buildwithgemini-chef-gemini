"""Test suite for Phase 2 contracts, safety disclaimers, unit conversions, and domain registry."""

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.schemas import ToolResult, SafetyWarning, ProvenanceInfo
from app.units import UnitConverter
from app.registry import ToolRegistry, ToolMetadata
from app.agent import root_agent


def test_tool_result_contract():
    result = ToolResult(
        status="success",
        tool="sous_vide_pasteurization_log_reducer",
        result={"log_reduction": 6.5, "holding_minutes": 45.0},
        units={"holding_minutes": "mins"},
        assumptions=["Water bath temperature is calibrated to +/- 0.1°C"],
        warnings=[
            SafetyWarning(
                category="food_safety",
                level="warning",
                message="Core temperature must reach 58.0°C before timing begins.",
                regulatory_reference="FDA Food Code 3-401.11"
            )
        ],
        provenance=ProvenanceInfo(formula_id="FSIS-6D-SALMONELLA-2021")
    )
    
    formatted = result.format_output()
    assert "Sous Vide Pasteurization Log Reducer Analysis" in formatted
    assert "FDA Food Code 3-401.11" in formatted
    assert "FSIS-6D-SALMONELLA-2021" in formatted


def test_unit_converter_validations():
    assert UnitConverter.celsius_to_fahrenheit(100.0) == 212.0
    assert UnitConverter.mpa_to_bar(600.0) == 6000.0

    with pytest.raises(ValueError, match="non-negative"):
        UnitConverter.validate_non_negative(-5.0, "mass_g")

    with pytest.raises(ValueError, match="outside valid scientific range"):
        UnitConverter.validate_range(150.0, 0.0, 100.0, "humidity_pct")


def test_tool_registry():
    meta = ToolMetadata(
        name="haccp_critical_control_point_monitor",
        domain="PRESERVATION_FERMENTATION",
        subdomain="haccp",
        risk_level="high"
    )
    ToolRegistry.register_tool(meta)
    
    tools = ToolRegistry.get_domain_tools("PRESERVATION_FERMENTATION")
    assert "haccp_critical_control_point_monitor" in tools


def test_root_agent_tool_count():
    from app.registry import ToolRegistry
    ToolRegistry.auto_discover()
    assert len(root_agent.tools) >= 10
    assert len(ToolRegistry._registry) >= 220


if __name__ == "__main__":
    pytest.main(["-v", __file__])
