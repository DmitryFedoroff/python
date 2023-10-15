def get_integer_input(prompt="Enter an integer: ") -> int:
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def is_special_multiple(number: int) -> bool:
    return number % 30 in {5, 10, 15}


if __name__ == '__main__':
    user_input = get_integer_input()
    print(is_special_multiple(user_input))
