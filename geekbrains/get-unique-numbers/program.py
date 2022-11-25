from random import randint


def get_int_input():
    while True:
        try:
            return list(map(int, input().split()))
        except ValueError:
            print("Input value is not integer. Please try again ...")


if __name__ == '__main__':
    row, col = get_int_input()
    start, end = get_int_input()
    list_2d = [[randint(start, end) for x in range(col)] for y in range(row)]
