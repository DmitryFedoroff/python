from random import randint


if __name__ == '__main__':
    row, col = get_int_input()
    start, end = get_int_input()
    list_2d = [[randint(start, end) for x in range(col)] for y in range(row)]
