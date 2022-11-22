def get_int_input():
    while True:
        try:
            s = input()
            return int(s)
        except ValueError:
            print("Input value is not integer. Please try again ...")


def summ_sequence(n):
    return sum([round((1 + 1 / x) ** x, 2) for x in range(1, n + 1)])


if __name__ == '__main__':
    num = get_int_input()
