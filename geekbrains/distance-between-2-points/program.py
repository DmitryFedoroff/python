import math


def get_int_input():
    while True:
        try:
            return list(map(int, input().split()))
        except ValueError:
            print("Input value is not integer. Please try again ...")


def calc_dist(p, q):
    return round(math.sqrt(sum((x - y) ** 2 for x, y in zip(p, q))), 2)


if __name__ == '__main__':
    a = get_int_input()
    b = get_int_input()
