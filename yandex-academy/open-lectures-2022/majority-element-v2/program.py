def find_majority(n, nums):
    nums.sort()
    return nums[n // 2]

n = int(input('Enter length of array: '))
nums = list(map(int, input('Enter numbers: ').split()))