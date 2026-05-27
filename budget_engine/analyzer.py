import json

"""
This file handles:

reading transactions
grouping by category
calculating totals
comparing to budgets

This is the “math brain.”
"""

def run_analysis():
    # Open the file and parse JSON content
    with open('data/transactions.json', 'r') as file:
        data = json.load(file)

    with open('data/budgets.json', 'r') as file:
        data_budgets = json.load(file)

    # this needs to track totals per category
    totals = {}

    for item in data:
        amount = item["amount"]
        merchant = item["merchant"]
        category = item["category"]

        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount

    # Budget section
    final_report = {}

    for category, total in totals.items():
        category_budget = data_budgets[category]
        money_remaining = category_budget - totals[category]
        percentage_left = money_remaining / category_budget * 100

        # Package calculations into a nested dictionary structure.
        final_report[category] = {
            "total": total,
            "money_remaining": money_remaining,
            "percentage_left": percentage_left,
        }

    # Save report
    with open('data/report.json', 'w') as file:
        json.dump(final_report, file, indent=4)

    return final_report
