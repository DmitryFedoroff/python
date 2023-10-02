def find_majority(nums):
    candidate = count = 0
    for num in nums:
        if count == 0: candidate = num
        count += 1 if num == candidate else -1
    return candidate if nums.count(candidate) > len(nums) // 2 else 'No majority element'


if __name__ == '__main__':
    _ = input('Enter length of array: ')
    nums = list(map(int, input('Enter numbers: ').split()))
    print(f'Majority element in array: {find_majority(nums)}')
