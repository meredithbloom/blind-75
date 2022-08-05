# 70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Constraints
# 1 <= n <= 45

n1 = 2
# output = 2
# There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

n2 = 3
# output = 3
# There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

from itertools import product, permutations

# def check_sum(iter, target):
# 	sum = 0
# 	for item in iter:
# 		sum += item
# 	return sum


def climbStairs(n):
	
	def dynamic(n, cache):
		if n not in cache:
			cache[n] = dynamic(n-1, cache) + dynamic(n-2, cache)
		return cache[n]
	return dynamic(n, {1:1, 2:2})
	
	


print(climbStairs(2))
print(climbStairs(3))
print(climbStairs(4))
