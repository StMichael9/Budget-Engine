"""Handles:
- reading JSON
- reading CSV
- validating required fields
- returning clean Python dicts
"""

import json
import csv

def load_json(path):
    with open(path, 'r') as file:
        data = json.load(file)
        return data

def load_csv(path):
    with open(path, 'r') as file:
        data = list(csv.DictReader(file))
        return data
    

def validate_data(data):
    
    # Check if either required key is completely missing from this row
    if isinstance(data, list):
        for row in data:
            if 'category' not in row or 'amount' not in row:
                return False
        return True

    elif isinstance(data, dict):
        if 'income' not in data or 'expenses' not in data:
            return False
        return True



                
            
                    
        
            


    
