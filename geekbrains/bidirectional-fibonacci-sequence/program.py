import re


def get_int_input(prompt="Enter a non-negative integer: "):
    int_pattern = re.compile(r'\d+')
    while True:
        user_input = input(prompt).strip()
        if int_pattern.fullmatch(user_input):
            return int(user_input)
        print("Invalid input. Please enter a non-negative integer.")