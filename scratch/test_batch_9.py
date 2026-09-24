"""Unit tests for Batch 9 (Tools 101 to 200)."""

import pytest
import sys
from pathlib import Path

# Ensure app directory is in sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.agent import root_agent
from app.tools import (
    caviar_spherification_calcium_lactate,
    meat_glue_transglutaminase_binding,
    vacuum_compression_osmosis_fruit,
    ultrasonic_emulsification_cavitation,
    supercritical_fluid_flavor_extraction,
    enzymatic_meat_tenderization_papain,
    flash_freeze_liquid_nitrogen_shatter,
    hydrocolloid_syneresis_prevention,
    flavor_network_gas_chromatography,
    centrifugal_clarification_pectin,
    bread_hydration_bakers_percentage,
    croissant_butter_lamination_rheology,
    panettone_lievito_madre_acidity,
    macaronage_italian_meringue_viscosity,
    sugar_glass_isomalt_pulling,
    gelatin_bloom_conversion_matrix,
    choux_pastry_egg_absorption_index,
    chocolate_beta5_seeding_crystal,
    pastry_fat_crystallization_polymorph,
    souffle_albumen_foam_stiffening,
    wine_vintage_gdd_terroir_score,
    champagne_tirage_dosage_pressure,
    cider_tannin_acid_sugar_balance,
    bourbon_barrel_char_extraction,
    beer_hop_alpha_acid_ibu,
    cocktail_dilution_thermal_transfer,
    absinthe_louche_thujone_level,
    vermouth_botanical_steep_extract,
    soda_carbonation_volume_pressure,
    spirits_distillation_cut_fractions,
    mexican_nixtamalization_calcium_ratio,
    indian_tadka_fat_soluble_blooming,
    thai_curry_paste_aromatic_oil,
    ethiopian_injera_ersho_fermentation,
    italian_pasta_bronze_die_extrusion,
    spanish_paella_socarrat_bottom_heat,
    middle_eastern_halva_crystallization,
    japanese_ramen_tare_dashi_umami,
    french_mother_sauces_glace_matrix,
    georgian_khachapuri_suluguni_stretch,
    keto_net_carb_macro_ratio,
    fodmap_polyol_oligosaccharide_check,
    renal_potassium_phosphorus_leach,
    glycemic_index_load_glucose_response,
    endurance_carbo_load_glycogen,
    anti_inflammatory_polyphenol_index,
    histamine_intolerance_biogenic_amine,
    muscle_hypertrophy_leucine_threshold,
    diabetic_carb_exchange_insulin_unit,
    iddsi_texture_modified_diet_checker,
    ikejime_seafood_atp_preservation,
    dry_aged_beef_calpain_tenderization,
    whole_animal_nose_to_tail_yield,
    citrus_peel_oleo_saccharum_extract,
    seafood_sustainability_monterey_watch,
    spent_grain_upcycled_baking_flour,
    cascara_coffee_cherry_tisane_brew,
    cricket_flour_protein_incorporation,
    cell_cultivated_meat_searing_scaffold,
    food_waste_methane_landfill_offset,
    thermal_diffusivity_roast_joule,
    emulsion_droplet_size_stokes_law,
    starch_gelatinization_pasting_temp,
    caramelization_pyrolysis_temp_curve,
    maillard_reaction_reducing_sugar_ph,
    sous_vide_thermal_pasteurization_math,
    deep_frying_oil_degradation_tpm,
    bread_crumb_retrogradation_staling,
    ice_cream_freezing_point_depression,
    rheology_non_newtonian_fluid_yield,
    flavor_pairing_molecular_volatiles,
    umami_synergy_glutamate_inosinate,
    sensory_threshold_detection_triad,
    wine_cheese_tannin_fat_matching,
    coffee_extraction_yield_tds,
    tea_polyphenol_steep_temp_time,
    bitterness_masking_sodium_cyclamate,
    pungency_scoville_capsaicin_dilution,
    astringency_tannin_salivary_protein,
    kokumi_gamma_glutamyl_peptide_booster,
    recipe_batch_scaling_volume_surface,
    commercial_kitchen_prep_par_level,
    food_cost_margin_contribution_calc,
    haccp_critical_control_point_monitor,
    shelf_life_arrhenius_accelerated_test,
    cold_chain_temperature_excursion_eval,
    recipe_carbon_footprint_footprint,
    water_footprint_ingredient_scanner,
    menu_engineering_matrix_star_puzzle,
    food_allergen_cross_contamination_audit
)


def test_agent_tool_count():
    # Over 200 tools registered in root_agent
    assert len(root_agent.tools) >= 200, f"Expected >= 200 tools, got {len(root_agent.tools)}"


def test_molecular_gastronomy_tools():
    res1 = caviar_spherification_calcium_lactate(500.0)
    assert "Spherification" in res1

    res2 = meat_glue_transglutaminase_binding(1000.0)
    assert "Transglutaminase" in res2

    res3 = vacuum_compression_osmosis_fruit(250.0)
    assert "Vacuum Compression" in res3

    res4 = ultrasonic_emulsification_cavitation(300.0)
    assert "Ultrasonic Cavitation" in res4

    res5 = supercritical_fluid_flavor_extraction(100.0)
    assert "Supercritical CO2" in res5


def test_bakers_pastry_tools():
    res1 = bread_hydration_bakers_percentage(1000.0, 75.0)
    assert "Baker's Percentage" in res1

    res2 = croissant_butter_lamination_rheology(500.0)
    assert "Croissant" in res2

    res3 = chocolate_beta5_seeding_crystal(1000.0)
    assert "Chocolate Beta V" in res3

    res4 = gelatin_bloom_conversion_matrix(10.0, 200.0, 160.0)
    assert "Gelatin Bloom" in res4


def test_enology_beverage_tools():
    res1 = champagne_tirage_dosage_pressure(24.0)
    assert "Champagne" in res1

    res2 = beer_hop_alpha_acid_ibu(50.0, 12.0, 60.0, 20.0)
    assert "IBU" in res2

    res3 = coffee_extraction_yield_tds(1.35, 16.0)
    assert "Coffee Extraction" in res3


def test_clinical_nutrition_tools():
    res1 = keto_net_carb_macro_ratio(120.0, 40.0, 15.0, 5.0)
    assert "Ketogenic" in res1

    res2 = endurance_carbo_load_glycogen(70.0)
    assert "Glycogen" in res2

    res3 = food_cost_margin_contribution_calc(4.50, 18.00)
    assert "Food Cost" in res3


if __name__ == "__main__":
    pytest.main(["-v", __file__])
