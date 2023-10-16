def check_statement():
    for x, y, z in ((a, b, c) for a in range(2) for b in range(2) for c in range(2)):
        print(x, y, z, "-", not (x or y or z) == (not x and not y and not z))


if __name__ == '__main__':
    check_statement()
