import json
import pandas as pd

# File paths
input_file_path = 'extracted_data1.txt'
output_file_path = 'output_data.xlsx'

# Read JSON objects from file
json_objects = []
try:
    with open(input_file_path, 'r', encoding='utf-8') as file:
        for index, line in enumerate(file):
            try:
                json_object = json.loads(line)
                json_objects.append(json_object)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from line {index + 1}: {line.strip()}\nError: {e}")

except FileNotFoundError:
    print(f"File not found: {input_file_path}")
except UnicodeDecodeError as e:
    print(f"Unicode decoding error: {e}. Try a different file encoding.")
except Exception as e:
    print(f"An error occurred: {e}")

# Process JSON objects and convert to DataFrame
data = []
for obj in json_objects:
    part_number = obj.get("Part-Number", "")
    spring_rate = obj.get("Spring-Rates", "")
    fitment = json.dumps(obj.get("Fitment", {}))  # Convert object/array to string
    fitment_warning = json.dumps(obj.get("Fitment-Warning", {}))  # Convert object/array to string
    print([part_number, spring_rate, fitment, fitment_warning])
    data.append([part_number, spring_rate, fitment, fitment_warning])

# Create DataFrame
df = pd.DataFrame(data, columns=["part-number", "spring-rate", "Fitment", "Fitment-warning"])

# Save DataFrame to Excel
df.to_excel(output_file_path, index=False)

print(f"Data successfully exported to {output_file_path}.")
print(f"Number of objects imported: {len(json_objects)}")
