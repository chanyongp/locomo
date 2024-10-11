# Function to reduce QA entries to 1/5th while maintaining category distribution
import json
from collections import defaultdict

# Load the json file
file_path = "/home/chanyong/Analysis/Rabbit_Hole/locomo/data/locomo10_copy.json"
with open(file_path, 'r') as file:
    data = json.load(file)

def reduce_qa_by_category(data, factor=5):
    for entry in data:
        if "qa" in entry:
            # Group QA by category
            qa_by_category = defaultdict(list)
            for qa_entry in entry["qa"]:
                qa_by_category[qa_entry["category"]].append(qa_entry)
            
            # Reduce QA size for each category
            reduced_qa = []
            for category, qa_list in qa_by_category.items():
                reduced_length = max(1, len(qa_list) // factor)  # Ensure at least 1 QA per category
                reduced_qa.extend(qa_list[:reduced_length])
            
            # Replace original QA list with reduced QA list
            entry["qa"] = reduced_qa
    
    return data

# Reduce the QA size by category
reduced_data_by_category = reduce_qa_by_category(data)

# Save the reduced data to a new json file
output_reduced_category_path = "/home/chanyong/Analysis/Rabbit_Hole/locomo/data/locomo10_copy_reduced_by_category.json"
with open(output_reduced_category_path, 'w') as file:
    json.dump(reduced_data_by_category, file, indent=2)

output_reduced_category_path
