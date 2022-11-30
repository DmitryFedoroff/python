import random


def get_int_input():
    while True:
        try:
            s = input()
            return int(s)
        except ValueError:
            print("Input value is not integer. Please try again ...")


if __name__ == '__main__':
    n = get_int_input()
    lst = [random.randint(1, 10) for i in range(n)]
    print(*lst)
