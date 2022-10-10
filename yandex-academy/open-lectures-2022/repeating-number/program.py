def find_rep_num(nums, k):
    last_k = set()
    for i in range(len(nums)):
        if nums[i] in last_k:
            return True
        last_k.add(nums[i])
        if i >= k:
            last_k.remove(nums[i - k])
    return False

n, k = map(int, input('Enter n and k: ').split())
nums = list(map(int, input('Enter numbers: ').split()))
