from typing import List, Tuple, Dict
from utils import file_handler
import uuid


class PhonebookModel:
    def __init__(self):
        self.data: Dict[str, Tuple[str, str]] = {}

    def add_contact(self, contact: Tuple[str, str]) -> str:
        contact_id = str(uuid.uuid4())
        self.data[contact_id] = contact
        return contact_id

    def get_all_contacts(self) -> List[Tuple[str, str, str]]:
        return [(contact_id, name, phone) for contact_id, (name, phone) in self.data.items()]

    def remove_contact(self, contact_id: str) -> bool:
        if contact_id in self.data:
            del self.data[contact_id]
            return True
        return False

    def search_contacts(self, search_choice: int, search_term: str) -> List[Tuple[str, str, str]]:
        if search_choice == 1:
            return [(contact_id, name, phone) for contact_id, (name, phone) in self.data.items() if search_term.lower() in name.lower()]
        else:
            return [(contact_id, name, phone) for contact_id, (name, phone) in self.data.items() if search_term in phone]

    def load_data(self, file_name: str, format_type: str) -> Tuple[bool, str]:
        try:
            if format_type == 'CSV':
                contacts = file_handler.read_csv(file_name)
            elif format_type == 'JSON':
                contacts = file_handler.read_json(file_name)
            self.data = {contact_id: (name, phone) for contact_id, (name, phone) in contacts.items()}
            return True, "Data imported successfully"
        except Exception as e:
            return False, f"Error occurred while loading data: {e}"

    def save_data(self, file_name: str, format_type: str) -> Tuple[bool, str]:
        try:
            if format_type == 'CSV':
                file_handler.write_csv({contact_id: data for contact_id, data in self.data.items()}, file_name)
            elif format_type == 'JSON':
                file_handler.write_json({contact_id: data for contact_id, data in self.data.items()}, file_name)
            return True, "Data exported successfully"
        except Exception as e:
            return False, f"Error occurred while saving data: {e}"

    def find_contact(self, contact_id: str) -> bool:
        return contact_id in self.data

    def edit_contact(self, contact_id: str, new_name: str, new_phone: str):
        if contact_id in self.data:
            name, phone = self.data[contact_id]
            self.data[contact_id] = (new_name if new_name else name, new_phone if new_phone else phone)
