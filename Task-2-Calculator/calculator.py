# Simple Calculator Program
while True:
    try:
        # Step 1: Input numbers
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("⚠ Invalid input! Please enter numbers only.")
        continue 

    # Step 2: Show operation choices
    print("\nChoose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ").strip()

    # Step 3: Define functions for operations
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Division by zero is not allowed!"

    # Step 4: Perform calculation using functions
    if choice == "1":
        print(f"Result: {num1} + {num2} = {add(num1, num2)}")
    elif choice == "2":
        print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
    elif choice == "3":
        print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
    elif choice == "4":
        print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
    elif choice == "5":
        print("Exiting Calculator. Goodbye!")
        break
    else:
        print("⚠ Invalid operation choice! Please try again.")

