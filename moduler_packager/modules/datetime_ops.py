import datetime

def datetime_operations():
    while True:
        print("\nDateTime Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            now = datetime.datetime.now()
            print(f"Current Date and Time: {now}")
        elif choice == "2":
            date1 = input("Enter the first date (YYYY-MM-DD): ")
            date2 = input("Enter the second date (YYYY-MM-DD): ")
            d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
            d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
            difference = abs((d2 - d1).days)
            print(f"Difference: {difference} days")
        elif choice == "3":
            break