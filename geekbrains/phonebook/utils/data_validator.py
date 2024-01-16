import re


PHONE_NUMBER_PATTERN = re.compile(r'^\+?[0-9]{10,15}$')
NAME_PATTERN = re.compile(r'^[a-zA-Z]+$')
MENU_CHOICE_PATTERN = re.compile(r'^[1-6]$')


def validate_phone_number(phone_number):
    return PHONE_NUMBER_PATTERN.fullmatch(phone_number) is not None


def validate_name(name):
    return NAME_PATTERN.fullmatch(name) is not None


def get_menu_choice():
    while True:
        choice = input("Enter your choice (1-6): ").strip()
        if MENU_CHOICE_PATTERN.fullmatch(choice):
            return int(choice)
        print("Invalid input. Please enter a number between 1 and 6.")
