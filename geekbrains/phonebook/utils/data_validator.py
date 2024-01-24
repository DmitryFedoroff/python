import re


PHONE_NUMBER_PATTERN = re.compile(r'^\+?[0-9]{10,15}$')
NAME_PATTERN = re.compile(r'^[a-zA-Z\s]+$')
MENU_CHOICE_PATTERN = re.compile(r'^[1-8]$')


def validate_phone_number(phone_number):
    if not phone_number or phone_number.isspace():
        print("Phone number cannot be empty or just whitespace.")
        return False

    if PHONE_NUMBER_PATTERN.fullmatch(phone_number) is None:
        print("Invalid phone number format. Please enter a valid number.")
        return False
    return True


def validate_name(name):
    if not name or name.isspace():
        print("Name cannot be empty or just whitespace.")
        return False
    if NAME_PATTERN.fullmatch(name) is None:
        print("Invalid name format. Name should contain only letters and spaces.")
        return False
    return True


def get_menu_choice():
    while True:
        choice = input("Enter your choice (1-8): ").strip()
        if MENU_CHOICE_PATTERN.fullmatch(choice):
            return int(choice)
        print("Invalid input. Please enter a number between 1 and 8.")
