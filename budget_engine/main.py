""" main.py
This file is the boss of the whole project.
It tells the analyzer to do the math.
It tells the recommender to give advice.
Then it shows the results to the user.
You only run THIS file. Everything else works behind the scenes.
"""

import analyzer
import recommender

# This guard clause ensures the dashboard only runs if main.py is executed directly.
# It prevents the script from accidentally triggering if it's imported elsewhere.
if __name__ == "__main__":
    # 1. Run the analysis and catch the returned dictionary
    report = analyzer.run_analysis()

    # 2. Pass that fresh report into the recommender and catch the advice
    advices = recommender.generate_recommendations(report)

    print("\n=== FINANCIAL SUMMARY REPORT ===")

    # Everything below must be indented 4 spaces to stay inside the if block
    for category, items in report.items():
        total = items['total']
        money_remaining = items['money_remaining']  # Fixed: Restored underscore to prevent KeyError
        advice_list = advices[category]
        
        # Simple text header and dash dividers
        print(f"\n--- {category.upper()} ---")
        print(f"Spent:     ${total:.2f}")
        print(f"Remaining: ${money_remaining:.2f}")
        print("Advice:")
        
        # Indented plain bullet points for a clean look
        for tip in advice_list:
            print(f"  - {tip}")
    # Print a clean closing border at the very end
    print("\n===============================\n")

