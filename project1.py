FILE_NAME = "expenses.txt"

def add_expense():
    try:
        category = input("Enter category (Food/Travel/etc.): ")
        amount = float(input("Enter amount: "))
        with open(FILE_NAME, "a") as file:
            file.write(f"{category},{amount}\n")
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount! Please enter a number.")

def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()
            if not data:
                print("No expenses recorded yet.")
                return
            print("\n--- All Expenses ---")
            for line in data:
                category, amount = line.strip().split(",")
                print(f"Category: {category} | Amount: ₹{amount}")
    except FileNotFoundError:
        print("No expense file found. Add expenses first.")

def calculate_total():
    try:
        total = 0
        with open(FILE_NAME, "r") as file:
            for line in file:
                _, amount = line.strip().split(",")
                total += float(amount)
        print(f"\nTotal Expense: ₹{total}")
    except FileNotFoundError:
        print("No expense file found.")

def category_count():
    try:
        counts = {}
        with open(FILE_NAME, "r") as file:
            for line in file:
                category, _ = line.strip().split(",")
                counts[category] = counts.get(category, 0) + 1
        print("\nCategory-wise Count:")
        for cat, count in counts.items():
            print(f"{cat}: {count}")
    except FileNotFoundError:
        print("No expense file found.")

def menu():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category Count")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            category_count()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

menu()