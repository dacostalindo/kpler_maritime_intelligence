import os
import csv
import json
import requests

# from app import db

# if not os.path.isfile("vessel.db"):
#     db.create_all()


PATH_TO_CSV = 'vessel_data.csv'
BASE = "http://127.0.0.1:5000/"


    
def __post_to_db(csv_dict):
    counter = 0
    for entry in csv_dict:
        #remove leading space in dictionary key
        json_entry = { x.translate({32:None}) : y 
                 for x, y in entry.items()}
        response = requests.post( BASE + "insert", params=json_entry)
        print(response.json())
        

def main():
    with open(PATH_TO_CSV, mode='r') as csv_file:
        csv_dict = csv.DictReader(csv_file)
        __post_to_db(csv_dict)

if __name__ == "__main__":
    main()