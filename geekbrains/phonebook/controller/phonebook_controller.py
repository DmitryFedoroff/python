from model.phonebook_model import PhonebookModel
from view.phonebook_view import PhonebookView
from utils.data_validator import validate_phone_number, validate_name, get_menu_choice


class PhonebookController:
    def __init__(self):
        self.model = PhonebookModel()
        self.view = PhonebookView()

    def start(self):
        while True:
            self.view.display_menu()
            choice = get_menu_choice()
            if choice == 1:
                self.add_contact()
            elif choice == 2:
                self.display_contacts()
            elif choice == 3:
                self.remove_contact()
            elif choice == 4:
                self.search_contacts()
            elif choice in [5, 6]:
                self.handle_file_operations(choice - 1)
            elif choice == 7:
                break

    def add_contact(self):
        name = self.view.get_user_input("Name: ")
        if not validate_name(name):
            self.view.display_message("Invalid name.")
            return

        phone = self.view.get_user_input("Phone Number: ")
        if not validate_phone_number(phone):
            self.view.display_message("Invalid phone number.")
            return

        contact = [name, phone]
        self.model.add_contact(contact)
        self.view.display_message("Contact added.")

    def display_contacts(self):
        contacts = self.model.get_all_contacts()
        if not contacts:
            self.view.display_message("No contacts available.")
        else:
            self.view.display_data(contacts)

    def remove_contact(self):
        name = self.view.get_user_input("Enter name of the contact to be removed: ")
        if self.model.remove_contact(name):
            self.view.display_message("Contact removed successfully.")
        else:
            self.view.display_message("Contact not found.")

    def search_contacts(self):
        search_choice = self.view.get_search_choice()
        search_term = self.view.get_user_input("Enter search term: ")
        results = self.model.search_contacts(search_choice, search_term)
        if not results:
            self.view.display_message("No contacts found with the given search term.")
        else:
            self.view.display_data(results)

    def handle_file_operations(self, choice):
        file_name = self.view.get_user_input("Enter file name: ")
        format_type = self.view.get_user_input("Enter file format (csv/JSON): ").upper()

        if format_type not in ['CSV', 'JSON']:
            self.view.display_message("Invalid file format. Please choose csv or JSON.")
            return

        file_name = self.ensure_correct_file_extension(file_name, format_type)

        success, message = False, ""
        if choice == 4:
            success, message = self.model.load_data(file_name, format_type)
        elif choice == 5:
            success, message = self.model.save_data(file_name, format_type)

        self.view.display_message(message if not success else "Operation successful.")

    def ensure_correct_file_extension(self, file_name, format_type):
        if format_type == 'CSV' and not file_name.endswith('.csv'):
            return file_name + '.csv'
        elif format_type == 'JSON' and not file_name.endswith('.JSON'):
            return file_name + '.JSON'
        return file_name
