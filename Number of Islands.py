# # Number of Islands
#
# **MediumTopics**
#
# Given a 2D grid `grid` where `'1'` represents land
# and `'0'` represents water,
# count and return the number of islands.
#
# An **island** is formed by connecting adjacent lands
# horizontally or vertically and is surrounded by water.
#
# You may assume water is surrounding the grid
# (i.e., all the edges are water).
#
# **Example 1:**
#
# ```java
# Input: grid = [
#     ["0","1","1","1","0"],
#     ["0","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
#   ]
#
# Output: 1
# ```
#
# **Example 2:**
#
# ```java
# Input: grid = [
#     ["1","1","0","0","1"],
#     ["1","1","0","0","1"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
#   ]
#
# Output: 4
# ```
#
# **Constraints:**
#
# - `1 <= grid.length, grid[i].length <= 100`
# - `grid[i][j]` is `'0'` or `'1'`.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0
        visited = set()

        def dfs(row, col):
            # Out of bounds
            if (
                row < 0 or col < 0 or
                row >= ROWS or col >= COLS
            ):
                return

            # Water or already visited
            if grid[row][col] == "0" or (row, col) in visited:
                return

            # Mark current land as visited
            visited.add((row, col))

            # Visit 4 directions
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(ROWS):
            for col in range(COLS):

                # Found a new island
                if grid[row][col] == "1" and (row, col) not in visited:
                    res += 1
                    dfs(row, col)

        return res