# TWO SUM
# Given an array of integer "nums" and an integer "target", return indices of the two numbers such that they add up to "target"

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Constraints
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9


# SOLUTION HAS TIME COMPLEXITY O(N)

nums1 = [2,7,11,15]
target1 = 9

nums2 = [3,2,4]
target2 = 6

nums3 = [3,3] 
target3 = 6



def twoSum(nums, target):
    dif = {}
    for i in range(len(nums)): # O(n) - iterating through list
        difference = target - nums[i]
        print(difference)
        if nums[i] in dif.keys(): # O(1) - dictionary access
            index1 = dif[nums[i]]
            return [i, index1]
        else:
            dif[difference] = i
            

 
 
print(twoSum(nums1, target1))
print(twoSum(nums2, target2))
print(twoSum(nums3, target3))
            
            