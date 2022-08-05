# BEST TIME TO BUY AND SELL STOCK

# Given an array prices where prices[i] is the price of a given stock on the ith day

# You want to maximize profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock

# Return the maximum profit you can achieve from this transation. If you cannot achieve any profit, return 0.

# Constraints
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4

# Array, Dynamic Programming


# Examples

# Input
prices1 = [7,1,5,3,6,4]

prices2 = [7,6,4,3,1]
prices3 = [1,4,2]
prices4 = [3,2,6,5,0,3]

# brute force would be to compare every item with every item after it in the array - O(n^2)
# should be able to get it down to O(n) by progressing through the list from both directions until they meet in the middle

def difference(sell, buy):
	if (sell-buy) < 0:
		return 0
	else:
		return (sell - buy)


def maxProfit(prices):
	print(prices)
	# starting from each end and moving towards center
	buy = 0
	sell = len(prices)-1
	#max_profit = 0
	low = prices[buy]
	low_index = 0
	high = prices[len(prices)-1]
	high_index = len(prices)-1
	print(f'starting low is {low} and starting high is {high}')
	# before buy and sell indices meet in the middle
	while low_index < high_index:
		print(f'current high index is {high_index} and current low index is {low_index}')
		if prices[buy] < low and low_index < high_index:
			print(f'current low index is {low_index}')
			low = prices[buy]
			low_index = buy
			print(f'new lowest price is {low} at index {low_index}')
		if prices[sell] > high and high_index > low_index:
			high = prices[sell]
			high_index = sell
			print(f'new highest sell is {high} at index {high_index}')	
		buy += 1
		sell -= 1
	# print(f'current high index is {high_index} and current low index is {low_index}')
	print(difference(high, low))
	
	


#maxProfit(prices1)
#maxProfit(prices2)
#maxProfit(prices3)
maxProfit(prices4)