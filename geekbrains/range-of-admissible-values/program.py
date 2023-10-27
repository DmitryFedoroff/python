def get_integer_input(prompt="Enter an integer: ") -> int:
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


if __name__ == '__main__':
    quadrant_ranges = ['(x > 0, y > 0)', '(x < 0, y > 0)', '(x < 0, y < 0)', '(x > 0, y < 0)']
    quadrant_number = get_integer_input("Range of admissible values in each of 4 quadrants. Enter the quadrant number (1-4): ")
    print(quadrant_ranges[quadrant_number - 1])
