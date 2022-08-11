prices = [7, 1, 5, 3, 6, 4]


def maxProfit(prices):
    l, r = 0, 1
    profit = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit += prices[r] - prices[l]
        l, r = r, r + 1
    return profit


print(maxProfit(prices))
