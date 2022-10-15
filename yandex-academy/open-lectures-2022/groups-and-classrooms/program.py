def seat_groups(class_cap, group_size):
    group_size.sort()
    class_cap.sort()
    pos = 0
    result = 0
    for now in group_size:
        while pos < len(class_cap) and class_cap[pos] < now:
            pos += 1
        if pos != len(class_cap):
            result += 1
            pos += 1
    return result

n = int(input('Enter number of classrooms: '))
class_cap = list(map(int, input('Enter capacity of each classroom: ').split()))
m = int(input('Enter number of groups: '))
group_size = list(map(int, input('Enter number of students in each group: ').split()))
print(f'Maximum number of groups can be seated: {seat_groups(class_cap, group_size)}')
