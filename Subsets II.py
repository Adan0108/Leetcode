# # Subsets II (Backtracking)
#
# **MediumTopics**
#
# You are given an array `nums` of integers,
# which may contain duplicates.
#
# Return all possible subsets.
#
# The solution must **not** contain duplicate subsets.
#
# You may return the solution in **any order**.
#
# **Example 1:**
#
# ```java
# Input: nums = [1,2,1]
#
# Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]
# ```
#
# **Example 2:**
#
# ```java
# Input: nums = [7,7]
#
# Output: [[],[7],[7,7]]
# ```
#
# **Constraints:**
#
# - `1 <= nums.length <= 11`
# - `-20 <= nums[i] <= 20`

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        cur = []

        def backtracking(i):
            if i == len(nums):
                res.add(tuple(cur))
                return
            
            #append the number
            cur.append(nums[i])
            backtracking(i + 1)

            #pop for backtrack
            cur.pop()
            #not append the number path
            backtracking(i + 1)

        #sort becasue (1,2) and (2,1) is the same subset
        #sort so duplicate subsets have the same order
        nums.sort()
        backtracking(0)

        return [list(s) for s in res]