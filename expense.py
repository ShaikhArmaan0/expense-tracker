import csv
from datetime import datetime



def add_expense(expenses, next_id):


     while True:
       
           category = input("Enter the category: ").strip().capitalize()
   
           if category.replace(" ", "").isalpha():
               break
         
           print("Category should contain only letters.")



     while True:
           description = input("Enter the expense description: ").strip()

           if description:
            break

           print("Description cannot be empty.")
                    
          
     while True:
              
         try:
             amount = float(input("Enter the expense amount: ₹"))

             if amount <= 0:
                    print("Amount should be greater than 0")
                    continue
             break
         except ValueError:
              print("Please enter the valid number.")



     current_id = next_id
     date = datetime.now().strftime("%Y-%m-%d")

     expense = { 
             "id": current_id,
             "date": date,
             "category": category,
             "description": description,
             "amount": amount
         }

     expenses.append(expense)
     next_id += 1
     print(f"Expense added successfully (ID: {current_id})")
     return next_id




def list_expenses(expenses):
    if not expenses:
        print("No expense found")
    else:
        for expense in expenses:
            print("ID:", expense["id"])
            print("Date:", expense["date"])
            print("Category:", expense["category"])
            print("Description:", expense["description"])
            print("Amount:", expense["amount"])
            print("--------------------------")


def update_expense(expenses):
        update_id = int(input("Enter the expense ID to update: "))

        found = False

        for expense in expenses:
             if expense["id"] == update_id:
                  print("Current Category:", expense["category"])
                  print("Current Description:", expense["description"])
                  print("Current Amount:", expense["amount"])
                  print("--------------------")
                  found = True
                  while True:
                        print("Chose details to update: ")
                        
                        print("1. Category")
                        print("2. Description")
                        print("3. Amount")
                        print("4. All")
                        print("5. Main Menu")

                        choice1 = int(input("Enter your choice: "))
                        print("--------------------")

                        if choice1 == 1:
                             expense["category"] = input("Enter the Cateogry: ")
                             print(f"Expense ID {update_id} updated successfully.")
                             print("--------------------")


                        elif choice1 == 2:
                             expense["description"] = input("Enter new description: ")
                             print(f"Expense ID {update_id} updated successfully.")
                             print("--------------------")

                        elif choice1 == 3:
                             expense["amount"] = float(input("Enter the new amount: "))
                             print(f"Expense ID {update_id} updated successfully.")
                             print("--------------------")

                        elif choice1 == 4:
                             expense["category"] = input("Enter the new Cateogry: ")
                             expense["description"] = input("Enter new description: ")
                             expense["amount"] = float(input("Enter  new amount: "))
                             print(f"Expense ID {update_id} updated successfully.")
                             print("--------------------")

                             
                        elif choice1 == 5:
                             break
                        
                        else:
                             print("Invalid Choice!")
                             print("--------------------")
        if not found:
             print("Expense ID Not Found")
             print("--------------------")
             

def delete_expense(expenses):
        delete_id = int(input("Enter the Expense ID to delete: "))
        print("--------------------")

        found = False
        
        for expense in expenses:
            if expense["id"] == delete_id:
                expenses.remove(expense)
                print(f"Expense ID {delete_id} deleted successfully.")
                print("--------------------")
                found = True
                break
        if not found:
            print("Expense ID not found")
            print("--------------------")


