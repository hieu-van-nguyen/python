# time complexity is O(n) and space complexity is O(1) where n is the length of the array
def buy_and_sell_stock_one(prices):
    min_price, max_profit = float("inf"), 0.0
    for price in prices:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    
    return max_profit

print(buy_and_sell_stock_one([310, 310, 275,275, 260, 260, 290, 230, 230])) # 30