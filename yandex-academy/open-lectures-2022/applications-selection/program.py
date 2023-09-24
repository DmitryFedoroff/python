from operator import itemgetter


def find_max_applications(applications):
    applications.sort(key=itemgetter(1))
    count, end_time = 1, applications[0][1]
    for start, end in applications[1:]:
        if start >= end_time:
            count += 1
            end_time = end
    return count


if __name__ == '__main__':
    number_of_applications = int(input('Enter number of applications: '))
    applications = [list(map(int, input('Enter start and end times separated by space: ').split())) for _ in range(number_of_applications)]
    print(f'Max number of applications that can be fulfilled: {find_max_applications(applications)}')