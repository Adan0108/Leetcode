# # Max Area of Island
#
# **MediumTopics**
#
# You are given a matrix `grid` where `grid[i]`
# is either a `0` (representing water)
# or `1` (representing land).
#
# An island is defined as a group of `1`'s
# connected horizontally or vertically.
#
# You may assume all four edges of the grid
# are surrounded by water.
#
# The **area** of an island is defined as
# the number of cells within the island.
#
# Return the maximum **area** of an island in `grid`.
#
# If no island exists, return `0`.
#
# **Example 1:**
#
# [image]
# (https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/8eeb491c-c8ff-4ed6-78ed-ce4cf87d7200/public)
#
# ```java
# Input: grid = [
#   [0,1,1,0,1],
#   [1,0,1,0,1],
#   [0,1,1,0,1],
#   [0,1,0,0,1]
# ]
#
# Output: 6
# ```
#
# Explanation:
# `1`'s cannot be connected diagonally,
# so the maximum area of the island is `6`.
#
# **Constraints:**
#
# - `1 <= grid.length, grid[i].length <= 50`

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        visited = set()

        def dfs(x , y):
            if y >= ROWS or x >= COLS or y < 0 or x < 0:
                return 0
            
            if grid[y][x] == 0 or (x , y) in visited:
                return 0
            
            visited.add((x,y))
            return (
            1
            + dfs(x + 1, y)
            + dfs(x - 1, y)
            + dfs(x , y + 1)
            + dfs(x , y - 1)
            )

        
        for row in range(ROWS):
            for col in range(COLS):
                cur = dfs(col, row)
                res = max(cur, res)
        return res
        