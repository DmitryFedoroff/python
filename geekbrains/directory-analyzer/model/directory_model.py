import os
from typing import Dict, Any


class DirectoryModel:
    def __init__(self, directory: str) -> None:
        self.directory = directory

    def calculate_directory_size(self, path: str) -> int:
        total_size = 0
        for root, _, files in os.walk(path):
            total_size += sum(os.path.getsize(os.path.join(root, name)) for name in files)
        return total_size

    def analyze_directory(self, path: str = None, parent_directory: str = "") -> Dict[str, Any]:
        if path is None:
            path = self.directory
        data = {}
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                data[item_path] = {
                    "type": "File",
                    "name": item,
                    "size": os.path.getsize(item_path),
                    "parent_directory": parent_directory,
                }
            elif os.path.isdir(item_path):
                data[item_path] = {
                    "type": "Directory",
                    "name": item,
                    "size": self.calculate_directory_size(item_path),
                    "parent_directory": parent_directory,
                }
                data.update(self.analyze_directory(item_path, parent_directory=item))
        return data
