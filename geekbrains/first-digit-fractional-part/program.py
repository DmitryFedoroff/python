import re


def get_float_input(prompt: str = "Enter a float number: ") -> float:
    float_pattern = re.compile(r'[+-]?[0-9]+\.[0-9]+')
    while True:
        user_input = input(prompt).strip()
        if float_pattern.fullmatch(user_input):
            return float(user_input)
        print("Invalid input. Please enter a valid floating-point number.")


def get_fractional_digit(float_num: float) -> int:
    return int(abs(float_num * 10) % 10)


if __name__ == '__main__':
    num = get_float_input()
    print(get_fractional_digit(num))
