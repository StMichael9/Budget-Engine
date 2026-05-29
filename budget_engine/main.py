from data_loader import load_json, load_csv, validate_data

def main():
    # Load JSON
    json_data = load_json("sample_data/user1.json")
    print("JSON Loaded:", json_data)

    # Validate JSON
    print("JSON Valid:", validate_data(json_data))

    # Load CSV
    csv_data = load_csv("sample_data/test.csv")
    print("CSV Loaded:", csv_data)

    # Validate CSV
    print("CSV Valid:", validate_data(csv_data))

if __name__ == "__main__":
    main()
