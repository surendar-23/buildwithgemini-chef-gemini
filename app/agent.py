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
    absinthe_thujone_louche_effect,
    add_pantry_item,
    ancient_grain_sourdough_matrix,
    anti_inflammatory_polyphenol_diet,
    aquacultured_seafood_sustainability,
    bakers_percentage_calc,
    banquet_kitchen_operations,
    bbq_smoker_wood_science,
    beer_hop_alpha_acid_ibu_calc,
    black_garlic_maillard_chamber,
    cacao_roasting_curve_evaluator,
    calculate_recipe_nutrition,
    cannele_beeswax_copper_mold_guide,
    carbon_seasonal_evaluator,
    cell_cultivated_meat_media_evaluator,
    champagne_methode_traditionnelle_calc,
    charcuterie_board_designer,
    charcuterie_nitrite_calculator,
    check_pantry_for_recipe,
    cheese_rind_affineur_guide,
    chocolate_tempering_crystal_polymorph,
    choux_pastry_egg_absorption_index,
    cider_apple_tannin_acid_balance,
    clarified_consomme_centrifuge_gel,
    clinical_dietary_matrix,
    cocktail_ice_dilution_thermodynamics,
    coffee_cherry_cascara_upcycled_beverage,
    coffee_extraction_yield_calculator,
    create_fusion_recipe,
    croissant_lamination_butter_block,
    cryogenic_liquid_nitrogen_shatter,
    culinary_physics_calculator,
    curing_chamber_psychrometrics,
    diabetic_carbohydrate_exchange_calc,
    distillery_cuts_heads_hearts_tails,
    dry_aged_beef_enzymatic_tenderization,
    edible_insect_cricket_flour_protein,
    endurance_carbo_loading_glycogen,
    estimate_grocery_budget,
    ethiopian_injera_ersho_ferment,
    evoo_polyphenol_evaluator,
    execute_custom_culinary_skill,
    explain_cooking_technique,
    fermentation_curing_planner,
    find_nearby_places,
    finishing_salt_mineralogy_evaluator,
    flavor_aroma_network,
    fluid_gel_shear_hydrocolloid,
    foam_emulsion_lecithin_stabilizer,
    fodmap_polyol_oligosaccharide_scanner,
    food_waste_compost_methane_offset,
    freezing_point_depression_calc,
    french_mother_sauces_reduction_matrix,
    garum_amino_acid_hydrolysis,
    gelatin_bloom_strength_converter,
    generate_dish_image,
    generate_dish_video,
    generate_shopping_list,
    generate_weekly_meal_plan,
    geocode_address,
    georgian_khachapuri_cheese_blend,
    get_pantry_items,
    global_spice_rub_crafter,
    glycemic_index_load_blood_glucose,
    heritage_grain_milling_calc,
    histamine_intolerance_biogenic_amines,
    honey_terroir_pairing,
    hypertrophy_leucine_trigger_protein,
    ikejime_fish_quality_brain_spike,
    indian_tadka_spice_blooming_order,
    italian_pasta_extrusion_bronze_die,
    japanese_ramen_tare_dashi_matching,
    ketogenic_net_carb_macro_evaluator,
    kimchi_leuconostoc_fermentation,
    kitchen_brigade_station_planner,
    koji_kin_grain_inoculator,
    kombucha_scoby_symbiosis_evaluator,
    lacto_fermentation_salinity_calc,
    lookup_global_recipes,
    macaron_macaronage_viscosity_guide,
    mead_gravity_attenuation_calc,
    mexican_nixtamalization_masa_calc,
    middle_eastern_tahini_halva_crystallizer,
    mixology_guide,
    molecular_gastronomy_engine,
    panettone_pasta_madre_ph_manager,
    pantry_spoilage_alert,
    plating_art_director,
    post_op_soft_blended_texture_diet,
    praline_nut_caramel_gianduja_calc,
    rapid_batch_prep_planner,
    recommend_drink_pairing,
    renal_dietary_potassium_phosphorus,
    restaurant_menu_costing,
    rotary_evaporator_flavor_distill,
    sake_seimai_buai_evaluator,
    search_recipes,
    seaweed_umami_hydrocolloid_evaluator,
    soda_carbonation_volume_pressure,
    souffle_egg_white_foam_stabilizer,
    sous_vide_pasteurization_log_reducer,
    spanish_paella_socarrat_fire_control,
    spent_grain_upcycled_flour_baking,
    spherification_calcium_bath_calc,
    spirits_barrel_char_aging_evaluator,
    sugar_caramelization_stage_thermometer,
    suggest_ingredient_substitutes,
    tea_gongfu_water_pairing,
    tempeh_rhizopus_oligosporus_planner,
    terroir_wine_vintage_weather_evaluator,
    thai_curry_paste_mortar_pestle,
    transform_leftovers,
    translucent_edible_film_crafter,
    transglutaminase_meat_glue_dosing,
    tsukemono_nukazuke_bed_manager,
    ultrasonic_homogenizer_emulsion,
    universal_culinary_encyclopedia,
    vermouth_botanical_fortification,
    vinegar_acetobacter_acidification,
    wild_mushroom_culinary_guide,
    wine_cellar_tracker,
    whole_animal_nose_to_tail_utilization,
    zero_proof_hydrosol_craft,
    zero_waste_citrus_peel_oleo_saccharum,
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
    food_allergen_cross_contamination_audit,
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
        absinthe_thujone_louche_effect,
        add_pantry_item,
        ancient_grain_sourdough_matrix,
        anti_inflammatory_polyphenol_diet,
        aquacultured_seafood_sustainability,
        bakers_percentage_calc,
        banquet_kitchen_operations,
        bbq_smoker_wood_science,
        beer_hop_alpha_acid_ibu_calc,
        black_garlic_maillard_chamber,
        cacao_roasting_curve_evaluator,
        calculate_recipe_nutrition,
        cannele_beeswax_copper_mold_guide,
        carbon_seasonal_evaluator,
        cell_cultivated_meat_media_evaluator,
        champagne_methode_traditionnelle_calc,
        charcuterie_board_designer,
        charcuterie_nitrite_calculator,
        check_pantry_for_recipe,
        cheese_rind_affineur_guide,
        chocolate_tempering_crystal_polymorph,
        choux_pastry_egg_absorption_index,
        cider_apple_tannin_acid_balance,
        clarified_consomme_centrifuge_gel,
        clinical_dietary_matrix,
        cocktail_ice_dilution_thermodynamics,
        coffee_cherry_cascara_upcycled_beverage,
        coffee_extraction_yield_calculator,
        create_fusion_recipe,
        croissant_lamination_butter_block,
        cryogenic_liquid_nitrogen_shatter,
        culinary_physics_calculator,
        curing_chamber_psychrometrics,
        diabetic_carbohydrate_exchange_calc,
        distillery_cuts_heads_hearts_tails,
        dry_aged_beef_enzymatic_tenderization,
        edible_insect_cricket_flour_protein,
        endurance_carbo_loading_glycogen,
        estimate_grocery_budget,
        ethiopian_injera_ersho_ferment,
        evoo_polyphenol_evaluator,
        execute_custom_culinary_skill,
        explain_cooking_technique,
        fermentation_curing_planner,
        find_nearby_places,
        finishing_salt_mineralogy_evaluator,
        flavor_aroma_network,
        fluid_gel_shear_hydrocolloid,
        foam_emulsion_lecithin_stabilizer,
        fodmap_polyol_oligosaccharide_scanner,
        food_waste_compost_methane_offset,
        freezing_point_depression_calc,
        french_mother_sauces_reduction_matrix,
        garum_amino_acid_hydrolysis,
        gelatin_bloom_strength_converter,
        generate_dish_image,
        generate_dish_video,
        generate_shopping_list,
        generate_weekly_meal_plan,
        geocode_address,
        georgian_khachapuri_cheese_blend,
        get_pantry_items,
        global_spice_rub_crafter,
        glycemic_index_load_blood_glucose,
        heritage_grain_milling_calc,
        histamine_intolerance_biogenic_amines,
        honey_terroir_pairing,
        hypertrophy_leucine_trigger_protein,
        ikejime_fish_quality_brain_spike,
        indian_tadka_spice_blooming_order,
        italian_pasta_extrusion_bronze_die,
        japanese_ramen_tare_dashi_matching,
        ketogenic_net_carb_macro_evaluator,
        kimchi_leuconostoc_fermentation,
        kitchen_brigade_station_planner,
        koji_kin_grain_inoculator,
        kombucha_scoby_symbiosis_evaluator,
        lacto_fermentation_salinity_calc,
        lookup_global_recipes,
        macaron_macaronage_viscosity_guide,
        mead_gravity_attenuation_calc,
        mexican_nixtamalization_masa_calc,
        middle_eastern_tahini_halva_crystallizer,
        mixology_guide,
        molecular_gastronomy_engine,
        panettone_pasta_madre_ph_manager,
        pantry_spoilage_alert,
        plating_art_director,
        post_op_soft_blended_texture_diet,
        praline_nut_caramel_gianduja_calc,
        rapid_batch_prep_planner,
        recommend_drink_pairing,
        renal_dietary_potassium_phosphorus,
        restaurant_menu_costing,
        rotary_evaporator_flavor_distill,
        sake_seimai_buai_evaluator,
        search_recipes,
        seaweed_umami_hydrocolloid_evaluator,
        soda_carbonation_volume_pressure,
        souffle_egg_white_foam_stabilizer,
        sous_vide_pasteurization_log_reducer,
        spanish_paella_socarrat_fire_control,
        spent_grain_upcycled_flour_baking,
        spherification_calcium_bath_calc,
        spirits_barrel_char_aging_evaluator,
        sugar_caramelization_stage_thermometer,
        suggest_ingredient_substitutes,
        tea_gongfu_water_pairing,
        tempeh_rhizopus_oligosporus_planner,
        terroir_wine_vintage_weather_evaluator,
        thai_curry_paste_mortar_pestle,
        transform_leftovers,
        translucent_edible_film_crafter,
        transglutaminase_meat_glue_dosing,
        tsukemono_nukazuke_bed_manager,
        ultrasonic_homogenizer_emulsion,
        universal_culinary_encyclopedia,
        vermouth_botanical_fortification,
        vinegar_acetobacter_acidification,
        wild_mushroom_culinary_guide,
        wine_cellar_tracker,
        whole_animal_nose_to_tail_utilization,
        zero_proof_hydrosol_craft,
        zero_waste_citrus_peel_oleo_saccharum,
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
        food_allergen_cross_contamination_audit,
    ],
    after_agent_callback=generate_memories_callback,
    after_model_callback=a2ui_callback,
)

app = App(
    root_agent=root_agent,
    name="app",
)



