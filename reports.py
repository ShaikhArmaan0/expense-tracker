import csv
from datetime import datetime




def summary(expenses):
     if not expenses:
          print("No Expenses Found")
          return
     
     total = 0
     for expense in expenses:
          total += expense["amount"]
     print(f"Total Expense: {total}")
     print("--------------------")


def monthly_summary(expenses):
     month = int(input("Enter month (1-12): "))
     print("--------------------")
     

     if month < 1 or month > 12:
        print("Invalid month!")
        return

     total = 0

     for expense in expenses:  
        expense_month = int(expense["date"][5:7])

        if expense_month == month:
             total += expense["amount"]
     print(f"Total Expenses for Month {month}: {total}")
     print("--------------------")


def export_csv(expenses):
     with open("expenses.csv", "w") as file:
          writer = csv.writer(file)

        #   header
          writer.writerow(["ID", "Date", "Category" ,"Description", "Amount"])

        #   data
          for expense in expenses:
               writer.writerow([
                    expense["id"],
                    expense["date"],
                    expense["category"],
                    expense["description"],
                    expense["amount"]
               ])
     print("--------------------")          
     print("Expenses Exported Successfully!")
     print("--------------------")

