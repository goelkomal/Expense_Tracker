# Expense Tracker Program

import json
import os

# Define the file location for storing expenses
EXPENSES_FILE = "expenses.json"

def load_expenses():
    """Load expenses from a JSON file."""
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    """Save expenses to a JSON file."""
    with open(EXPENSES_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    """Add a new expense to the list."""
    try:
        category = input("Enter the expense category: ")
        amount = float(input("Enter the expense amount: "))
        description = input("Enter a description for the expense: ")

        expense = {
            "category": category,
            "amount": amount,
            "description": description
        }
        expenses.append(expense)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

def view_expenses(expenses):
    """Display all expenses."""
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nExpenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Category: {expense['category']}, Amount: ${expense['amount']:.2f}, Description: {expense['description']}")

def analyze_expenses(expenses):
    """Analyze expenses by category."""
    if not expenses:
        print("No expenses recorded.")
        return

    category_totals = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("\nExpense Analysis by Category:")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")

def main():
    """Main function to run the expense tracker."""
    print("Welcome to the Expense Tracker!")
    expenses = load_expenses()

    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            analyze_expenses(expenses)
        elif choice == '4':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

