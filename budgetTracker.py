import json
import os

def load_budget(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        return {'income': 0, 'expenses': []}

def save_budget(budget, filename):
    with open(filename, 'w') as file:
        json.dump(budget, file)

def add_income(budget):
    amount = float(input("Enter income amount: ₹"))
    budget['income'] += amount
    print("Income added successfully.")

def add_expense(budget):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: ₹"))
    budget['expenses'].append({'category': category, 'amount': amount})
    print("Expense added successfully.")

def calculate_remaining_budget(budget):
    total_expenses = sum(item['amount'] for item in budget['expenses'])
    remaining_budget = budget['income'] - total_expenses
    return remaining_budget

def analyze_expenses(budget):
    expense_categories = {}
    for expense in budget['expenses']:
        category = expense['category']
        amount = expense['amount']
        if category in expense_categories:
            expense_categories[category] += amount
        else:
            expense_categories[category] = amount
    print("Expense Analysis:")
    for category, amount in expense_categories.items():
        print(f"{category}: ₹{amount:.2f}")

def erase_budget_data(filename):
    confirmation = input("Are you sure you want to erase all data? (yes/no): ")
    if confirmation.lower() == 'yes':
        with open(filename, 'w') as file:
            file.write('')
        print("All data erased successfully.")
        return True
    else:
        print("Operation canceled.")
        return False

def main():
    filename = "budget.json"
    budget = load_budget(filename)

    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Remaining Budget")
        print("4. Analyze Expenses")
        print("5. Erase All Data")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_income(budget)
        elif choice == '2':
            add_expense(budget)
        elif choice == '3':
            remaining_budget = calculate_remaining_budget(budget)
            print(f"Remaining Budget: ₹{remaining_budget:.2f}")
        elif choice == '4':
            analyze_expenses(budget)
        elif choice == '5':
            if erase_budget_data(filename):
                budget = {'income': 0, 'expenses': []}  # Reset budget in memory
            else:
                if not budget['income'] and not budget['expenses']:
                    print("There is no data.")
        elif choice == '6':
            save_budget(budget, filename)
            print("Exited")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
