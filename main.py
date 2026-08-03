from storage import save_data, load_data
from expense import (add_expense, update_expense, list_expenses, delete_expense)
from reports import (summary, monthly_summary, export_csv)

expenses = load_data()
          
if expenses:
    next_id = max(expense["id"] for expense in expenses) + 1
else:
    next_id = 1


while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense.")
    print("2. List Expenses.")
    print("3. Update Expense.")
    print("4. Delete Expense.")
    print("5. Summary.")
    print("6. Monthly Summary.")
    print("7. Export in CSV")
    print("8. Exit")


    try:

        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if choice == 1:
        print("--------------------")
        next_id = add_expense(expenses, next_id)
        save_data(expenses)

    elif choice == 2:
        print("--------------------")
        list_expenses(expenses)

    elif choice == 3:
         print("--------------------")
         update_expense(expenses)
         save_data(expenses)

    elif choice == 4:
         print("--------------------")
         delete_expense(expenses)
         save_data(expenses)

    elif choice == 5:
         print("--------------------")
         summary(expenses)

    elif choice == 6:
         monthly_summary(expenses)

    elif choice == 7:
         export_csv(expenses)

    elif choice == 8:
         
         print("Thank you for using Expense Tracker!")
         print("--------------------")
         break

    else:
        print("Invalid Choice!")

