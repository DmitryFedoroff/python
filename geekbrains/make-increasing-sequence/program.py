import random


def get_int_input():
    while True:
        try:
            s = input()
            return int(s)
        except ValueError:
            print("Input value is not integer. Please try again ...")


def make_incr_seq(ls):
    seq = []
    [seq.append(ls[i]) for i in range(len(ls)) if ls[i] == max(ls[:i + 1:]) and ls[i] not in seq]
    return seq


if __name__ == '__main__':
    n = get_int_input()
    lst = [random.randint(1, 10) for i in range(n)]
    print(*lst)
