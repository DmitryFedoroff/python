import re


def get_float_input(prompt: str = "Enter a float number: ") -> float:
    float_pattern = re.compile(r'[+-]?[0-9]+\.[0-9]+')
    while True:
        user_input = input(prompt).strip()
        if float_pattern.fullmatch(user_input):
            return float(user_input)
        print("Invalid input. Please enter a valid floating-point number.")


def sum_digits_of_float(floating_number: float) -> list[int]:
    return [sum(int(digit) for digit in part) for part in str(abs(floating_number)).split('.')]


if __name__ == '__main__':
    user_float = get_float_input()
    print(*sum_digits_of_float(user_float))