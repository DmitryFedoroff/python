class PhonebookView:
    def display_menu(self):
        menu_choices = [
            '1 - Enter Data',
            '2 - Show All Contacts',
            '3 - Import Data',
            '4 - Export Data',
            '5 - Exit',
        ]
        for choice in menu_choices:
            print(choice)

    def get_user_input(self, prompt):
        return input(prompt)

    def display_data(self, data):
        for contact in data:
            print(', '.join(contact))

    def display_message(self, message):
        print(message)
