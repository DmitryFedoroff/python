INF = int(1e18)
MAX_ELEM = int(1e9)

def calc_util(min_util):
    result = 0
    count = 0
    for i in range(1, n + 1):
        if utility[i] < min_util:
            break
        count += 1
        result += utility[i]
    
    j = 2
    while (j <= n) and (utility[1] + utility[j] >= min_util):
        j += 1

    pref_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        pref_sum[i] = pref_sum[i - 1] + utility[i]

    for i in range(1, n + 1):
        if i + 1 >= j:
            break
        while (j - 1 > i) and (utility[i] + utility[j - 1] < min_util):
            j -= 1
        count += (j - i - 1)
        result += pref_sum[j - 1] - pref_sum[i] + utility[i] * (j - i -1)
    if count >= k:
        return result - (count - k) * min_util
    else:
        return INF

def binary_search():
    utility.sort()
    utility.append(0)
    utility.reverse()
    l = -MAX_ELEM
    r = MAX_ELEM
    while r > l:
        m = (l + r + 1) // 2
        if calc_util(m) != INF:
            l = m
        else:
            r = m - 1
    return l

n, k = map(int, input().split())
utility = list(map(int, input().split()))