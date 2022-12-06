def get_int_input():
    while True:
        try:
            s = input()
            return int(s)
        except ValueError:
            print("Input value is not integer. Please try again ...")


def get_seq(n):
    return [((-3) ** x) for x in range(n)]


if __name__ == '__main__':
    num = get_int_input()
