# # Search a 2D Matrix (Binary Search)
#
#
# **MediumTopicsCompany TagssvgHints**
#
# You are given an `m x n` 2-D integer array `matrix` and an integer `target`.
#
# - Each row in `matrix` is sorted in *non-decreasing* order.
# - The first integer of every row is greater than the last integer of the previous row.
#
# Return `true` if `target` exists within `matrix` or `false` otherwise.
#
# Can you write a solution that runs in `O(log(m * n))` time?
#
# **Example 1:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/7ca61f56-00d4-4fa0-26cf-56809028ac00/public)
#
# ```java
# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
#
# Output: true
# ```
#
# **Example 2:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/f25f2085-ce04-4447-9cee-f0a66c32a300/public)
#
# ```java
# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
#
# Output: false
# ```

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #search row first to allocate number in which row
        top = 0
        bottom = len(matrix) - 1

        #top <= target <= bot
        while top <= bottom:
            row = (top + bottom) // 2

            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break

        # Target is not inside any row range
        if top > bottom:
            return False
        
        row = (top + bottom) // 2

        l = 0
        r = len(matrix[row]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return False
            
