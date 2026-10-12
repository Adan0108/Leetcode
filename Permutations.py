# # Permutations
#
# **MediumTopics**
#
# Given an array `nums` of **unique** integers,
# return all the possible permutations.
#
# You may return the answer in **any order**.
#
# **Example 1:**
#
# ```java
# Input: nums = [1,2,3]
#
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# ```
#
# **Example 2:**
#
# ```java
# Input: nums = [7]
#
# Output: [[7]]
# ```
#
# **Constraints:**
#
# - `1 <= nums.length <= 6`
# - `-10 <= nums[i] <= 10`

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        numSet = []

        def backtracking():
            # When permutation has enough numbers,
            # save a copy of the current path
            if len(numSet) == len(nums):
                res.append(numSet.copy())
                return

            # Try every number
            for num in nums:

                # Skip numbers already used
                if num in numSet:
                    continue

                # Choose
                numSet.append(num)

                # Explore
                backtracking()

                # Backtrack
                numSet.pop()

        backtracking()
        return res
            
            
        