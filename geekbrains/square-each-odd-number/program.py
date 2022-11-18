def get_int_input():
    while True:
        try:
            s = input()
            return int(s)
        except ValueError:
            print("Input value is not integer. Please try again ...")


def square_odd_nums(ls):
    [print(x ** 2, end='\t') for x in ls if x % 2 > 0]


if __name__ == '__main__':
    n = get_int_input()
    lst = list(range(n))
