import random
import uuid


def random_data_generation():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Password")
        print("3. Generate Unique Identifier (UUID)")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            num = random.randint(1, 100)
            print(f"Random Number: {num}")
        elif choice == "2":
            password = "".join(
                random.choices("abcdefghijklmnopqrstuvwxyz0123456789!@#", k=8)
            )
            print(f"Generated Password: {password}")
        elif choice == "3":
            uid = uuid.uuid4()
            print(f"Generated UUID: {uid}")
        elif choice == "4":
            break
