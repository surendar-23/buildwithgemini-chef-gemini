# ruff: noqa
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
from zoneinfo import ZoneInfo

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types


def get_weather(query: str) -> str:
    """Simulates a web search. Use it get information on weather.

    Args:
        query: A string containing the location to get weather information for.

    Returns:
        A string with the simulated weather information for the queried location.
    """
    if "sf" in query.lower() or "san francisco" in query.lower():
        return "It's 60 degrees and foggy."
    return "It's 90 degrees and sunny."


def get_current_time(query: str) -> str:
    """Simulates getting the current time for a city.

    Args:
        city: The name of the city to get the current time for.

    Returns:
        A string with the current time information.
    """
    if "sf" in query.lower() or "san francisco" in query.lower():
        tz_identifier = "America/Los_Angeles"
    else:
        return f"Sorry, I don't have timezone information for query: {query}."

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    return f"The current time for query {query} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"


from a2ui.basic_catalog.provider import BasicCatalog
from a2ui.schema.manager import A2uiSchemaManager
from google.adk.agents.callback_context import CallbackContext
from google.adk.memory import VertexAiMemoryBankService
from google.adk.tools.preload_memory_tool import PreloadMemoryTool

from app.a2ui_utils import a2ui_callback
from app.tools import (
    absinthe_louche_thujone_level,
    absinthe_thujone_louche_effect,
    acoustic_levitation_contactless_dehydration,
    add_pantry_item,
    ancient_grain_sourdough_matrix,
    anti_inflammatory_polyphenol_diet,
    anti_inflammatory_polyphenol_index,
    aquacultured_seafood_sustainability,
    astringency_tannin_salivary_protein,
    atmospheric_cold_plasma_food_sanitization,
    bakers_percentage_calc,
    banquet_kitchen_operations,
    bbq_smoker_wood_science,
    beer_hop_alpha_acid_ibu,
    beer_hop_alpha_acid_ibu_calc,
    calculate_aroma_volatile_pairing,
    verify_haccp_critical_control_point,
    bio_fermented_ester_aroma_synthesizer,
    bitterness_masking_sodium_cyclamate,
    black_garlic_maillard_chamber,
    bourbon_barrel_char_extraction,
    bread_crumb_retrogradation_staling,
    bread_hydration_bakers_percentage,
    cacao_roasting_curve_evaluator,
    calculate_recipe_nutrition,
    cannele_beeswax_copper_mold_guide,
    caramelization_pyrolysis_temp_curve,
    carbon_seasonal_evaluator,
    cascara_coffee_cherry_tisane_brew,
    caviar_spherification_calcium_lactate,
    cell_cultivated_meat_media_evaluator,
    cell_cultivated_meat_searing_scaffold,
    centrifugal_clarification_pectin,
    champagne_methode_traditionnelle_calc,
    champagne_tirage_dosage_pressure,
    charcuterie_board_designer,
    charcuterie_nitrite_calculator,
    check_pantry_for_recipe,
    cheese_rind_affineur_guide,
    chocolate_beta5_seeding_crystal,
    chocolate_tempering_crystal_polymorph,
    choux_pastry_egg_absorption_index,
    cider_apple_tannin_acid_balance,
    cider_tannin_acid_sugar_balance,
    citrus_peel_oleo_saccharum_extract,
    clarified_consomme_centrifuge_gel,
    clinical_dietary_matrix,
    cocktail_dilution_thermal_transfer,
    cocktail_ice_dilution_thermodynamics,
    coffee_cherry_cascara_upcycled_beverage,
    coffee_extraction_yield_calculator,
    coffee_extraction_yield_tds,
    cold_chain_temperature_excursion_eval,
    commercial_kitchen_prep_par_level,
    create_fusion_recipe,
    cricket_flour_protein_incorporation,
    croissant_butter_lamination_rheology,
    croissant_lamination_butter_block,
    cryogenic_liquid_nitrogen_shatter,
    culinary_physics_calculator,
    curing_chamber_psychrometrics,
    deep_frying_oil_degradation_tpm,
    diabetic_carb_exchange_insulin_unit,
    diabetic_carbohydrate_exchange_calc,
    distillery_cuts_heads_hearts_tails,
    dry_aged_beef_calpain_tenderization,
    dry_aged_beef_enzymatic_tenderization,
    edible_insect_cricket_flour_protein,
    emulsion_droplet_size_stokes_law,
    endurance_carbo_load_glycogen,
    endurance_carbo_loading_glycogen,
    enzymatic_meat_tenderization_papain,
    estimate_grocery_budget,
    ethiopian_injera_ersho_ferment,
    ethiopian_injera_ersho_fermentation,
    evoo_polyphenol_evaluator,
    execute_custom_culinary_skill,
    explain_cooking_technique,
    fermentation_curing_planner,
    find_nearby_places,
    finishing_salt_mineralogy_evaluator,
    flash_freeze_liquid_nitrogen_shatter,
    flavor_aroma_network,
    flavor_network_gas_chromatography,
    flavor_pairing_molecular_volatiles,
    fluid_gel_shear_hydrocolloid,
    foam_emulsion_lecithin_stabilizer,
    fodmap_polyol_oligosaccharide_check,
    fodmap_polyol_oligosaccharide_scanner,
    food_allergen_cross_contamination_audit,
    food_cost_margin_contribution_calc,
    food_printing_3d_rheology_shear_rate,
    food_waste_compost_methane_offset,
    food_waste_methane_landfill_offset,
    freezing_point_depression_calc,
    french_mother_sauces_glace_matrix,
    french_mother_sauces_reduction_matrix,
    garum_amino_acid_hydrolysis,
    gelatin_bloom_conversion_matrix,
    gelatin_bloom_strength_converter,
    generate_dish_image,
    generate_dish_video,
    generate_shopping_list,
    generate_weekly_meal_plan,
    geocode_address,
    georgian_khachapuri_cheese_blend,
    georgian_khachapuri_suluguni_stretch,
    get_pantry_items,
    global_spice_rub_crafter,
    glycemic_index_load_blood_glucose,
    glycemic_index_load_glucose_response,
    haccp_critical_control_point_monitor,
    heritage_grain_milling_calc,
    high_pressure_processing_hpp_protein_denaturation,
    histamine_intolerance_biogenic_amine,
    histamine_intolerance_biogenic_amines,
    honey_terroir_pairing,
    hydrocolloid_syneresis_prevention,
    hypertrophy_leucine_trigger_protein,
    ice_cream_freezing_point_depression,
    iddsi_texture_modified_diet_checker,
    ikejime_fish_quality_brain_spike,
    ikejime_seafood_atp_preservation,
    indian_tadka_fat_soluble_blooming,
    indian_tadka_spice_blooming_order,
    italian_pasta_bronze_die_extrusion,
    italian_pasta_extrusion_bronze_die,
    japanese_ramen_tare_dashi_matching,
    japanese_ramen_tare_dashi_umami,
    keto_net_carb_macro_ratio,
    ketogenic_net_carb_macro_evaluator,
    kimchi_leuconostoc_fermentation,
    kitchen_brigade_station_planner,
    koji_kin_grain_inoculator,
    kokumi_gamma_glutamyl_peptide_booster,
    kombucha_scoby_symbiosis_evaluator,
    lacto_fermentation_salinity_calc,
    laser_caramelization_surface_engraving,
    lookup_global_recipes,
    macaron_macaronage_viscosity_guide,
    macaronage_italian_meringue_viscosity,
    maillard_reaction_reducing_sugar_ph,
    mead_gravity_attenuation_calc,
    meat_glue_transglutaminase_binding,
    menu_engineering_matrix_star_puzzle,
    mexican_nixtamalization_calcium_ratio,
    mexican_nixtamalization_masa_calc,
    middle_eastern_halva_crystallization,
    middle_eastern_tahini_halva_crystallizer,
    mixology_guide,
    molecular_gastronomy_engine,
    muscle_hypertrophy_leucine_threshold,
    mycelium_fermentation_scaffold_density,
    panettone_lievito_madre_acidity,
    panettone_pasta_madre_ph_manager,
    pantry_spoilage_alert,
    pastry_fat_crystallization_polymorph,
    plating_art_director,
    post_op_soft_blended_texture_diet,
    praline_nut_caramel_gianduja_calc,
    pulsed_electric_field_pef_cell_permeabilization,
    pungency_scoville_capsaicin_dilution,
    rapid_batch_prep_planner,
    recipe_batch_scaling_volume_surface,
    recipe_carbon_footprint_footprint,
    recommend_drink_pairing,
    renal_dietary_potassium_phosphorus,
    renal_potassium_phosphorus_leach,
    restaurant_menu_costing,
    rheology_non_newtonian_fluid_yield,
    rotary_evaporator_flavor_distill,
    sake_seimai_buai_evaluator,
    seafood_sustainability_monterey_watch,
    search_recipes,
    seaweed_umami_hydrocolloid_evaluator,
    sensory_threshold_detection_triad,
    shelf_life_arrhenius_accelerated_test,
    smart_sous_vide_thermocouple_core_calc,
    soda_carbonation_volume_pressure,
    sonic_acoustic_spirits_accelerated_aging,
    souffle_albumen_foam_stiffening,
    souffle_egg_white_foam_stabilizer,
    sous_vide_pasteurization_log_reducer,
    sous_vide_thermal_pasteurization_math,
    spanish_paella_socarrat_bottom_heat,
    spanish_paella_socarrat_fire_control,
    spent_grain_upcycled_baking_flour,
    spent_grain_upcycled_flour_baking,
    spherification_calcium_bath_calc,
    spirits_barrel_char_aging_evaluator,
    spirits_distillation_cut_fractions,
    starch_gelatinization_pasting_temp,
    sugar_caramelization_stage_thermometer,
    sugar_glass_isomalt_pulling,
    suggest_ingredient_substitutes,
    supercritical_fluid_flavor_extraction,
    tea_gongfu_water_pairing,
    tea_polyphenol_steep_temp_time,
    tempeh_rhizopus_oligosporus_planner,
    terroir_wine_vintage_weather_evaluator,
    thai_curry_paste_aromatic_oil,
    thai_curry_paste_mortar_pestle,
    thermal_diffusivity_roast_joule,
    transform_leftovers,
    transglutaminase_meat_glue_dosing,
    translucent_edible_film_crafter,
    tsukemono_nukazuke_bed_manager,
    ultrasonic_emulsification_cavitation,
    ultrasonic_homogenizer_emulsion,
    umami_synergy_glutamate_inosinate,
    universal_culinary_encyclopedia,
    vacuum_compression_osmosis_fruit,
    vermouth_botanical_fortification,
    vermouth_botanical_steep_extract,
    vinegar_acetobacter_acidification,
    water_footprint_ingredient_scanner,
    whole_animal_nose_to_tail_utilization,
    whole_animal_nose_to_tail_yield,
    wild_mushroom_culinary_guide,
    wine_cellar_tracker,
    wine_cheese_tannin_fat_matching,
    wine_vintage_gdd_terroir_score,
    zero_proof_hydrosol_craft,
    zero_waste_citrus_peel_oleo_saccharum,
)




schema_manager = A2uiSchemaManager(
    version="0.8",
    catalogs=[BasicCatalog.get_config("0.8")],
)

instruction = schema_manager.generate_system_prompt(
    role_description=(
        "You are Chef Gemini, an elite culinary concierge with 100+ specialized domain tools and universal culinary authority. "
        "Always remember and strictly adhere to all user allergies, dietary restrictions, and food preferences stated across past or current conversations. "
        "Use your memory to filter recipes, verify pantry safety, and personalize meal planning accordingly. "
        "Help users with 200+ global regional cuisines, clinical & therapeutic nutrition matrices (IDDSI, Renal, Ketogenic, Glycemic Index, FODMAP, Histamine, Hypertrophy Leucine Trigger), "
        "molecular gastronomy & hydrocolloid rheology, koji & garum & lacto fermentation schedules, spirits aging & cold rotovap distillation, pastry crystal polymorphs, "
        "sourdough pasta madre, authentic nixtamalization, tadka blooming, socarrat, ikejime fish harvesting, dry aging beef, whole animal nose-to-tail, and zero-waste upcycling."
    ),
    workflow_description="Analyze the user request and return structured UI when appropriate.",
    ui_description=(
        "Keep every surface tiny and flat: ONE Card > ONE Column > a few Text rows. "
        "Never nest a Card inside a Card. "
        "Use ONLY these components: Card, Column, Row, Text, and Image. Do not use "
        "Table or Heading (unsupported), or Buttons, actions, or forms (they do "
        "nothing in adk web). "
        "You may include one Image component, but only when you have a public https "
        "URL for the image (for example the URL an image tool returns after uploading "
        "to a public bucket). Set the Image url to that exact https link, for example "
        '{"Image": {"url": {"literalString": "https://..."}}}. Never point an '
        "Image at a bare filename, an artifact name, or a non-http(s) path. If you do "
        "not have a public URL, add a short Text line noting the image or video instead. "
        "No markdown in text; use the usageHint property ('h1', 'h2', 'body') for "
        "headings and emphasis. "
        "Output ONLY the raw A2UI JSON array — no prose, and never wrap it in "
        "<a2a_datapart_json> tags or 'kind'/'data'/'metadata' objects."
    ),
    include_schema=True,
    include_examples=True,
)


async def generate_memories_callback(callback_context: CallbackContext):
    try:
        await callback_context.add_session_to_memory()
    except Exception as e:
        print(f"Warning: add_session_to_memory skipped or unavailable: {e}")
    return None


def memory_service_builder():
    return VertexAiMemoryBankService(
        project="qwiklabs-gcp-02-8b55424b019a",
        location="us-east1",
        agent_engine_id="1765615563092000768",
    )


root_agent = Agent(
    name="root_agent",
    model=Gemini(
        model="gemini-flash-latest",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=instruction,
    tools=[
        PreloadMemoryTool(),
        absinthe_louche_thujone_level,
        absinthe_thujone_louche_effect,
        acoustic_levitation_contactless_dehydration,
        add_pantry_item,
        ancient_grain_sourdough_matrix,
        anti_inflammatory_polyphenol_diet,
        anti_inflammatory_polyphenol_index,
        aquacultured_seafood_sustainability,
        astringency_tannin_salivary_protein,
        atmospheric_cold_plasma_food_sanitization,
        bakers_percentage_calc,
        banquet_kitchen_operations,
        bbq_smoker_wood_science,
        beer_hop_alpha_acid_ibu,
        beer_hop_alpha_acid_ibu_calc,
        calculate_aroma_volatile_pairing,
        verify_haccp_critical_control_point,
        bio_fermented_ester_aroma_synthesizer,
        bitterness_masking_sodium_cyclamate,
        black_garlic_maillard_chamber,
        bourbon_barrel_char_extraction,
        bread_crumb_retrogradation_staling,
        bread_hydration_bakers_percentage,
        cacao_roasting_curve_evaluator,
        calculate_recipe_nutrition,
        cannele_beeswax_copper_mold_guide,
        caramelization_pyrolysis_temp_curve,
        carbon_seasonal_evaluator,
        cascara_coffee_cherry_tisane_brew,
        caviar_spherification_calcium_lactate,
        cell_cultivated_meat_media_evaluator,
        cell_cultivated_meat_searing_scaffold,
        centrifugal_clarification_pectin,
        champagne_methode_traditionnelle_calc,
        champagne_tirage_dosage_pressure,
        charcuterie_board_designer,
        charcuterie_nitrite_calculator,
        check_pantry_for_recipe,
        cheese_rind_affineur_guide,
        chocolate_beta5_seeding_crystal,
        chocolate_tempering_crystal_polymorph,
        choux_pastry_egg_absorption_index,
        cider_apple_tannin_acid_balance,
        cider_tannin_acid_sugar_balance,
        citrus_peel_oleo_saccharum_extract,
        clarified_consomme_centrifuge_gel,
        clinical_dietary_matrix,
        cocktail_dilution_thermal_transfer,
        cocktail_ice_dilution_thermodynamics,
        coffee_cherry_cascara_upcycled_beverage,
        coffee_extraction_yield_calculator,
        coffee_extraction_yield_tds,
        cold_chain_temperature_excursion_eval,
        commercial_kitchen_prep_par_level,
        create_fusion_recipe,
        cricket_flour_protein_incorporation,
        croissant_butter_lamination_rheology,
        croissant_lamination_butter_block,
        cryogenic_liquid_nitrogen_shatter,
        culinary_physics_calculator,
        curing_chamber_psychrometrics,
        deep_frying_oil_degradation_tpm,
        diabetic_carb_exchange_insulin_unit,
        diabetic_carbohydrate_exchange_calc,
        distillery_cuts_heads_hearts_tails,
        dry_aged_beef_calpain_tenderization,
        dry_aged_beef_enzymatic_tenderization,
        edible_insect_cricket_flour_protein,
        emulsion_droplet_size_stokes_law,
        endurance_carbo_load_glycogen,
        endurance_carbo_loading_glycogen,
        enzymatic_meat_tenderization_papain,
        estimate_grocery_budget,
        ethiopian_injera_ersho_ferment,
        ethiopian_injera_ersho_fermentation,
        evoo_polyphenol_evaluator,
        execute_custom_culinary_skill,
        explain_cooking_technique,
        fermentation_curing_planner,
        find_nearby_places,
        finishing_salt_mineralogy_evaluator,
        flash_freeze_liquid_nitrogen_shatter,
        flavor_aroma_network,
        flavor_network_gas_chromatography,
        flavor_pairing_molecular_volatiles,
        fluid_gel_shear_hydrocolloid,
        foam_emulsion_lecithin_stabilizer,
        fodmap_polyol_oligosaccharide_check,
        fodmap_polyol_oligosaccharide_scanner,
        food_allergen_cross_contamination_audit,
        food_cost_margin_contribution_calc,
        food_printing_3d_rheology_shear_rate,
        food_waste_compost_methane_offset,
        food_waste_methane_landfill_offset,
        freezing_point_depression_calc,
        french_mother_sauces_glace_matrix,
        french_mother_sauces_reduction_matrix,
        garum_amino_acid_hydrolysis,
        gelatin_bloom_conversion_matrix,
        gelatin_bloom_strength_converter,
        generate_dish_image,
        generate_dish_video,
        generate_shopping_list,
        generate_weekly_meal_plan,
        geocode_address,
        georgian_khachapuri_cheese_blend,
        georgian_khachapuri_suluguni_stretch,
        get_pantry_items,
        global_spice_rub_crafter,
        glycemic_index_load_blood_glucose,
        glycemic_index_load_glucose_response,
        haccp_critical_control_point_monitor,
        heritage_grain_milling_calc,
        high_pressure_processing_hpp_protein_denaturation,
        histamine_intolerance_biogenic_amine,
        histamine_intolerance_biogenic_amines,
        honey_terroir_pairing,
        hydrocolloid_syneresis_prevention,
        hypertrophy_leucine_trigger_protein,
        ice_cream_freezing_point_depression,
        iddsi_texture_modified_diet_checker,
        ikejime_fish_quality_brain_spike,
        ikejime_seafood_atp_preservation,
        indian_tadka_fat_soluble_blooming,
        indian_tadka_spice_blooming_order,
        italian_pasta_bronze_die_extrusion,
        italian_pasta_extrusion_bronze_die,
        japanese_ramen_tare_dashi_matching,
        japanese_ramen_tare_dashi_umami,
        keto_net_carb_macro_ratio,
        ketogenic_net_carb_macro_evaluator,
        kimchi_leuconostoc_fermentation,
        kitchen_brigade_station_planner,
        koji_kin_grain_inoculator,
        kokumi_gamma_glutamyl_peptide_booster,
        kombucha_scoby_symbiosis_evaluator,
        lacto_fermentation_salinity_calc,
        laser_caramelization_surface_engraving,
        lookup_global_recipes,
        macaron_macaronage_viscosity_guide,
        macaronage_italian_meringue_viscosity,
        maillard_reaction_reducing_sugar_ph,
        mead_gravity_attenuation_calc,
        meat_glue_transglutaminase_binding,
        menu_engineering_matrix_star_puzzle,
        mexican_nixtamalization_calcium_ratio,
        mexican_nixtamalization_masa_calc,
        middle_eastern_halva_crystallization,
        middle_eastern_tahini_halva_crystallizer,
        mixology_guide,
        molecular_gastronomy_engine,
        muscle_hypertrophy_leucine_threshold,
        mycelium_fermentation_scaffold_density,
        panettone_lievito_madre_acidity,
        panettone_pasta_madre_ph_manager,
        pantry_spoilage_alert,
        pastry_fat_crystallization_polymorph,
        plating_art_director,
        post_op_soft_blended_texture_diet,
        praline_nut_caramel_gianduja_calc,
        pulsed_electric_field_pef_cell_permeabilization,
        pungency_scoville_capsaicin_dilution,
        rapid_batch_prep_planner,
        recipe_batch_scaling_volume_surface,
        recipe_carbon_footprint_footprint,
        recommend_drink_pairing,
        renal_dietary_potassium_phosphorus,
        renal_potassium_phosphorus_leach,
        restaurant_menu_costing,
        rheology_non_newtonian_fluid_yield,
        rotary_evaporator_flavor_distill,
        sake_seimai_buai_evaluator,
        seafood_sustainability_monterey_watch,
        search_recipes,
        seaweed_umami_hydrocolloid_evaluator,
        sensory_threshold_detection_triad,
        shelf_life_arrhenius_accelerated_test,
        smart_sous_vide_thermocouple_core_calc,
        soda_carbonation_volume_pressure,
        sonic_acoustic_spirits_accelerated_aging,
        souffle_albumen_foam_stiffening,
        souffle_egg_white_foam_stabilizer,
        sous_vide_pasteurization_log_reducer,
        sous_vide_thermal_pasteurization_math,
        spanish_paella_socarrat_bottom_heat,
        spanish_paella_socarrat_fire_control,
        spent_grain_upcycled_baking_flour,
        spent_grain_upcycled_flour_baking,
        spherification_calcium_bath_calc,
        spirits_barrel_char_aging_evaluator,
        spirits_distillation_cut_fractions,
        starch_gelatinization_pasting_temp,
        sugar_caramelization_stage_thermometer,
        sugar_glass_isomalt_pulling,
        suggest_ingredient_substitutes,
        supercritical_fluid_flavor_extraction,
        tea_gongfu_water_pairing,
        tea_polyphenol_steep_temp_time,
        tempeh_rhizopus_oligosporus_planner,
        terroir_wine_vintage_weather_evaluator,
        thai_curry_paste_aromatic_oil,
        thai_curry_paste_mortar_pestle,
        thermal_diffusivity_roast_joule,
        transform_leftovers,
        transglutaminase_meat_glue_dosing,
        translucent_edible_film_crafter,
        tsukemono_nukazuke_bed_manager,
        ultrasonic_emulsification_cavitation,
        ultrasonic_homogenizer_emulsion,
        umami_synergy_glutamate_inosinate,
        universal_culinary_encyclopedia,
        vacuum_compression_osmosis_fruit,
        vermouth_botanical_fortification,
        vermouth_botanical_steep_extract,
        vinegar_acetobacter_acidification,
        water_footprint_ingredient_scanner,
        whole_animal_nose_to_tail_utilization,
        whole_animal_nose_to_tail_yield,
        wild_mushroom_culinary_guide,
        wine_cellar_tracker,
        wine_cheese_tannin_fat_matching,
        wine_vintage_gdd_terroir_score,
        zero_proof_hydrosol_craft,
        zero_waste_citrus_peel_oleo_saccharum,
    ],
    after_agent_callback=generate_memories_callback,
    after_model_callback=a2ui_callback,
)

app = App(
    root_agent=root_agent,
    name="app",
)



