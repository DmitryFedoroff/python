from typing import List, Tuple
from colorama import Fore, init

init(autoreset=True)


class PhonebookView:
    def display_menu(self) -> None:
        menu_choices: List[str] = [
            '1 - Add Contact',
            '2 - Show All Contacts',
            '3 - Remove Contact',
            '4 - Search Contacts',
            '5 - Edit Contact',
            '6 - Import Data',
            '7 - Export Data',
            '8 - Exit'
        ]
        print(Fore.CYAN + '=' * 30 + ' MENU ' + '=' * 30 + Fore.RESET)
        for choice in menu_choices:
            print(Fore.YELLOW + choice + Fore.RESET)
        print(Fore.CYAN + '=' * 65 + Fore.RESET)

    def display_search_options(self) -> None:
        print("Choose search parameter:\n1 - Name\n2 - Phone Number")

    def get_user_choice(self, valid_choices: List[str], prompt: str) -> str:
        while True:
            choice = input(prompt).strip()
            if choice in valid_choices:
                return choice
            else:
                print(f"Invalid input. Please choose one of the following: {', '.join(valid_choices)}")

    def get_search_choice(self) -> int:
        self.display_search_options()
        choice = self.get_user_choice(['1', '2'], "Your choice: ")
        return int(choice)

    def get_user_input(self, prompt: str) -> str:
        return input(prompt)

    def display_data(self, data: List[Tuple[str, str, str]]) -> None:
        for contact_id, name, phone in data:
            print(f'ID: {contact_id}, Name: {name}, Phone: {phone}')

    def display_message(self, message: str) -> None:
        print(message)
