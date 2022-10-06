def find_nums(s1, s2, s3):
    result = s1 & s2
    merged12 = s1.union(s2)
    result = result.union(merged12 & s3)
    return result

l1 = (input('Enter length of 1st list: '))
s1 = set(map(int, input('Enter numbers: ').split()))
l2 = (input('Enter length of 2nd list: '))
s2 = set(map(int, input('Enter numbers: ').split()))
l3 = (input('Enter length of 3rd list: '))
s3 = set(map(int, input('Enter numbers: ').split()))
print(f'Numbers present in at least two out of three lists:', *sorted(find_nums(s1, s2, s3)))
