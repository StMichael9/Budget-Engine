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



# Budget section

final_report = {}

# Loop through totals using .items() to get both the category name and spent number.
# I use the category placeholder to look up the matching limit in our budget file.
for category, total in totals.items():
    category_budget = data_budgets[category]

    money_remaining = category_budget - totals[category]
    print(f"{category} Budget: ${category_budget} | Spent: ${total:.2f} | Remaining: ${money_remaining:.2f}")
    percentage_left = money_remaining / category_budget * 100 
    

    if money_remaining < 0:
        print("You went overboard")
    else: 
        print(f"Percentage left: {percentage_left}%")

 # Package calculations into a nested dictionary structure.
 # # This prepares the data to be saved cleanly as a JSON object.
    final_report[category] = {
        "total": total,
        "money_remaining": money_remaining,
        "percentage_left": percentage_left,
}

with open ('data/report.json', 'w') as file:
    json.dump(final_report, file, indent = 4)
