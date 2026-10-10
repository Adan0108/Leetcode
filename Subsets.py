# # Subsets
#
# **MediumTopics**
#
# Given an array `nums` of **unique** integers,
# return all possible subsets of `nums`.
#
# The solution set must **not** contain duplicate subsets.
# You may return the solution in **any order**.
#
# **Example 1:**
#
# ```java
# Input: nums = [1,2,3]
#
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# ```
#
# **Example 2:**
#
# ```java
# Input: nums = [7]
#
# Output: [[],[7]]
# ```
#
# **Constraints:**
#
# - `1 <= nums.length <= 10`
# - `-10 <= nums[i] <= 10`

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []

        def backtrack(i):
            # If we have made a decision for every number,
            # save the current subset
            if i == len(nums):
                res.append(subset.copy())
                return

            # Choice 1: include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # Backtrack:
            # remove nums[i] before exploring the other choice
            subset.pop()

            # Choice 2: do not include nums[i]
            backtrack(i + 1)

        backtrack(0)

        return res