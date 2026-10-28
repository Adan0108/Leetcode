# # Combination Sum II (Backtracking) (Remove Duplicate path branch)
#
# **MediumTopics**
#
# You are given an array of integers `candidates`,
# which may contain duplicates, and a target integer `target`.
#
# Return a list of all **unique combinations** of `candidates`
# where the chosen numbers sum to `target`.
#
# Each element from `candidates` may be chosen
# **at most once** within a combination.
#
# The solution set must not contain duplicate combinations.
#
# You may return the combinations in **any order**,
# and the order of the numbers in each combination
# can be in **any order**.
#
# **Example 1:**
#
# ```java
# Input: candidates = [9,2,2,4,6,1,5], target = 8
#
# Output: [
#   [1,2,5],
#   [2,2,4],
#   [2,6]
# ]
# ```
#
# **Example 2:**
#
# ```java
# Input: candidates = [1,2,3,4,5], target = 7
#
# Output: [
#   [1,2,4],
#   [2,5],
#   [3,4]
# ]
# ```
#
# **Constraints:**
#
# - `1 <= candidates.length <= 100`
# - `1 <= candidates[i] <= 50`
# - `1 <= target <= 30`

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        candidates.sort()

        def backtracking(start, curSum):
            if curSum == target:
                res.append(cur.copy())
                return

            for i in range(start, len(candidates)):

                # Skip duplicate choices at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since sorted, all later numbers will also be too large
                if curSum + candidates[i] > target:
                    break

                # Add current number
                cur.append(candidates[i])

                backtracking(i + 1, curSum + candidates[i])

                # Backtrack
                cur.pop()

        backtracking(0, 0)

        return res