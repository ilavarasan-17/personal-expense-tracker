expenses=[]
def add_expense(expenses):
    category = input("Enter expense category: ").strip()

    try:
        amount = int(input("Enter expense amount:"))
    except ValueError:
        print("Please enter a valid number.")
        return

    if amount < 0:
        print("Amount cannot be negative.")
        return

    expenses.append({"category": category, "amount": amount})
def view_expenses(expenses):

    if not expenses:
        print("No expenses recorded.")
        return

    for expense in expenses:
        print(f"Category: {expense['category']}, Amount: {expense['amount']}")

def calculate_total(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    total = sum(expense["amount"] for expense in expenses)
    print("Total expenses:", total)

def delete_expense(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['category']} - ₹{expense['amount']}")

    try:
        choice = int(input("Enter the expense number to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if choice < 1 or choice > len(expenses):
        print("Invalid expense number.")
        return

    deleted_expense = expenses.pop(choice - 1)
    print(f"Deleted: {deleted_expense['category']} - ₹{deleted_expense['amount']}")
    
def edit_expense(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['category']} - ₹{expense['amount']}")

    try:
        choice = int(input("Enter the expense number to edit: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if choice < 1 or choice > len(expenses):
        print("Invalid expense number.")
        return

    new_category = input("Enter new category: ").strip()

    expenses[choice - 1]["category"] = new_category

    try:
        new_amount = int(input("Enter new amount: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if new_amount < 0:
        print("Amount cannot be negative.")
        return

    expenses[choice - 1]["amount"] = new_amount
    print("Expense updated successfully.")

def search_expense(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    search_category = input("Enter category to search: ").strip()

    found = False

    for expense in expenses:
        if expense["category"] == search_category:
            print(f"Category: {expense['category']}, Amount: ₹{expense['amount']}")
            found = True

    if not found:
        print("No matching expense found.")

def category_total(expenses):
    category = input("Enter category: ").strip()
    total = 0
    found = False

    for expense in expenses:
        if expense["category"] == category:
            total += expense["amount"]
            found = True

    if not found:
        print("No expenses found for this category.")
    else:
        print(f"Total spent on {category}: ₹{total}")

def expense_summary(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    number_of_expenses = len(expenses)
    total = sum(expense["amount"] for expense in expenses)
    average = total / number_of_expenses

    print("Total expenses:", total)
    print("Number of expenses:", number_of_expenses)
    print(f"Average expense: ₹{average:.2f}")

while True:
    print("\n================================")
    print("    PERSONAL EXPENSE TRACKER")
    print("================================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Delete Expense")
    print("5. Edit Expense")
    print("6. Search Expense")
    print("7. Category Total")
    print("8. Expense Summary")
    print("9. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
         add_expense(expenses)
    elif choice == "2":
        view_expenses(expenses)
        
    elif choice == "3":
          calculate_total(expenses)
    elif choice == "4":
        delete_expense(expenses)
        
    elif choice == "5":
        edit_expense(expenses)
    elif choice == "6":
        search_expense(expenses)
    elif choice == "7":
        category_total(expenses)
    elif choice == "8":
        expense_summary(expenses)
    elif choice == "9":
        break
        
        
    else:
        print("Invalid choice. Please try again.")
