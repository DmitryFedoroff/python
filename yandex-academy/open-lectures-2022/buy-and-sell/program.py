def find_trading_days(n, cost):
    min_index = 0
    max_gas = 1 / cost[0]
    max_revenue = 0
    trading_days = (0, 0)
    for i in range(1, n):
        if max_gas * cost[i] - 1 > max_revenue:
            max_revenue = max_gas * cost[i] - 1
            trading_days = (min_index + 1, i + 1)
        if 1 / cost[i] > max_gas:
            min_index = i
            max_gas = 1 / cost[i]
    return trading_days

n = int(input('Enter number of days: '))
cost = list(map(int, input('Prices of gas on each of days: ').split()))