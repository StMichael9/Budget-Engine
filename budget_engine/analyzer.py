import json

"""This file handles:

reading transactions

grouping by category

calculating totals

comparing to budgets

This is the “math brain.”"""

# Open the file and parse JSON content
with open ('data/transactions.json', 'r') as file:
    data = json.load(file)

    # Open the file and parse JSON content
with open ('data/budgets.json', 'r') as file:
    data_budgets = json.load(file)


# this needs to track of totals per catagory
totals = {}

for item in data:
    amount = item["amount"]
    merchant = item["merchant"]
    category = item["category"]
    print(f"Spent {amount} on {merchant}")

    if category in totals:
        totals[category] += amount
    else:
        totals[category] = amount

for category, total in totals.items():
    print(f"{category}: ${total:.2f}")





#for d in data:
 #   print(d) 