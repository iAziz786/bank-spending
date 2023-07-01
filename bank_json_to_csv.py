# I used this file to first convert the XML which I got from my bank to JSON
# then I used ChatGPT to create the csv from the JSON
# Depending upon your back, your CSV will be different. The titles are this:
# Date,Ref No,Description,Debit,Credit,Remaining
import json
import csv


def json_to_csv(json_file_path, csv_file_path):
    # Load JSON file
    with open(json_file_path, "r") as jf:
        data = json.load(jf)

    # Prepare data for CSV
    csv_data = []
    for record in data:
        cell = record["Cell"]
        csv_record = {
            "Date": cell[0]["Data"]["__text"] if "__text" in cell[0]["Data"] else "",
            "Ref No": cell[2]["Data"]["__text"] if "__text" in cell[2]["Data"] else "",
            "Description": cell[3]["Data"]["__text"]
            if "__text" in cell[3]["Data"]
            else "",
            "Debit": cell[4]["Data"]["__text"] if "__text" in cell[4]["Data"] else "",
            "Credit": cell[5]["Data"]["__text"] if "__text" in cell[5]["Data"] else "",
            "Remaining": cell[6]["Data"]["__text"]
            if "__text" in cell[6]["Data"]
            else "",
        }
        csv_data.append(csv_record)

    # Write to CSV file
    with open(csv_file_path, "w", newline="") as cf:
        writer = csv.DictWriter(
            cf,
            fieldnames=[
                "Date",
                "Ref No",
                "Description",
                "Debit",
                "Credit",
                "Remaining",
            ],
        )
        writer.writeheader()
        writer.writerows(csv_data)


# Call the function with your file paths
if __name__ == "__main__":
    json_to_csv("spend.json", "spend.csv")
