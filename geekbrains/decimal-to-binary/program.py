def get_integer_input(prompt="Enter an integer: ") -> int:
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def decimal_to_binary(n: int) -> str:
    return bin(n)[2:]


if __name__ == '__main__':
    number = get_integer_input()
    print(decimal_to_binary(number))
