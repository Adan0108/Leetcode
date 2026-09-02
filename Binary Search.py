# Binary Search
#
# You are given an array of distinct integers `nums`, sorted in
# ascending order, and an integer `target`.
#
# Search for `target` inside `nums`.
#
# If `target` exists, return its index.
# Otherwise, return -1.
#
# The solution must run in O(log n) time.
#
# Example 1:
#
# Input: nums = [-1,0,2,4,6,8], target = 4
#
# Output: 3
#
# Example 2:
#
# Input: nums = [-1,0,2,4,6,8], target = 3
#
# Output: -1
#
# Constraints:
#
# 1 <= nums.length <= 10,000
# -10,000 < nums[i], target < 10,000
# All integers in `nums` are unique.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        h = len(nums) - 1
        l = 0
        # Continue while the search area is still valid.
        while l <= h:
            # Calculate the middle index.
            m = (l + h) // 2
            #m = l + (h - l) // 2 can also use this to avoid int overload
            
            # Compare the middle value with target.
            if nums[m] < target:
                # Target must be on the right side.
                l = m + 1
            elif nums[m] > target:
                # Target must be on the left side.
                h = m - 1
            else:
                # Return the index of target.
                return m
        # Target does not exist.
        return -1