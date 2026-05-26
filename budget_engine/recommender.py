import json
"""This file handles:

turning numbers into advice

generating recommendations

formatting messages

This is the “advice brain.”"""

with open('data/report.json', 'r') as file:
    data = json.load(file)

recommendations = {}

for category, item in data.items():
     # Now 'category' is the string "Dining"
    # Now 'item' is the dictionary: {"total": 22.2, "money_remaining": 127.8, ...}

    total = item['total']
    money_remaining = item['money_remaining']
    percentage_left = item['percentage_left']

    if percentage_left < 0:
        recommendations[category] = ["You have gone over budget", "Try tracking daily expenses."]
    elif percentage_left < 50:
        recommendations[category] = ["You have used over half your budget.", "Consider cutting down on non-essential spending."]
    else:
        recommendations[category] = ["You are pacing beautifully!", "Great job keeping your spending under control."]

print(recommendations)


  
    

    

