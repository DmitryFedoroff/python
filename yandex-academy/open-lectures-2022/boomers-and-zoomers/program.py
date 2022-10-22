def count_invites(n, age):
    age.sort()
    left, right, result = 0, 0, 0
    for i in range(n):
        while (left < n) and (age[left] <= 0.5 * age[i] + 7):
            left += 1
        while (right < n) and (age[right] <= age[i]):
            right += 1
        if right > left + 1:
            result += right - left - 1
    return result

n = int(input('Number of people: '))
age = list(map(int, input('Age of people: ').split()))
print(f'Total number of birthday invitations: {count_invites(n, age)}')
