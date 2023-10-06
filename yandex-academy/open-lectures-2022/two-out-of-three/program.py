def find_common_elements(set1, set2, set3):
    common_12_3 = set1 & set2 | set1 & set3 | set2 & set3
    return sorted(common_12_3)


if __name__ == '__main__':
    _ = int(input('Enter length of 1st list: '))
    set1 = set(map(int, input('Enter numbers: ').split()))
    _ = int(input('Enter length of 2nd list: '))
    set2 = set(map(int, input('Enter numbers: ').split()))
    _ = int(input('Enter length of 3rd list: '))
    set3 = set(map(int, input('Enter numbers: ').split()))
    common_elements = find_common_elements(set1, set2, set3)
    print('Numbers present in at least two out of three lists:', *common_elements)
