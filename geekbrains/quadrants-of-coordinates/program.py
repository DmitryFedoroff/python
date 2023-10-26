import re


def get_float_input(prompt: str = "Enter a number: ") -> float:
    float_pattern = re.compile(r'[+-]?(\d+(\.\d+)?|\.\d+)')
    while True:
        user_input = input(prompt).strip()
        if float_pattern.fullmatch(user_input):
            return float(user_input)
        print("Invalid input. Please enter a valid number.")


def determine_quadrant_or_axis(x: float, y: float) -> str:
    if x == 0 and y == 0:
        return "Origin"
    elif x == 0:
        return "OY axis"
    elif y == 0:
        return "OX axis"
    else:
        quadrant = 'I' if x > 0 and y > 0 else \
                   'II' if x < 0 and y > 0 else \
                   'III' if x < 0 and y < 0 else 'IV'
        return f"{quadrant} quadrant"


if __name__ == '__main__':
    x_coord = get_float_input("Enter the x coordinate: ")
    y_coord = get_float_input("Enter the y coordinate: ")
    result = determine_quadrant_or_axis(x_coord, y_coord)
    print(f"The point lies in the {result}.")
