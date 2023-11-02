def get_integer_input(prompt="Enter an integer: ") -> int:
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def sum_of_sequence(num_terms: int) -> float:
    return sum((1 + 1 / x) ** x for x in range(1, num_terms + 1))


if __name__ == '__main__':
    number_of_terms = get_integer_input()
    print(f"{sum_of_sequence(number_of_terms):.2f}")
