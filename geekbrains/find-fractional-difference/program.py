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


def find_fractional_difference(numbers):
    fractional_parts = [abs(num) - abs(int(num)) for num in numbers]
    max_fraction = max(fractional_parts)
    min_fraction = min(fractional_parts)
    return max_fraction - min_fraction, max_fraction, min_fraction


if __name__ == '__main__':
    num = get_int_input('Enter the number of elements in the list: ')
    start = get_float_input('Enter the start of the range (floating-point number): ')
    end = get_float_input('Enter the end of the range (floating-point number): ')
    random_list = generate_random_floats(num, start, end)
    fractional_diff, max_fraction, min_fraction = find_fractional_difference(random_list)
    print(f'List of random floating-point numbers: {random_list}')
    print(
        f'Difference between the maximum and minimum values of the fractional parts: '
        f'{round(fractional_diff, 2)} (Max: {round(max_fraction, 2)}, Min: {round(min_fraction, 2)})'
    )
