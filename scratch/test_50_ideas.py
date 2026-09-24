"""Test suite for the 50 new brainstormed tools."""

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.science_ext import FoodScienceEngine
from app.clinical_ext import ClinicalEngine
from app.ops_ext import OpsEngine
from app.beverage_ext import BeverageEngine
from app.future_ext import FutureFoodEngine
from app.tools import (
    nmr_water_mobility_analyzer,
    cgm_glucose_curve_predictor,
    haccp_alarm_workflow_engine,
    rotovap_boiling_point_calc,
    food_3d_printing_rheology_modeler
)


def test_category_1_science():
    res = FoodScienceEngine.nmr_water_mobility(50.0, 80.0)
    assert res["estimated_water_activity"] > 0.0
    out = nmr_water_mobility_analyzer(50.0, 80.0)
    assert "Nmr Water Mobility Analyzer Analysis" in out or "water" in out.lower()


def test_category_2_clinical():
    res = ClinicalEngine.cgm_glucose_curve(45.0, 10.0, 5.0)
    assert res["estimated_glucose_peak_spike_mg_dl"] > 0.0
    out = cgm_glucose_curve_predictor(45.0, 10.0, 5.0)
    assert "Cgm Glucose Curve Predictor Analysis" in out or "glucose" in out.lower()


def test_category_3_ops():
    res = OpsEngine.haccp_alarm_workflow(8.0, 3.0)
    assert res["is_critical_deviation"] is True
    out = haccp_alarm_workflow_engine(8.0, 3.0)
    assert "Haccp Alarm Workflow Engine Analysis" in out or "critical" in out.lower()


def test_category_4_beverage():
    res = BeverageEngine.rotovap_boiling_point(35.0, 40.0)
    assert res["required_vacuum_mbar"] > 0.0
    out = rotovap_boiling_point_calc(35.0, 40.0)
    assert "Rotovap Boiling Point Calc Analysis" in out or "vacuum" in out.lower()


def test_category_5_future():
    res = FutureFoodEngine.food_3d_printing_rheology(35.0, 1.2)
    assert res["is_3d_printable"] is True
    out = food_3d_printing_rheology_modeler(35.0, 1.2)
    assert "Food 3D Printing Rheology Modeler Analysis" in out or "printable" in out.lower()


if __name__ == "__main__":
    pytest.main(["-v", __file__])
