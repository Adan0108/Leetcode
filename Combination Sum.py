# # Combination Sum
#
# **MediumTopics**
#
# You are given an array of **distinct** integers `nums`
# and a target integer `target`.
#
# Your task is to return a list of all **unique combinations**
# of `nums` where the chosen numbers sum to `target`.
#
# The **same** number may be chosen from `nums`
# an **unlimited number of times**.
#
# Two combinations are the same if the frequency of each
# of the chosen numbers is the same,
# otherwise they are different.
#
# You may return the combinations in **any order**
# and the order of the numbers in each combination
# can be in **any order**.
#
# **Example 1:**
#
# ```java
# Input:
# nums = [2,5,6,9]
# target = 9
#
# Output: [[2,2,5],[9]]
# ```
#
# Explanation:
# 2 + 2 + 5 = 9.
# We use 2 twice, and 5 once.
#
# 9 = 9.
# We use 9 once.
#
# **Example 2:**
#
# ```java
# Input:
# nums = [3,4,5]
# target = 16
#
# Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]
# ```
#
# **Example 3:**
#
# ```java
# Input:
# nums = [3]
# target = 5
#
# Output: []
# ```
#
# **Constraints:**
#
# - All elements of `nums` are **distinct**.
# - `1 <= nums.length <= 20`
# - `2 <= nums[i] <= 30`
# - `2 <= target <= 30`

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        numSet = []

        def backtrack(i, curSum):
            # Found a valid combination
            if curSum == target:
                res.append(numSet.copy())
                return

            # Stop if:
            # 1. We used all numbers
            # 2. Current sum is already too large
            if i == len(nums) or curSum > target:
                return

            # Choice 1: use nums[i]
            #
            # Keep i the same because we are allowed
            # to use nums[i] again
            numSet.append(nums[i])
            backtrack(i, curSum + nums[i])

            # Backtrack
            numSet.pop()

            # Choice 2: skip nums[i]
            # Move to the next number
            backtrack(i + 1, curSum)

        backtrack(0, 0)

        return res