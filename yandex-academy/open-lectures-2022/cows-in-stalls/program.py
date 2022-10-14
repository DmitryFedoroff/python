def count_cows(distance, k, stalls):
    counter = 1
    prev_pos = stalls[0]
    for i in range(1, len(stalls)):
        if stalls[i] - prev_pos >= distance:
            counter += 1
            prev_pos = stalls[i]
    return counter >= k

n, k = map(int, input('Enter number of stalls and cows: ').split())
stalls = list(map(int, input('Enter stalls coordinates: ').split()))
