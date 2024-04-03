import os


class DirectoryModel:
    def __init__(self, directory: str) -> None:
        self.directory = directory

    def calculate_directory_size(self, path: str) -> int:
        total_size = 0
        for root, _, files in os.walk(path):
            total_size += sum(os.path.getsize(os.path.join(root, name)) for name in files)
        return total_size
