# Longest Consecutive Sequence
#
# Given an integer array nums, return the length of the longest
# consecutive sequence that can be formed.
#
# A consecutive sequence is a sequence in which each element is
# exactly 1 greater than the previous element.
#
# The elements do not need to be consecutive in the original array.
#
# The algorithm must run in O(n) time.
#
# Example 1:
# Input: nums = [2, 20, 4, 10, 3, 4, 5]
# Output: 4
#
# Explanation:
# The longest consecutive sequence is [2, 3, 4, 5].
#
# Example 2:
# Input: nums = [0, 3, 2, 5, 4, 6, 1, 1]
# Output: 7
#
# Explanation:
# The longest consecutive sequence is [0, 1, 2, 3, 4, 5, 6].
#
# Constraints:
# 0 <= len(nums) <= 100,000
# -10^9 <= nums[i] <= 10^9
#
# Recommended complexity:
# Time: O(n)
# Space: O(n)
#
# n is the size of the input array.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #O(n) -> Set()
        #if it start of an array then n - 1 dont exist
        #if it start of an array then we count or not we skip
        res = 0
        check = set(nums)

        for num in nums:
            if (num - 1) not in check:
                cur = 1
                while (num + cur) in check:
                    cur += 1
                res = max(cur,res)
        return res
            
        