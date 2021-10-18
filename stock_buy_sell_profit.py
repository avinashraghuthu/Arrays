# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii


def stock_buy_sell(prices):
	index = 0
	max_profit = 0
	prices_len = len(prices)
	while index < prices_len - 1:
		while index < prices_len - 1 and prices[index + 1] <= prices[index]:
			index += 1
		buy_price = prices[index]
		while index < prices_len - 1 and prices[index + 1] >= prices[index]:
			index += 1
		sell_price = prices[index]
		print(buy_price, sell_price)
		max_profit += (sell_price - buy_price)
		index += 1
	return max_profit


prices = [7, 1, 5, 3, 6, 4]

# Function call
print(stock_buy_sell(prices))
