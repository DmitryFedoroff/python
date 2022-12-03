import random


def get_int_input():
    while True:
        try:
            s = input()
            return int(s)
        except ValueError:
            print("Input value is not integer. Please try again ...")


def find_uniq_vals(ls):
    uniq = []
    [uniq.append(x) for x in ls if ls.count(x) == 1]
    return uniq


if __name__ == '__main__':
    n = get_int_input()
    lst = [random.randint(1, 10) for i in range(n)]
    print(*lst)
    print(*find_uniq_vals(lst))
