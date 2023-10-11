INF = int(1e18)
MAX_ELEM = int(1e9)


def calc_total_utility(min_util, utilities, n, k):
    total_utility = 0
    count = 0
    for util in utilities[:n]:
        if util < min_util:
            break
        count += 1
        total_utility += util

    j = 2
    while (j <= n) and (utilities[0] + utilities[j - 1] >= min_util):
        j += 1

    pref_sum = [0]
    for util in utilities:
        pref_sum.append(pref_sum[-1] + util)

    for i in range(1, n + 1):
        if i + 1 >= j:
            break
        while (j - 1 > i) and (utilities[i - 1] + utilities[j - 2] < min_util):
            j -= 1
        count += (j - i - 1)
        total_utility += pref_sum[j - 1] - pref_sum[i] + utilities[i - 1] * (j - i - 1)

    if count >= k:
        return total_utility - (count - k) * min_util
    return INF


def find_min_util(utilities, n, k):
    utilities.sort(reverse=True)
    left, right = -MAX_ELEM, MAX_ELEM
    while left < right:
        mid = (left + right + 1) // 2
        if calc_total_utility(mid, utilities, n, k) != INF:
            left = mid
        else:
            right = mid - 1
    return left


if __name__ == '__main__':
    n = int(input('Enter number of ingredients: '))
    k = int(input('Enter number of potions: '))
    utilities = list(map(int, input('Enter ingredients utility (higher number is better): ').split()))
    max_util = find_min_util(utilities, n, k)
    print(f'Maximum total utility of potions: {calc_total_utility(max_util, utilities, n, k)}')
