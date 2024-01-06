import re


def get_float_input(prompt: str = "Enter the precision (e.g., 0.001): ") -> float:
    float_pattern = re.compile(r'^0\.0*1$')
    while True:
        user_input = input(prompt).strip()
        if float_pattern.fullmatch(user_input):
            return float(user_input)
        print("Invalid input. Please enter a valid precision (e.g., 0.001).")
