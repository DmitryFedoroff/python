import re


def get_float_input():
    s = input()
    if re.match(r'[+-]?[0-9]+\.[0-9]+', s) is None:
        raise ValueError("Input is not floating point number. Please try again ...")
    return float(s)


def sum_digits(fnum):
    return [sum(map(int, list(x))) for x in str(abs(fnum)).split('.')]


if __name__ == '__main__':
    n = get_float_input()
