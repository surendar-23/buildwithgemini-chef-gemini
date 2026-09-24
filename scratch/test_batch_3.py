from app.tools import transform_leftovers, create_fusion_recipe, estimate_grocery_budget, mixology_guide

print("1. Testing transform_leftovers...")
r1 = transform_leftovers("half roasted chicken, 1 cup cooked white rice, wilted spinach, lemon")
print("Leftover Recipe:\n", r1[:250], "\n---")

print("2. Testing create_fusion_recipe...")
r2 = create_fusion_recipe("Mexican", "Japanese")
print("Fusion Recipe:\n", r2[:250], "\n---")

print("3. Testing estimate_grocery_budget...")
r3 = estimate_grocery_budget("Avocado Toast with poached eggs and microgreens", target_budget_per_serving=4.0)
print("Budget Breakdown:\n", r3[:250], "\n---")

print("4. Testing mixology_guide...")
r4 = mixology_guide("Gin, cucumber, elderflower tonic, lime", style="cocktail")
print("Cocktail Guide:\n", r4[:250])
