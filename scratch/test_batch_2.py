from app.tools import generate_weekly_meal_plan, suggest_ingredient_substitutes, explain_cooking_technique

print("1. Testing generate_weekly_meal_plan...")
res1 = generate_weekly_meal_plan(days=3, dietary_goal="high-protein")
print("Meal Plan Output:\n", res1[:300], "\n---")

print("2. Testing suggest_ingredient_substitutes...")
res2 = suggest_ingredient_substitutes(ingredient="heavy cream", restriction_or_reason="dairy-free")
print("Substitute Output:\n", res2[:300], "\n---")

print("3. Testing explain_cooking_technique...")
res3 = explain_cooking_technique(technique_or_question="How to temper chocolate")
print("Technique Output:\n", res3[:300])
