from typing import Dict, Any


class DirectoryView:
    @staticmethod
    def display_data(data: Dict[str, Any]) -> None:
        for path, info in data.items():
            print(f'{path}: {info["type"]} - {info["name"]} - {info["size"]} bytes')

    @staticmethod
    def display_message(message: str) -> None:
        print(message)
