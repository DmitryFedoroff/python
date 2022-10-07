def find_majority(n, nums):
    count = {}
    for i in nums:
        count[i] = count.get(i, 0) + 1
    for val in count:
        if count[val] > n // 2:
            result = val
    return result

n = int(input('Enter length of array: '))
nums = list(map(int, input('Enter numbers: ').split()))
print(f'Majority element in array: {find_majority(n, nums)}')