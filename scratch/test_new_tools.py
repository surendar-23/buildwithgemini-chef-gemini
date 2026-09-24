from app.tools import recommend_drink_pairing, calculate_recipe_nutrition, generate_shopping_list

print("1. Testing recommend_drink_pairing...")
r1 = recommend_drink_pairing("Grilled Salmon with lemon herbs", "wine")
print("Drink Pairing Output:\n", r1[:300], "\n---")

print("2. Testing calculate_recipe_nutrition...")
r2 = calculate_recipe_nutrition("2 avocados, 1 slice sourdough, 1 poached egg, olive oil")
print("Nutrition Output:\n", r2[:300], "\n---")

print("3. Testing generate_shopping_list...")
r3 = generate_shopping_list("chickpea-curry")
print("Shopping List Output:\n", r3[:300])
