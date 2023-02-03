import csv
import json

def lambda_handler(event, context):
  
    # Read the contents of the csv file
    with open("input.csv", "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Write the contents of the csv file to a json file
    with open("output.json", "w") as f:
        json.dump(rows, f)

    return {
        'statusCode': 200,
        'body': 'CSV to JSON conversion complete'
    }
