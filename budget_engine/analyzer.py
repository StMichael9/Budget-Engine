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

for item in data:
    amount = item["amount"]
    merchant = item["merchant"]
    print(f"Spent {amount} on {merchant}")


#for d in data:
 #   print(d) 