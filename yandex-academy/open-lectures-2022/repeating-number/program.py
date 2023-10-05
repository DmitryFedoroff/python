def has_repeating_number_within_distance(measurements, k):
    last_seen_index = {}
    for idx, measurement in enumerate(measurements):
        if measurement in last_seen_index and idx - last_seen_index[measurement] <= k:
            return True
        last_seen_index[measurement] = idx
    return False


if __name__ == '__main__':
    n, k = map(int, input('Enter n and k: ').split())
    measurements = list(map(int, input('Enter measurements: ').split()))
    print('Yes' if has_repeating_number_within_distance(measurements, k) else 'No')
