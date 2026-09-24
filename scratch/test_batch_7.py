from app.tools import (
    kitchen_brigade_station_planner,
    honey_terroir_pairing,
    heritage_grain_milling_calc,
    sake_seimai_buai_evaluator,
    evoo_polyphenol_evaluator,
    ancient_grain_sourdough_matrix,
    cacao_roasting_curve_evaluator,
    seaweed_umami_hydrocolloid_evaluator,
    wild_mushroom_culinary_guide,
    zero_proof_hydrosol_craft,
    charcuterie_nitrite_calculator,
    coffee_extraction_yield_calculator,
    mead_gravity_attenuation_calc,
    cheese_rind_affineur_guide,
    finishing_salt_mineralogy_evaluator,
)

print("16. Testing kitchen_brigade_station_planner...")
t16 = kitchen_brigade_station_planner("5-Course Fine Dining Gala", guest_count=150)
print("Brigade Output:\n", t16[:150], "\n---")

print("17. Testing honey_terroir_pairing...")
t17 = honey_terroir_pairing("Tupelo", "Aged Gouda")
print("Honey Output:\n", t17[:150], "\n---")

print("18. Testing heritage_grain_milling_calc...")
t18 = heritage_grain_milling_calc("Einkorn", 500.0)
print("Grain Output:\n", t18[:150], "\n---")

print("19. Testing sake_seimai_buai_evaluator...")
t19 = sake_seimai_buai_evaluator("Junmai Daiginjo", "chilled")
print("Sake Output:\n", t19[:150], "\n---")

print("20. Testing evoo_polyphenol_evaluator...")
t20 = evoo_polyphenol_evaluator("Picual", "Burrata Salad")
print("EVOO Output:\n", t20[:150], "\n---")

print("21. Testing ancient_grain_sourdough_matrix...")
t21 = ancient_grain_sourdough_matrix("50% Einkorn, 50% Bread Flour", 76.0)
print("Ancient Sourdough Output:\n", t21[:150], "\n---")

print("22. Testing cacao_roasting_curve_evaluator...")
t22 = cacao_roasting_curve_evaluator("Madagascar Sambirano", "medium")
print("Cacao Roast Output:\n", t22[:150], "\n---")

print("23. Testing seaweed_umami_hydrocolloid_evaluator...")
t23 = seaweed_umami_hydrocolloid_evaluator("Rishiri Kombu", "dashi-stock")
print("Seaweed Output:\n", t23[:150], "\n---")

print("24. Testing wild_mushroom_culinary_guide...")
t24 = wild_mushroom_culinary_guide("Morel", "duck-fat")
print("Wild Mushroom Output:\n", t24[:150], "\n---")

print("25. Testing zero_proof_hydrosol_craft...")
t25 = zero_proof_hydrosol_craft("London Dry Botanical", "medium")
print("Zero Proof Output:\n", t25[:150], "\n---")

print("26. Testing charcuterie_nitrite_calculator...")
t26 = charcuterie_nitrite_calculator(3.0, "dry-cured-salumi-cure2")
print("Nitrite Output:\n", t26, "\n---")

print("27. Testing coffee_extraction_yield_calculator...")
t27 = coffee_extraction_yield_calculator(18.0, 300.0, 1.38)
print("Coffee EY Output:\n", t27, "\n---")

print("28. Testing mead_gravity_attenuation_calc...")
t28 = mead_gravity_attenuation_calc(3.5, 10.0)
print("Mead Gravity Output:\n", t28, "\n---")

print("29. Testing cheese_rind_affineur_guide...")
t29 = cheese_rind_affineur_guide("Taleggio / Washed Rind", "brevibacterium-linens")
print("Cheese Affineur Output:\n", t29[:150], "\n---")

print("30. Testing finishing_salt_mineralogy_evaluator...")
t30 = finishing_salt_mineralogy_evaluator("Maldon Flake", "Ribeye Steak")
print("Finishing Salt Output:\n", t30[:150])
