from typing import List, Tuple
from utils import file_handler


class PhonebookModel:
    def __init__(self):
        self.data = {}

    def add_contact(self, contact: Tuple[str, str]):
        name, phone = contact
        self.data[name] = phone

    def get_all_contacts(self) -> List[Tuple[str, str]]:
        return [(name, phone) for name, phone in self.data.items()]

    def remove_contact(self, name: str) -> bool:
        if name in self.data:
            del self.data[name]
            return True
        return False

    def search_contacts(self, search_choice: int, search_term: str) -> List[Tuple[str, str]]:
        if search_choice == 1:
            return [(name, self.data[name]) for name in self.data if search_term.lower() in name.lower()]
        else:
            return [(name, phone) for name, phone in self.data.items() if search_term in phone]

    def load_data(self, file_name: str, format_type: str) -> Tuple[bool, str]:
        try:
            if format_type == 'CSV':
                contacts = file_handler.read_csv(file_name)
            elif format_type == 'JSON':
                contacts = file_handler.read_json(file_name)
            if isinstance(contacts, list):
                self.data = {name: phone for name, phone in contacts}
            else:
                self.data = contacts
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

    def find_contact(self, name: str) -> bool:
        return name in self.data

    def edit_contact(self, name: str, new_name: str, new_phone: str):
        if not new_name:
            new_name = name
        if not new_phone:
            new_phone = self.data[name]

        if new_name != name:
            del self.data[name]

        self.data[new_name] = new_phone
