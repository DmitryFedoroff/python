def find_min_dist(n, time_points):
    day = 1440
    minute_points = []
    for now_time in time_points:
        h, m = map(int, now_time.split(':'))
        minute_points.append(h * 60 + m)
    minute_points.sort()
    min_dist = day + minute_points[0] - minute_points[-1]
    for i in range(1, len(minute_points)):
        min_dist = min(min_dist, minute_points[i] - minute_points[i - 1])
    return min_dist

n = int(input('Enter number of trains: '))
time_points = input('Enter 24-hour clock time points (HH:MM): ').split()