import csv
import json
from typing import Dict, Tuple


def read_csv(file_name: str) -> Dict[str, Tuple[str, str]]:
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        return {row[0]: (row[1], row[2]) for row in reader}


def write_csv(data: Dict[str, Tuple[str, str]], file_name: str) -> None:
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for contact_id, (name, phone) in data.items():
            writer.writerow([contact_id, name, phone])


def read_json(file_name: str) -> Dict[str, Tuple[str, str]]:
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_json(data: Dict[str, Tuple[str, str]], file_name: str) -> None:
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
