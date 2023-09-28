def find_optimal_trading_days(num_days, investment, prices):
    buy_day, sell_day, max_profit, min_price_day = 0, 0, 0, 0
    for i in range(1, num_days):
        profit = prices[i] * investment / prices[min_price_day] - investment
        if profit > max_profit:
            buy_day, sell_day, max_profit = min_price_day + 1, i + 1, profit
        if prices[i] < prices[min_price_day]:
            min_price_day = i
    return (0, 0) if max_profit == 0 else (buy_day, sell_day), round(max_profit, 2)


if __name__ == "__main__":
    investment = int(input("Enter initial investment: "))
    num_days = int(input("Enter number of days: "))
    prices = list(map(int, input("Enter prices of gas on each of days: ").split()))
    days, profit = find_optimal_trading_days(num_days, investment, prices)
    print(f"Numbers of days for buying and selling gas: {days[0]} {days[1]}")
    print(f"Max revenue: {profit}")
