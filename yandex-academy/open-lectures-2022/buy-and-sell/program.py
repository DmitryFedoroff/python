def find_trading_days(n, amount, cost):
    min_index = 0
    max_gas = amount / cost[0]
    max_revenue = 0
    trading_days = (0, 0)
    for i in range(1, n):
        if max_gas * cost[i] - amount > max_revenue:
            max_revenue = max_gas * cost[i] - amount
            trading_days = (min_index + 1, i + 1)
        if amount / cost[i] > max_gas:
            min_index = i
            max_gas = amount / cost[i]
    return trading_days, max_revenue

amount = int(input('Enter initial investment: '))
n = int(input('Enter number of days: '))
cost = list(map(int, input('Enter prices of gas on each of days: ').split()))
print('Numbers of days for buying and selling gas:', *find_trading_days(n, amount, cost)[0])
print('Max revenue:', find_trading_days(n, amount, cost)[1])