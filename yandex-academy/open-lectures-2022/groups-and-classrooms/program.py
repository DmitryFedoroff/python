from itertools import islice


def maximize_seating(classroom_capacities, group_sizes):
    classroom_capacities.sort()
    group_sizes.sort()
    position = 0
    total_seated_groups = 0
    for group_size in group_sizes:
        classroom_capacities = islice((cap for cap in classroom_capacities if cap >= group_size), position, None)
        try:
            next(classroom_capacities)
            total_seated_groups += 1
            position += 1
        except StopIteration:
            break
    return total_seated_groups


if __name__ == '__main__':
    number_of_classrooms = int(input('Enter number of classrooms: '))
    classroom_capacities = list(map(int, input('Enter capacity of each classroom: ').split()))
    number_of_groups = int(input('Enter number of groups: '))
    group_sizes = list(map(int, input('Enter number of students in each group: ').split()))
    print(f'Maximum number of groups that can be seated: {maximize_seating(classroom_capacities, group_sizes)}')
