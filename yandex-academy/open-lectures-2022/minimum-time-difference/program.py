def find_min_dist(time_points):
    minute_points = sorted(int(h) * 60 + int(m) for h, m in (tp.split(':') for tp in time_points))
    min_dists = min(minute_points[i] - minute_points[i - 1] for i in range(1, len(minute_points)))
    return min(min_dists, 1440 + minute_points[0] - minute_points[-1])


if __name__ == '__main__':
    input('Enter number of trains: ')
    time_points = input('Enter 24-hour clock time points (HH:MM): ').split()
    print(f'Minimum minutes difference between arrival of two trains: {find_min_dist(time_points)}')
