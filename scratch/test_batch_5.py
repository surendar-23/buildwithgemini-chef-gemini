from app.tools import (
    flavor_aroma_network,
    plating_art_director,
    culinary_physics_calculator,
    fermentation_curing_planner,
    carbon_seasonal_evaluator,
    pantry_spoilage_alert,
    bakers_percentage_calc,
    wine_cellar_tracker,
    rapid_batch_prep_planner,
    global_spice_rub_crafter,
)

print("1. Testing flavor_aroma_network...")
t1 = flavor_aroma_network("Coffee", "Pork Belly")
print("Flavor Aroma Output:\n", t1[:200], "\n---")

print("2. Testing plating_art_director...")
t2 = plating_art_director("Pan-seared duck breast with cherry reduction and parsnip puree", style="fine-dining")
print("Plating Guide Output:\n", t2[:200], "\n---")

print("3. Testing culinary_physics_calculator...")
t3 = culinary_physics_calculator("Ribeye Steak", 1.5, "cast-iron")
print("Culinary Physics Output:\n", t3[:200], "\n---")

print("4. Testing fermentation_curing_planner...")
t4 = fermentation_curing_planner("kimchi", "Napa cabbage, daikon, garlic, Korean chili flakes, 2.5% sea salt")
print("Fermentation Planner Output:\n", t4[:200], "\n---")

print("5. Testing carbon_seasonal_evaluator...")
t5 = carbon_seasonal_evaluator("Strawberries, Avocados, Beef", "United States")
print("Carbon Evaluator Output:\n", t5[:200], "\n---")

print("6. Testing pantry_spoilage_alert...")
t6 = pantry_spoilage_alert(days_threshold=3)
print("Spoilage Alert Output:\n", t6[:200], "\n---")

print("7. Testing bakers_percentage_calc...")
t7 = bakers_percentage_calc(flour_weight_g=500.0, hydration_percent=78.0)
print("Baker's Percentage Output:\n", t7, "\n---")

print("8. Testing wine_cellar_tracker...")
t8 = wine_cellar_tracker("2018 Barolo with Truffle Risotto")
print("Wine Cellar Output:\n", t8[:200], "\n---")

print("9. Testing rapid_batch_prep_planner...")
t9 = rapid_batch_prep_planner("Chickpea Curry, Roasted Salmon, Quinoa Salad", target_time_hours=2.0)
print("Batch Prep Output:\n", t9[:200], "\n---")

print("10. Testing global_spice_rub_crafter...")
t10 = global_spice_rub_crafter("Ethiopian Berbere", heat_level="hot")
print("Spice Rub Output:\n", t10[:200])
