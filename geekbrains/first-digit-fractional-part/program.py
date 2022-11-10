import re


def get_float_input(value):
    s = input(value)
    if re.match(r'[+-]?[0-9]+\.[0-9]+', s) is None:
        raise ValueError("Input is not floating point number. Please try again ...")
    return float(s)


def get_fract_digit(fnum): return int(abs(fnum * 10) % 10)


if __name__ == '__main__':
    n = get_float_input()
    print(get_fract_digit(n))
