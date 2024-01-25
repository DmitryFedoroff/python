import csv
import json


def read_csv(file_name):
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        return {row[0]: (row[1], row[2]) for row in reader}  # ID, Name, Phone


def write_csv(data, file_name):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for contact_id, (name, phone) in data.items():
            writer.writerow([contact_id, name, phone])


def read_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_json(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
