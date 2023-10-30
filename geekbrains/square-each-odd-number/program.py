def get_integer_list(prompt="Enter a list of integers: "):
    while True:
        try:
            return list(map(int, input(prompt).split()))
        except ValueError:
            print("Invalid input. Please enter a list of valid integers.")


def square_odd_numbers(numbers):
    return ' '.join(str(x ** 2) for x in numbers if x % 2)


if __name__ == '__main__':
    print(square_odd_numbers(get_integer_list()))
