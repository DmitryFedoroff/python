import re


def get_int_input(prompt="Enter a natural number: "):
    int_pattern = re.compile(r'^[1-9]\d*$')
    while True:
        user_input = input(prompt).strip()
        if int_pattern.fullmatch(user_input):
            return int(user_input)
        print("Invalid input. Please enter a natural number.")
