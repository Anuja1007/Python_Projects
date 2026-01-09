"""
Challenge: JSON-to-Excel Converter Tool

Create a python utility that reads structured data (like you'd get from an API) from a '.json' and converts it to a CSV file that can be opened in Excel.

Your Program should:
1. Read from a file named 'api_data,json' in the same folder.
2. Convert the JSON content (a list of dictionaries) into 'converted_date.csv'.
3. Automatically extract field names as CSV headers.
4. Handle nested structures by flatenning or skipping them.

Bonus:
- Provide feedback on how many records were converted 
- Allow user to define which fields to extract
- Handle missing fields gracefully

"""
import json
import csv
import os

INPUT_FILE = "api_data.json"
OUTPUT_FILE = "converted_data.csv"


def load_json_data(filename):
    if not os.path.exists(filename):
        print("JSON file not found")
        return []

    with open(filename, "r", encoding="utf-8") as f:
        try:
            return json.load(f)   # ✅ FIXED
        except json.JSONDecodeError:
            print("Invalid JSON format")
            return []


def convert_to_csv(data, output_file):
    if not data:
        print("No data to convert")
        return

    fieldnames = list(data[0].keys())  # ✅ FIXED name

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)  # ✅ simpler + safe

    print(f"Converted {len(data)} records to {output_file}")


def main():
    print("Converting JSON to CSV...")
    data = load_json_data(INPUT_FILE)
    convert_to_csv(data, OUTPUT_FILE)


if __name__ == "__main__":
    main()
