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

	max_profit = 0
	cheapest = float('inf')
	
	for i in range(len(prices)):
		if prices[i] < cheapest:
			cheapest = prices[i]
		elif prices[i] - cheapest > max_profit:
			max_profit = prices[i] - cheapest
	
	return max_profit
	
	


#maxProfit(prices1)
#maxProfit(prices2)
#maxProfit(prices3)
print(maxProfit(prices4))