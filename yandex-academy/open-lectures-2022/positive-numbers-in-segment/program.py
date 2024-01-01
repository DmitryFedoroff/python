def read_integer(prompt='Enter an integer: ') -> int:
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print('Invalid input. Please enter a valid integer.')
