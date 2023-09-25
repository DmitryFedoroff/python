def count_birthday_invitations(people_ages):
    people_ages.sort()
    count = 0
    left = 0
    right = 0
    for i in range(len(people_ages)):
        while left < len(people_ages) and people_ages[left] <= 0.5 * people_ages[i] + 7:
            left += 1
        while right < len(people_ages) and people_ages[right] <= people_ages[i]:
            right += 1
        count += max(0, right - left - 1)
    return count


if __name__ == '__main__':
    num_people = int(input('Number of people: '))
    ages = map(int, input('Age of people: ').split())
    print(f'Total number of birthday invitations: {count_birthday_invitations(list(ages))}')