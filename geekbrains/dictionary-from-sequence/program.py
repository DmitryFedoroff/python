def get_integer_input(prompt="Enter an integer: ") -> int:
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def create_number_to_formula_dict(n: int) -> dict:
    return {x: 3 * x + 1 for x in range(1, n + 1)}


if __name__ == '__main__':
    num_elements = get_integer_input()
    print(create_number_to_formula_dict(num_elements))
