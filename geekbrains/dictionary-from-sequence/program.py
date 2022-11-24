def get_int_input():
    while True:
        try:
            s = input()
            return int(s)
        except ValueError:
            print("Input value is not integer. Please try again ...")


def create_dict(n):
    return {x: 3 * x + 1 for x in range(1, n + 1)}


if __name__ == '__main__':
    num = get_int_input()
