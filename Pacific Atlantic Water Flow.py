# # Pacific Atlantic Water Flow (Reverse DFS from valid condition)
#
# **MediumTopics**
#
# You are given a rectangular island `heights`
# where `heights[r][c]` represents the **height above sea level**
# of the cell at coordinate `(r, c)`.
#
# The island borders the **Pacific Ocean**
# from the top and left sides.
#
# The island borders the **Atlantic Ocean**
# from the bottom and right sides.
#
# Water can flow in **four directions**
# (up, down, left, or right)
# from a cell to a neighboring cell
# with **height equal or lower**.
#
# Water can also flow into the ocean
# from cells adjacent to the ocean.
#
# Find all cells where water can flow
# from that cell to **both**
# the Pacific and Atlantic oceans.
#
# Return the result as a **2D list**
# where each element is `[r, c]`
# representing the row and column of the cell.
#
# You may return the answer in **any order**.
#
# **Example 1:**
#
# [image]
# (https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/3899fae1-ab18-4d6b-15b4-c7f7aa224700/public)
#
# ```java
# Input: heights = [
#   [4,2,7,3,4],
#   [7,4,6,4,7],
#   [6,3,5,3,6]
# ]
#
# Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]
# ```
#
# **Example 2:**
#
# ```java
# Input: heights = [[1],[1]]
#
# Output: [[0,0],[1,0]]
# ```
#
# **Constraints:**
#
# - `1 <= heights.length, heights[r].length <= 100`
# - `0 <= heights[r][c] <= 1000`

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        res = []

        # Store cells that can reach each ocean
        pacific, atlantic = set(), set()

        def dfs(row, col, visit, prevHeight):
            # Stop if:
            # - already visited
            # - out of bounds
            # - current cell is lower than previous cell
            #   because we are searching in reverse flow
            if (
                (row, col) in visit or
                row < 0 or col < 0 or
                row == ROWS or col == COLS or
                heights[row][col] < prevHeight
            ):
                return

            # This cell can reach the current ocean
            visit.add((row, col))

            # Search in 4 directions
            # Only same or higher cells can be reached in reverse
            dfs(row + 1, col, visit, heights[row][col])
            dfs(row - 1, col, visit, heights[row][col])
            dfs(row, col + 1, visit, heights[row][col])
            dfs(row, col - 1, visit, heights[row][col])

        # Pacific touches the top row
        # Atlantic touches the bottom row
        for col in range(COLS):
            dfs(0, col, pacific, heights[0][col])
            dfs(ROWS - 1, col, atlantic, heights[ROWS - 1][col])

        # Pacific touches the left column
        # Atlantic touches the right column
        for row in range(ROWS):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, COLS - 1, atlantic, heights[row][COLS - 1])

        # Cells that can reach both oceans
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append((row, col))

        return res