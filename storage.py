import json


def save_data(expenses):
     with open("expenses.json", "w") as file:
          json.dump(expenses, file)

def load_data():
     

     try:

        with open("expenses.json", "r") as file:
            expenses = json.load(file)
     except (FileNotFoundError,json.JSONDecodeError):
          expenses = []
     return expenses
