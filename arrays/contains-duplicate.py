# Contains duplicate
# Given an integer array nums, return true is any value appears at least twice in the array, and return false if every element is distinct

# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

nums1 = [1,2,3,1]
nums2 = [1,2,3,4]
nums3 = [1,1,1,3,3,4,3,2,4,2]


def containsDuplicate(nums):
    numbers = {}
    for num in nums:
        if num in numbers.keys():
            return True
        else:
            numbers[num] = 1
    return False


print(containsDuplicate(nums1))
print(containsDuplicate(nums2))
print(containsDuplicate(nums3))
