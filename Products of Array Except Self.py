# Products of Array Except Self
#
# Given an integer array nums, return an array output where
# output[i] is the product of every element in nums except nums[i].
#
# Each product is guaranteed to fit in a 32-bit integer.
#
# Follow-up:
# Solve the problem in O(n) time without using division.
#
# Example 1:
# Input: nums = [1, 2, 4, 6]
# Output: [48, 24, 12, 8]
#
# Example 2:
# Input: nums = [-1, 0, 1, 2, 3]
# Output: [0, -6, 0, 0, 0]
#
# Constraints:
# 2 <= len(nums) <= 100,000
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed
# to fit in a 32-bit integer.
#
# Recommended complexity:
# Time: O(n)
# Space: O(n)
#
# n is the size of the input array.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for j in range(len(nums) -1 , -1 , -1):
            res[j] *= suffix
            suffix *= nums[j]

        return res