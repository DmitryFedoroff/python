from model.phonebook_model import PhonebookModel
from view.phonebook_view import PhonebookView
from utils.data_validator import validate_phone_number, validate_name, get_menu_choice
from typing import Callable, Dict


class PhonebookController:
    def __init__(self) -> None:
        self.model: PhonebookModel = PhonebookModel()
        self.view: PhonebookView = PhonebookView()
        self.actions: Dict[int, Callable[[], None]] = {
            1: self.add_contact,
            2: self.display_contacts,
            3: self.remove_contact,
            4: self.search_contacts,
            5: self.edit_contact,
            6: lambda: self.handle_file_operations(6),
            7: lambda: self.handle_file_operations(7)
        }

    def start(self) -> None:
        while True:
            self.view.display_menu()
            choice: int = self.view.get_user_choice([str(i) for i in range(1, 9)], "Enter your choice (1-8): ")
            if choice == '8':
                break
            action: Callable[[], None] = self.actions.get(int(choice), self.invalid_choice)
            action()

    def invalid_choice(self) -> None:
        self.view.display_message("Invalid choice. Please try again.")

    def add_contact(self) -> None:
        name: str = self.view.get_user_input("Name: ")
        if not validate_name(name):
            self.view.display_message("Invalid name.")
            return

        phone: str = self.view.get_user_input("Phone Number: ")
        if not validate_phone_number(phone):
            self.view.display_message("Invalid phone number.")
            return

        if not self.model.is_phone_number_unique(phone):
            self.view.display_message("This phone number is already in use. Please enter a unique number.")
            return

        contact_id: str = self.model.add_contact((name, phone))
        self.view.display_message(f"Contact added with ID: {contact_id}")

    def display_contacts(self) -> None:
        contacts = self.model.get_all_contacts()
        if not contacts:
            self.view.display_message("No contacts available.")
        else:
            self.view.display_data(contacts)

    def remove_contact(self) -> None:
        contact_id: str = self.view.get_user_input("Enter ID of the contact to be removed: ")
        if self.model.remove_contact(contact_id):
            self.view.display_message("Contact removed successfully.")
        else:
            self.view.display_message("Contact not found.")

    def search_contacts(self) -> None:
        self.view.display_search_options()
        search_choice: int = int(self.view.get_user_choice(['1', '2'], "Choose search parameter (1- Name, 2- Phone Number): "))
        search_term: str = self.view.get_user_input("Enter search term: ")
        results = self.model.search_contacts(search_choice, search_term)
        if not results:
            self.view.display_message("No contacts found with the given search term.")
        else:
            self.view.display_data(results)

    def edit_contact(self) -> None:
        contact_id: str = self.view.get_user_input("Enter the ID of the contact to edit: ")
        if not self.model.find_contact(contact_id):
            self.view.display_message("Contact not found.")
            return

        new_name: str = self.view.get_user_input("New Name (leave blank to keep unchanged): ")
        new_phone: str = self.view.get_user_input("New Phone Number (leave blank to keep unchanged): ")

        if new_name and not validate_name(new_name):
            self.view.display_message("Invalid new name.")
            return

        if new_phone and not validate_phone_number(new_phone):
            self.view.display_message("Invalid new phone number.")
            return

        if new_phone and not self.model.is_phone_number_unique(new_phone):
            self.view.display_message("This phone number is already in use. Please enter a unique number.")
            return

        self.model.edit_contact(contact_id, new_name, new_phone)
        self.view.display_message("Contact updated successfully.")

    def handle_file_operations(self, choice: int) -> None:
        file_name: str = self.view.get_user_input("Enter file name: ")
        format_type: str = self.view.get_user_input("Enter file format (csv/JSON): ").upper()

        if format_type not in ['CSV', 'JSON']:
            self.view.display_message("Invalid file format. Please choose csv or JSON.")
            return

        file_name = self.ensure_correct_file_extension(file_name, format_type)

        success: bool
        message: str
        if choice == 6:
            success, message = self.model.load_data(file_name, format_type)
        elif choice == 7:
            success, message = self.model.save_data(file_name, format_type)

        self.view.display_message(message if success else "Operation failed.")

    def ensure_correct_file_extension(self, file_name: str, format_type: str) -> str:
        if format_type == 'CSV' and not file_name.endswith('.csv'):
            return file_name + '.csv'
        elif format_type == 'JSON' and not file_name.endswith('.json'):
            return file_name + '.json'
        return file_name
