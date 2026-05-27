🧩 Budget-Engine
A lightweight, modular backend engine that analyzes spending data and generates simple, rule‑based financial recommendations. It compares actual spending against category budgets and outputs clear insights like:

“You’re over budget in Dining.”

“You have 60% of your Transportation budget remaining.”

This engine is fully standalone and can plug into any backend, CLI tool, or future API.

🚀 What It Does
Reads transactions + budgets

Calculates totals per category

Detects overspending

Generates human‑readable recommendations

Outputs clean, structured results

🧠 Why It’s Useful
Transparent logic (no ML required)

Easy to extend

Works with any JSON dataset

Perfect foundation for future API or UI layers

📦 How to Use
Replace the sample JSON files in data/ with your own:

transactions.json

budgets.json

Run:

Code
python main.py
View your personalized spending summary + recommendations.

🔧 Future Plans
REST API endpoints (FastAPI)

File upload support

Predictive budgeting (ML)

Web dashboard or mobile UI

🧱 Designed For
Anyone building:

A budgeting app

A financial dashboard

A backend service

A personal finance tool

A future ML‑powered recommendation system
