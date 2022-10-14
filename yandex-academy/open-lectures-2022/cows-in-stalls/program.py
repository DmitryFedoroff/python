def count_cows(distance, k, stalls):
    counter = 1
    prev_pos = stalls[0]
    for i in range(1, len(stalls)):
        if stalls[i] - prev_pos >= distance:
            counter += 1
            prev_pos = stalls[i]
    return counter >= k

def binary_search(k, stalls):
    left_bound = 0
    right_bound = stalls[-1]
    while right_bound > left_bound:
        distance = (left_bound + right_bound + 1) // 2
        if count_cows(distance, k, stalls):
            left_bound = distance
        else:
            right_bound = distance - 1
    return left_bound

n, k = map(int, input('Enter number of stalls and cows: ').split())
stalls = list(map(int, input('Enter stalls coordinates: ').split()))
