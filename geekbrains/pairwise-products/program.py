import re
from random import randint


def get_int_input(prompt="Enter a positive integer: "):
    int_pattern = re.compile(r'\d+')
    while True:
        user_input = input(prompt).strip()
        if int_pattern.fullmatch(user_input) and int(user_input) > 0:
            return int(user_input)
        print("Invalid input. Please enter a positive integer.")


def generate_random_list(size, start, end):
    return [randint(start, end) for _ in range(size)]


def multiply_pairs(numbers):
    if not numbers:
        return []
    return [numbers[i] * numbers[-1 - i] for i in range((len(numbers) + 1) // 2)]
