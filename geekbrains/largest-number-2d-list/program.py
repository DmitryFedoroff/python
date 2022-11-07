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
    row = get_int_input("Enter number of rows: ")
    col = get_int_input("Enter number of columns: ")
    start = get_int_input("Enter lower limit of range: ")
    end = get_int_input("Enter upper limit of range: ")
    list_2d = [[randint(start, end) for x in range(col)] for y in range(row)]
    print("Two-dimensional list: ")
    print_list(list_2d)
