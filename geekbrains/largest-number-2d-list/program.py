from random import randint


def get_integer_input(prompt="Enter an integer: ") -> int:
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_dimensions():
    return map(get_integer_input, ["Enter number of rows: ", "Enter number of columns: "])


def get_range():
    return map(get_integer_input, ["Enter lower limit: ", "Enter upper limit: "])


def generate_2d_list(rows, cols, start, end):
    return [[randint(start, end) for _ in range(cols)] for _ in range(rows)]


def print_2d_list(matrix):
    for row in matrix:
        print('\t'.join(map(str, row)))


def find_largest(matrix):
    return max(max(row) for row in matrix)


if __name__ == '__main__':
    rows, cols = get_dimensions()
    start, end = get_range()
    matrix = generate_2d_list(rows, cols, start, end)
    print_2d_list(matrix)
    largest_number = find_largest(matrix)
    print(f"The largest number in the generated 2D list is: {largest_number}")
