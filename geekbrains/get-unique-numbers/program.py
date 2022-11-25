from random import randint


def get_int_input():
    while True:
        try:
            return list(map(int, input().split()))
        except ValueError:
            print("Input value is not integer. Please try again ...")


def print_list(lst):
    [print(*x, sep='\t') for x in lst]


def get_unique_nums(lst):
    return sorted(set(i for j in lst for i in j))


if __name__ == '__main__':
    row, col = get_int_input()
    start, end = get_int_input()
    list_2d = [[randint(start, end) for x in range(col)] for y in range(row)]
    print_list(list_2d)
    print(get_unique_nums(list_2d))
