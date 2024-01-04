import random
import re


def get_float_input(prompt: str = "Enter a float number: ") -> float:
    float_pattern = re.compile(r'[+-]?[0-9]+\.[0-9]+')
    while True:
        user_input = input(prompt).strip()
        if float_pattern.fullmatch(user_input):
            return float(user_input)
        print("Invalid input. Please enter a valid floating-point number.")


def get_int_input(prompt="Enter a positive integer: "):
    int_pattern = re.compile(r'\d+')
    while True:
        user_input = input(prompt).strip()
        if int_pattern.fullmatch(user_input) and int(user_input) > 0:
            return int(user_input)
        print("Invalid input. Please enter a positive integer.")


def generate_random_floats(size, start, end):
    return [round(random.uniform(start, end), 2) for _ in range(size)]
