from random import *


if __name__ == '__main__':
    row = get_int_input("Enter number of rows: ")
    col = get_int_input("Enter number of columns: ")
    start = get_int_input("Enter lower limit of range: ")
    end = get_int_input("Enter upper limit of range: ")
    list_2d = [[randint(start, end) for x in range(col)] for y in range(row)]
    