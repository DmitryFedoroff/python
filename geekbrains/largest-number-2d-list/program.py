from random import *


def get_int_input(value):
    while True:
        try:
            s = input(value)
            return int(s)
        except ValueError:
            print("Input value is not integer. Please try again ...")


def print_list(lst): [print(*x, sep='\t') for x in lst]


def find_max(lst): return max(max(x) for x in lst)


if __name__ == '__main__':
    row, col = get_int_input()
    start, end = get_int_input()
    list_2d = [[randint(start, end) for x in range(col)] for y in range(row)]
    print_list(list_2d)
    print(find_max(list_2d))
