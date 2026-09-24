"""Unit test suite for Upscaled Chef Gemini (222 tools & multi-domain science)."""

import pytest
import sys
from pathlib import Path

# Ensure app directory is in sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.agent import root_agent
from app.tools import (
    food_printing_3d_rheology_shear_rate,
    acoustic_levitation_contactless_dehydration,
    mycelium_fermentation_scaffold_density,
    pulsed_electric_field_pef_cell_permeabilization,
    sonic_acoustic_spirits_accelerated_aging,
    smart_sous_vide_thermocouple_core_calc,
    bio_fermented_ester_aroma_synthesizer,
    laser_caramelization_surface_engraving,
    atmospheric_cold_plasma_food_sanitization,
    high_pressure_processing_hpp_protein_denaturation,
)


def test_agent_total_tools():
    """Verify that root_agent registers over 220 tools."""
    assert len(root_agent.tools) >= 220, f"Expected >= 220 tools, got {len(root_agent.tools)}"


def test_batch_10_future_food_science_tools():
    """Verify Batch 10 future food science tools."""
    res1 = food_printing_3d_rheology_shear_rate(150.0, 1.2)
    assert "3D Food Printing" in res1

    res2 = acoustic_levitation_contactless_dehydration(50.0, 40.0)
    assert "Acoustic Levitation" in res2

    res3 = mycelium_fermentation_scaffold_density(200.0, 7)
    assert "Mycelium Bio-Scaffold" in res3

    res4 = pulsed_electric_field_pef_cell_permeabilization(3.5, 20.0)
    assert "Pulsed Electric Field" in res4

    res5 = sonic_acoustic_spirits_accelerated_aging(500.0, 15.0)
    assert "Sonic Acoustic Accelerated Aging" in res5

    res6 = smart_sous_vide_thermocouple_core_calc(58.5, 40.0)
    assert "Smart Sous-Vide" in res6

    res7 = bio_fermented_ester_aroma_synthesizer("Saccharomyces cerevisiae", 22.0)
    assert "Bio-Fermented Ester" in res7

    res8 = laser_caramelization_surface_engraving(1500.0, 50.0)
    assert "Laser Surface Caramelization" in res8

    res9 = atmospheric_cold_plasma_food_sanitization(30.0, 5.0)
    assert "Cold Atmospheric Plasma" in res9

    res10 = high_pressure_processing_hpp_protein_denaturation(600.0, 3.0)
    assert "High-Pressure Processing" in res10


if __name__ == "__main__":
    pytest.main(["-v", __file__])
