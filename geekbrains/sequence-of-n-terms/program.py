def get_integer_input(prompt="Enter an integer: ") -> int:
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def generate_sequence(length: int) -> list:
    return [(-3) ** i for i in range(length)]


if __name__ == '__main__':
    num_elements = get_integer_input("Enter the length of the sequence: ")
    print(*generate_sequence(num_elements))
