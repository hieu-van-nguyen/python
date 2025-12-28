def maxProfit(prices):
    maxP = 0
    minPrice = prices[0]
    for price in prices:
        minPrice = min(minPrice, price)
        maxP = max(maxP, price - minPrice)
    return maxP;

print(maxProfit([10,1,5,6,7,1])) # 6