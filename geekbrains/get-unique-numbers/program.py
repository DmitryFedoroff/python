from random import randint


def get_int_input(prompt=""):
    while True:
        try:
            return list(map(int, input(prompt).strip().split()))
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")


def generate_2d_list(rows, cols, start, end):
    return [[randint(start, end) for _ in range(cols)] for _ in range(rows)]


def print_2d_list(matrix):
    print("\nGenerated two-dimensional array of random numbers:")
    for row in matrix:
        print(' '.join(f'{num:3d}' for num in row))


def get_unique_numbers(matrix):
    return sorted({number for row in matrix for number in row})


if __name__ == '__main__':
    rows, cols = get_int_input("Enter the number of rows and columns: ")
    start, end = get_int_input("Enter the lower and upper limits of the range: ")
    matrix = generate_2d_list(rows, cols, start, end)
    print_2d_list(matrix)
    unique_numbers = get_unique_numbers(matrix)
    print("\nList of unique numbers from the generated array:")
    print(unique_numbers)
