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


def count_positives_in_segment(sequence, segment_queries):
    cumulative_positives = [0]
    for number in sequence:
        cumulative_positives.append(cumulative_positives[-1] + (1 if number > 0 else 0))
    return [cumulative_positives[end] - cumulative_positives[start - 1] for start, end in segment_queries]
