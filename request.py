import requests
from collections import defaultdict

class PetStoreAPI:
    def __init__(self):
        self.base_url = "https://petstore.swagger.io/v2"
        self.user = None
        self.pets = []

    def create_user(self, username, email):
        user_data = {
            "id": 0,
            "username": username,
            "email": email,
        }
        response = requests.post(f"{self.base_url}/user", json=user_data)
        if response.status_code == 200:
            self.user = user_data
            print("User created successfully.")
        else:
            print(f"Failed to create user. Status code: {response.status_code}")

    def get_user_data(self):
        if self.user:
            print("User Data:")
            print(f"ID: {self.user['id']}")
            print(f"Username: {self.user['username']}")
            print(f"Email: {self.user['email']}")
        else:
            print("User not found.")

    def find_sold_pets(self):
        response = requests.get(f"{self.base_url}/pet/findByStatus?status=sold")
        if response.status_code == 200:
            self.pets = response.json()
            sold_pets = defaultdict(int)
            for pet in self.pets:
                sold_pets[pet['name']] += 1
            return sold_pets
        else:
            print(f"Failed to fetch sold pets. Status code: {response.status_code}")
            return {}

if __name__ == "__main__":
    api = PetStoreAPI()

    # Task 1: Create a user and retrieve their data
    api.create_user("JohnDoe", "johndoe@example.com")
    api.get_user_data()

    # Task 2: Collect and list the names of sold pets
    sold_pets = api.find_sold_pets()
    print("\nNames of sold pets:")
    for name, count in sold_pets.items():
        print(f"{name}: {count}")

    # Task 3: Create a class to identify the count of pets with the same name
    class PetNameCounter:
        def __init__(self, pets):
            self.pets = pets

        def count_pets_by_name(self):
            pet_count = defaultdict(int)
            for pet in self.pets:
                pet_count[pet['name']] += 1
            return pet_count

    pet_counter = PetNameCounter(api.pets)
    pet_name_counts = pet_counter.count_pets_by_name()
    print("\nCounts of pets with the same name:")
    for name, count in pet_name_counts.items():
        print(f"{name}: {count}")

