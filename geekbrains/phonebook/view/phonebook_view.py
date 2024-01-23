from colorama import Fore


class PhonebookView:
    def display_menu(self):
        menu_choices = [
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

    def get_search_choice(self):
        while True:
            print("Choose search parameter:\n1 - Name\n2 - Phone Number")
            choice = input("Your choice: ").strip()
            if choice in ['1', '2']:
                return int(choice)
            print("Invalid input. Please choose 1 or 2.")

    def get_user_input(self, prompt):
        return input(prompt)

    def display_data(self, data):
        for contact in data:
            print(', '.join(contact))

    def display_message(self, message):
        print(message)
