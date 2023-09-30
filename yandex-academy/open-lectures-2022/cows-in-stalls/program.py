def count_cows(min_distance, num_cows, stalls):
    count, last_stall = 1, stalls[0]
    for stall in stalls[1:]:
        if stall - last_stall >= min_distance:
            count += 1
            last_stall = stall
    return count >= num_cows


def find_max_distance(num_cows, stalls):
    stalls.sort()
    low, high = 0, stalls[-1] - stalls[0]
    while low < high:
        mid = (low + high + 1) // 2
        if count_cows(mid, num_cows, stalls):
            low = mid
        else:
            high = mid - 1
    return low


if __name__ == '__main__':
    num_stalls, num_cows = map(int, input('Enter number of stalls and cows: ').split())
    stalls = list(map(int, input('Enter stalls coordinates: ').split()))
    print(f'Largest possible allowable distance: {find_max_distance(num_cows, stalls)}')
