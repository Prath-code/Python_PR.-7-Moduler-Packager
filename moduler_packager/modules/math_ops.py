import math

def mathematical_operations():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Calculate Compound Interest")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            num = int(input("Enter a number: "))
            print(f"Factorial: {math.factorial(num)}")
        elif choice == "2":
            p = float(input("Enter principal amount: "))
            r = float(input("Enter rate of interest (in %): "))
            t = float(input("Enter time (in years): "))
            ci = p * (pow((1 + r / 100), t))
            print(f"Compound Interest: {ci:.2f}")
        elif choice == "3":
            break