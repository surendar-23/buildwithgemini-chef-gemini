"""Test suite for new brainstormed features: Aroma Volatile Pairing & HACCP Monitor."""

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.aroma import AromaPairingEngine
from app.haccp import HACCPEngine
from app.tools import calculate_aroma_volatile_pairing, verify_haccp_critical_control_point


def test_aroma_pairing_engine():
    res = AromaPairingEngine.calculate_compatibility("chocolate", "strawberry")
    assert res["synergy_score"] > 0
    assert "linalool" in res["shared_aroma_compounds"]
    assert res["pairing_strength"] in ["EXCEPTIONAL_SYNERGY", "HIGH_COMPATIBILITY", "MODERATE_COMPATIBILITY"]


def test_aroma_pairing_tool():
    output = calculate_aroma_volatile_pairing("basil", "strawberry")
    assert "Calculate Aroma Volatile Pairing Analysis" in output
    assert "linalool" in output.lower()


def test_haccp_engine_compliant():
    res = HACCPEngine.analyze_process_hazard("sous_vide_pork", 62.0, 45.0)
    assert res["status"] == "COMPLIANT"
    assert "FDA Food Code" in res["regulatory_reference"]


def test_haccp_engine_critical_deviation():
    res = HACCPEngine.analyze_process_hazard("sous_vide_pork", 48.0, 10.0)
    assert res["status"] == "CRITICAL_DEVIATION_DETECTED"
    assert "CRITICAL ACTION REQUIRED" in res["corrective_action_workflow"]


def test_haccp_tool_output():
    output = verify_haccp_critical_control_point("cooling_soup", 15.0, 30.0)
    assert "Verify Haccp Critical Control Point Analysis" in output or "Safety & Health Notes" in output


if __name__ == "__main__":
    pytest.main(["-v", __file__])
