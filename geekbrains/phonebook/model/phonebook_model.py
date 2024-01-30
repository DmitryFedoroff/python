from typing import List, Tuple, Dict
from utils import file_handler
from utils.logger_config import get_logger
import uuid


class PhonebookModel:
    def __init__(self):
        self.logger = get_logger(__name__)
        self.data: Dict[str, Tuple[str, str]] = {}

    def add_contact(self, contact: Tuple[str, str]) -> str:
        try:
            contact_id = str(uuid.uuid4())
            self.data[contact_id] = contact
            self.logger.info(f"Contact added with ID: {contact_id}")
            return contact_id
        except Exception as e:
            self.logger.error(f"Error adding contact: {e}")
            raise

    def get_all_contacts(self) -> List[Tuple[str, str, str]]:
        try:
            return [(contact_id, name, phone) for contact_id, (name, phone) in self.data.items()]
        except Exception as e:
            self.logger.error(f"Error retrieving all contacts: {e}")
            raise

    def remove_contact(self, contact_id: str) -> bool:
        try:
            if contact_id in self.data:
                del self.data[contact_id]
                self.logger.info(f"Contact removed with ID: {contact_id}")
                return True
            self.logger.warning(f"Attempted to remove non-existent contact with ID: {contact_id}")
            return False
        except Exception as e:
            self.logger.error(f"Error removing contact with ID: {contact_id}: {e}")
            raise

    def search_contacts(self, search_choice: int, search_term: str) -> List[Tuple[str, str, str]]:
        try:
            if search_choice == 1:
                results = [(contact_id, name, phone) for contact_id, (name, phone) in self.data.items() if
                           search_term.lower() in name.lower()]
            else:
                results = [(contact_id, name, phone) for contact_id, (name, phone) in self.data.items() if
                           search_term in phone]
            if results:
                self.logger.info(f"Search completed with results for term '{search_term}'")
            else:
                self.logger.info(f"Search completed with no results for term '{search_term}'")
            return results
        except Exception as e:
            self.logger.error(f"Error searching contacts with term '{search_term}': {e}")
            raise

    def load_data(self, file_name: str, format_type: str) -> Tuple[bool, str]:
        try:
            if format_type == 'CSV':
                contacts = file_handler.read_csv(file_name)
            elif format_type == 'JSON':
                contacts = file_handler.read_json(file_name)
            self.data = {contact_id: (name, phone) for contact_id, (name, phone) in contacts.items()}
            self.logger.info(f"Data loaded successfully from {file_name}")
            return True, "Data imported successfully"
        except Exception as e:
            self.logger.error(f"Error loading data from {file_name}: {e}")
            return False, f"Error occurred while loading data: {e}"

    def save_data(self, file_name: str, format_type: str) -> Tuple[bool, str]:
        try:
            if format_type == 'CSV':
                file_handler.write_csv({contact_id: data for contact_id, data in self.data.items()}, file_name)
            elif format_type == 'JSON':
                file_handler.write_json({contact_id: data for contact_id, data in self.data.items()}, file_name)
            self.logger.info(f"Data saved successfully to {file_name}")
            return True, "Data exported successfully"
        except Exception as e:
            self.logger.error(f"Error saving data to {file_name}: {e}")
            return False, f"Error occurred while saving data: {e}"

    def find_contact(self, contact_id: str) -> bool:
        try:
            if contact_id in self.data:
                self.logger.info(f"Contact found with ID: {contact_id}")
                return True
            self.logger.info(f"No contact found with ID: {contact_id}")
            return False
        except Exception as e:
            self.logger.error(f"Error finding contact with ID: {contact_id}: {e}")
            raise

    def edit_contact(self, contact_id: str, new_name: str, new_phone: str):
        try:
            if contact_id in self.data:
                name, phone = self.data[contact_id]
                self.data[contact_id] = (new_name if new_name else name, new_phone if new_phone else phone)
                self.logger.info(f"Contact with ID: {contact_id} has been edited")
        except Exception as e:
            self.logger.error(f"Error editing contact with ID: {contact_id}: {e}")
            raise

    def is_phone_number_unique(self, phone_number: str) -> bool:
        try:
            unique = not any(phone == phone_number for _, (_, phone) in self.data.items())
            if not unique:
                self.logger.info(f"Phone number {phone_number} is not unique")
            return unique
        except Exception as e:
            self.logger.error(f"Error checking uniqueness of phone number {phone_number}: {e}")
            raise
