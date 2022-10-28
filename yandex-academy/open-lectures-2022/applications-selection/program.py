def find_max_applic(n):
    applic = []
    for i in range(n):
        s = list(map(int, input('Enter number si and fi: ').split()))
        applic.append(s)
    count = 1
    applic.sort(key = lambda x: x[1])
    end = applic[0][1]
    for i in range(1, n):
        if applic[i][0] >= end:
            count += 1
            end = applic[i][1]
    return count

n = int(input('Enter number of applications: '))
