def maxProfit(prices):
    min_stock = 99999
    profit = 0

    for stock in prices:
        if stock < min_stock:
            min_stock = stock
        profit = max(profit, stock - min_stock)
    return profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
