from app.tools import (
    restaurant_menu_costing,
    tea_gongfu_water_pairing,
    freezing_point_depression_calc,
    charcuterie_board_designer,
    bbq_smoker_wood_science,
)

print("1. Testing restaurant_menu_costing...")
t1 = restaurant_menu_costing(18.50, target_fcp_percent=28.0, portion_count=2)
print("Menu Costing Output:\n", t1, "\n---")

print("2. Testing tea_gongfu_water_pairing...")
t2 = tea_gongfu_water_pairing("Raw Pu-erh", water_tds_ppm=85)
print("Gongfu Tea Output:\n", t2[:200], "\n---")

print("3. Testing freezing_point_depression_calc...")
t3 = freezing_point_depression_calc("120g sucrose, 30g dextrose, 550g whole milk, 120g heavy cream")
print("Gelato PAC/POD Output:\n", t3[:200], "\n---")

print("4. Testing charcuterie_board_designer...")
t4 = charcuterie_board_designer(board_size_people=8, dietary_notes="nut-free")
print("Charcuterie Board Output:\n", t4[:200], "\n---")

print("5. Testing bbq_smoker_wood_science...")
t5 = bbq_smoker_wood_science("Texas Beef Brisket", target_doneness_f=203.0)
print("BBQ Wood Science Output:\n", t5[:200])
