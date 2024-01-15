from typing import List, Tuple
from utils import file_handler


class PhonebookModel:
    def __init__(self):
        self.data = []

    def add_contact(self, contact: Tuple[str, str]):
        self.data.append(contact)

    def get_all_contacts(self) -> List[Tuple[str, str]]:
        return self.data

    def search_contacts(self, search_choice: int, search_term: str) -> List[Tuple[str, str]]:
        search_function = (
            (lambda contact: search_term.lower() in contact[0].lower())
            if search_choice == 1
            else (lambda contact: search_term in contact[1])
        )

        return [contact for contact in self.data if search_function(contact)]

    def load_data(self, file_name: str, format_type: str) -> Tuple[bool, str]:
        try:
            if format_type == 'CSV':
                self.data = file_handler.read_csv(file_name)
            elif format_type == 'JSON':
                self.data = file_handler.read_json(file_name)
            return True, "Data imported successfully"
        except Exception as e:
            return False, f"Error occurred while loading data: {e}"

    def save_data(self, file_name: str, format_type: str) -> Tuple[bool, str]:
        try:
            if format_type == 'CSV':
                file_handler.write_csv(self.data, file_name)
            elif format_type == 'JSON':
                file_handler.write_json(self.data, file_name)
            return True, "Data exported successfully"
        except Exception as e:
            return False, f"Error occurred while saving data: {e}"
