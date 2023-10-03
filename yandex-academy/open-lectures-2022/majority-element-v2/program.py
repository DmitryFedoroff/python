def find_majority(nums):
    return sorted(nums)[len(nums) // 2]


if __name__ == '__main__':
    n = int(input('Enter length of array: '))
    nums = list(map(int, input('Enter numbers: ').split()))
    print(f'Majority element in array: {find_majority(nums)}')
