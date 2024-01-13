import re


def validate_phone_number(phone_number):
    pattern = re.compile(r'^\+?[0-9]{10,15}$')
    return pattern.match(phone_number) is not None


def validate_name(name):
    return name.isalpha()


def get_menu_choice():
    pattern = re.compile(r'^[1-6]$')
    while True:
        choice = input("Enter your choice (1-6): ").strip()
        if pattern.fullmatch(choice):
            return int(choice)
        print("Invalid input. Please enter a number between 1 and 6.")
