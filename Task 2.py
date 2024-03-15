#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import os

# Function to load data from file
def load_data(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename, 'r') as file:
        return json.load(file)

# Function to save data to file
def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Function to add transaction
def add_transaction(data, transaction_type, category, amount):
    if transaction_type not in data:
        data[transaction_type] = []
    data[transaction_type].append({"category": category, "amount": amount})
    return data

# Function to calculate remaining budget
def calculate_budget(data):
    total_income = sum(transaction['amount'] for transaction in data.get('income', []))
    total_expense = sum(transaction['amount'] for transaction in data.get('expense', []))
    return total_income - total_expense

# Function to analyze expenses by category
def analyze_expenses(data):
    expense_analysis = {}
    for expense in data.get('expense', []):
        category = expense['category']
        amount = expense['amount']
        expense_analysis[category] = expense_analysis.get(category, 0) + amount
    return expense_analysis

# Main function
def main():
    filename = "budget_tracker_data.json"
    data = load_data(filename)

    while True:
        print("\nBudget Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Remaining Budget")
        print("4. Analyze Expenses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter income category: ")
            amount = float(input("Enter amount: "))
            data = add_transaction(data, 'income', category, amount)
            save_data(data, filename)
        elif choice == '2':
            category = input("Enter expense category: ")
            amount = float(input("Enter amount: "))
            data = add_transaction(data, 'expense', category, amount)
            save_data(data, filename)
        elif choice == '3':
            remaining_budget = calculate_budget(data)
            print(f"Remaining Budget: {remaining_budget}")
        elif choice == '4':
            expense_analysis = analyze_expenses(data)
            print("Expense Analysis:")
            for category, amount in expense_analysis.items():
                print(f"{category}: {amount}")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

