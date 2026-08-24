# Two Integer Sum II
#
# Given an integer array sorted in non-decreasing order, find two numbers
# whose sum equals the target.
#
# Return their 1-indexed positions as [index1, index2], where index1 < index2.
# The same element cannot be used twice.
# There is exactly one valid solution.
#
# Constraints:
# - 2 <= len(numbers) <= 30000
# - -1000 <= numbers[i] <= 1000
# - -1000 <= target <= 1000
#
# Example:
# Input: numbers = [1, 2, 3, 4], target = 3
# Output: [1, 2]
#
# Explanation:
# numbers[0] + numbers[1] = 1 + 2 = 3.
# Since the answer must be 1-indexed, return [1, 2].
#
# Time complexity: O(n)
# Additional space: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l , r = 0 , len(numbers) - 1
        res = []
        while l < r:
            # we take largest number (r) + smallest number (l)
            total = numbers[r] + numbers[l] 
            if total > target: #If the sum is too large, move r left to get a smaller number.
                r -= 1
            elif total < target: #If the sum is too small, move l right to get a larger number.
                l += 1
            else:
                res.append(l + 1)
                res.append(r + 1)
                return res