import logging
import google.auth
from google.auth.transport.requests import AuthorizedSession

# CRITICAL: Hardcode the project ID string so it works on Agent Platform runtime.
# Do NOT use os.getenv("GOOGLE_CLOUD_PROJECT") or google.auth.default() here.
FIRESTORE_PROJECT_ID = "qwiklabs-gcp-02-8b55424b019a"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def set_doc(session: AuthorizedSession, collection: str, doc_id: str, data_fields: dict):
    url = f"https://firestore.googleapis.com/v1/projects/{FIRESTORE_PROJECT_ID}/databases/(default)/documents/{collection}/{doc_id}"
    
    # Convert simple python dict to Firestore REST format
    firestore_fields = {}
    for k, v in data_fields.items():
        if isinstance(v, str):
            firestore_fields[k] = {"stringValue": v}
        elif isinstance(v, int):
            firestore_fields[k] = {"integerValue": str(v)}
        elif isinstance(v, float):
            firestore_fields[k] = {"doubleValue": v}
        elif isinstance(v, list):
            firestore_fields[k] = {"arrayValue": {"values": [{"stringValue": str(item)} for item in v]}}

    resp = session.patch(url, json={"fields": firestore_fields})
    if resp.status_code in [200, 201]:
        logger.info(f"Seeded {collection}/{doc_id} successfully.")
    else:
        logger.error(f"Error seeding {collection}/{doc_id}: {resp.status_code} - {resp.text}")


def seed_database():
    logger.info(f"Initializing Firestore seeding for project: {FIRESTORE_PROJECT_ID}")
    creds, _ = google.auth.default()
    session = AuthorizedSession(creds)

    # Seed recipes
    recipes = [
        {
            "id": "avocado-toast",
            "name": "Smashed Avocado Toast",
            "cuisine": "American",
            "prep_time_minutes": 10,
            "dietary_tags": ["vegan", "vegetarian"],
            "ingredients": ["2 slices sourdough bread", "1 ripe avocado", "1 tbsp lemon juice", "red pepper flakes", "sea salt"],
            "instructions": "Toast sourdough slices. Mash avocado with lemon juice, salt, and red pepper. Spread evenly on toast."
        },
        {
            "id": "tuscan-pasta",
            "name": "Creamy Tuscan Garlic Pasta",
            "cuisine": "Italian",
            "prep_time_minutes": 25,
            "dietary_tags": ["vegetarian"],
            "ingredients": ["8oz fettuccine", "1 cup heavy cream", "1/2 cup sun-dried tomatoes", "2 cups spinach", "3 cloves garlic minced"],
            "instructions": "Boil pasta. Sauté garlic and sun-dried tomatoes in olive oil. Add heavy cream and spinach. Toss with pasta."
        },
        {
            "id": "chickpea-curry",
            "name": "Coconut Chickpea Curry",
            "cuisine": "Indian",
            "prep_time_minutes": 20,
            "dietary_tags": ["vegan", "gluten-free"],
            "ingredients": ["1 can chickpeas drained", "1 can coconut milk", "1 tbsp curry powder", "1 diced onion", "2 cloves garlic"],
            "instructions": "Sauté onions and garlic. Add curry powder, coconut milk, and chickpeas. Simmer for 15 minutes."
        }
    ]

    for recipe in recipes:
        set_doc(session, "recipes", recipe["id"], recipe)

    # Seed pantry items
    pantry_items = [
        {
            "id": "avocado",
            "item_name": "Avocado",
            "quantity": 3,
            "unit": "items",
            "category": "Produce"
        },
        {
            "id": "chickpeas",
            "item_name": "Canned Chickpeas",
            "quantity": 2,
            "unit": "cans",
            "category": "Canned Goods"
        },
        {
            "id": "coconut-milk",
            "item_name": "Coconut Milk",
            "quantity": 3,
            "unit": "cans",
            "category": "Canned Goods"
        },
        {
            "id": "garlic",
            "item_name": "Garlic",
            "quantity": 1,
            "unit": "head",
            "category": "Produce"
        }
    ]

    for item in pantry_items:
        set_doc(session, "pantry", item["id"], item)

    print("Database seeding completed successfully!")


if __name__ == "__main__":
    seed_database()
