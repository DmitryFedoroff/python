from model.directory_model import DirectoryModel
from view.directory_view import DirectoryView
import json
import csv
import pickle
import os
from typing import Dict, Any


class DirectoryController:
    def __init__(self, directory: str) -> None:
        self.model = DirectoryModel(directory)
        self.view = DirectoryView()

    def analyze_and_save(self, output_dir: str) -> None:
        data = self.model.analyze_directory()
        self._write_to_json(data, output_dir, 'directory_analysis')
        self._write_to_csv(data, output_dir, 'directory_analysis')
        self._write_to_pickle(data, output_dir, 'directory_analysis')
        self.view.display_message("Analysis completed and data saved.")

    def _write_to_json(self, data: Dict[str, Any], directory: str, filename: str) -> None:
        filepath = os.path.join(directory, f'{filename}.json')
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    def _write_to_csv(self, data: Dict[str, Any], directory: str, filename: str) -> None:
        filepath = os.path.join(directory, f'{filename}.csv')
        with open(filepath, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Path', 'Type', 'Name', 'Size', 'Parent Directory'])
            for key, value in data.items():
                writer.writerow([key, value['type'], value['name'], value['size'], value['parent_directory']])

    def _write_to_pickle(self, data: Dict[str, Any], directory: str, filename: str) -> None:
        filepath = os.path.join(directory, f'{filename}.pickle')
        with open(filepath, 'wb') as file:
            pickle.dump(data, file)
