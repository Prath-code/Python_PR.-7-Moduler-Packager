from modules.datetime_ops import datetime_operations
from modules.math_ops import mathematical_operations
from modules.random_ops import random_data_generation


def main():
    while True:
        print("\nWelcome to Multi-Utility Toolkit")
        print("1. DateTime Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_operations()
        elif choice == "2":
            mathematical_operations()
        elif choice == "3":
            random_data_generation()
        elif choice == "4":
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
