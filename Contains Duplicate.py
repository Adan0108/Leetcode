# Contains Duplicate
# SET PROBLEM
# Given an integer array nums, return True if any value appears
# more than once in the array. Otherwise, return False.
#
# Example 1:
# Input: nums = [1, 2, 3, 3]
# Output: True
#
# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: False
#
# Constraints:
# 0 <= len(nums) <= 10^5
# -10^9 <= nums[i] <= 10^9
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appear = set()
        for num in nums:
            if num in appear:
                return True
            appear.add(num)
        return False
        