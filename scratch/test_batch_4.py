from app.tools import (
    universal_culinary_encyclopedia,
    clinical_dietary_matrix,
    molecular_gastronomy_engine,
    banquet_kitchen_operations,
    execute_custom_culinary_skill
)

print("1. Testing universal_culinary_encyclopedia...")
e1 = universal_culinary_encyclopedia("History and spice breakdown of Ethiopian Doro Wat", domain="regional-cuisines")
print("Encyclopedia Output:\n", e1[:250], "\n---")

print("2. Testing clinical_dietary_matrix...")
e2 = clinical_dietary_matrix("Low-FODMAP", "Garlic Butter Shrimp with Pasta and Mushrooms")
print("Clinical Matrix Output:\n", e2[:250], "\n---")

print("3. Testing molecular_gastronomy_engine...")
e3 = molecular_gastronomy_engine("Spherification", "Mango juice caviar using sodium alginate")
print("Molecular Gastronomy Output:\n", e3[:250], "\n---")

print("4. Testing banquet_kitchen_operations...")
e4 = banquet_kitchen_operations("Plated Wedding Dinner", 150, "Braised Short Ribs, Truffle Mash, Roasted Asparagus")
print("Banquet Operations Output:\n", e4[:250], "\n---")

print("5. Testing execute_custom_culinary_skill...")
e5 = execute_custom_culinary_skill("sourdough-baking", "Target 78% hydration sourdough bread baking schedule and autolyse times")
print("Custom Skill Output:\n", e5[:250])
