def read_integer(prompt='Enter an integer: ') -> int:
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print('Invalid input. Please enter a valid integer.')


def read_integer_list(prompt='Enter a list of integers: '):
    while True:
        try:
            return list(map(int, input(prompt).split()))
        except ValueError:
            print('Invalid input. Please enter a list of valid integers.')


def gather_queries(query_count):
    return [read_integer_list(f'Enter indices for query {i + 1} (separated by space): ') for i in range(query_count)]
