def get_int_input():
    while True:
        try:
            s = input()
            return int(s)
        except ValueError:
            print("Input value is not integer. Please try again ...")


def check_multiple(n):
    return (n % 5 == 0 or n % 10 == 0 or n % 15 == 0) and n % 30 != 0


if __name__ == '__main__':
    num = get_int_input()
