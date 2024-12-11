from mongita import MongitaClientDisk # type: ignore

client = MongitaClientDisk()
db = client.accommodation_db

def create_database():
    db.drop_collection("accommodation_collection")
    accommodation_collection = db.accommodation_collection
    accommodation_collection.insert_many([
        {"name": "Sea View Villa", "location": "Miami", "price": 250.0, "amenities": ["Pool", "Wi-Fi"]},
        {"name": "Mountain Cabin", "location": "Denver", "price": 150.0, "amenities": ["Fireplace", "Hiking"]}
    ])

    db.drop_collection("review_collection")
    review_collection = db.review_collection

    print("Database created successfully.")

if __name__ == "__main__":
    create_database()
