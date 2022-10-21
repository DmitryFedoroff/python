INF = int(1e18)
MAX_ELEM = int(1e9)

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