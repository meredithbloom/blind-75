# 268. Missing Number
'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.

'''

nums1 = [3,0,1]
nums2 = [0,1]
nums3 = [9,6,4,2,3,5,7,0,1]

# o(1) extra space complexity because we are creating a new set - might actually be o(n)
# o(n) time complexity - checking if each item in one set is present in another

def missingNumber(nums):
	n = len(nums)
	nums = set(nums)
	c = {x for x in range(0,n+1)}
	missing = c.difference(nums)
	for num in missing:
		print(num)
		return num

missingNumber(nums1)
missingNumber(nums2)
missingNumber(nums3)