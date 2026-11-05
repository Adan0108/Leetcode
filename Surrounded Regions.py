# # Surrounded Regions (DFS to check from only valid condition)
#
# **MediumTopics**
#
# You are given an `m x n` matrix `board`
# containing letters `'X'` and `'O'`.
#
# Capture regions that are surrounded.
#
# - **Connect:** A cell is connected to adjacent cells
#   horizontally or vertically.
#
# - **Region:** To form a region, connect every `'O'` cell.
#   Regions can have any shape.
#   They do not need to be squares or rectangles.
#
# - **Surround:** A region is surrounded if none of the `'O'`
#   cells in that region are on the edge of the board.
#
# Such regions are **completely enclosed**
# by `'X'` cells.
#
# To capture a **surrounded region**,
# replace all `'O'`s with `'X'`s **in-place**
# within the original board.
#
# You do not need to return anything.
#
# **Example 1:**
#
# [image]
# (https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/1dcdb7cb-9299-440d-e96d-d55fe6c54700/public)
#
# ```java
# Input: board = [
#   ["X","X","X","X"],
#   ["X","O","O","X"],
#   ["X","X","O","X"],
#   ["X","O","X","X"]
# ]
#
# Output: [
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","O","X","X"]
# ]
# ```
#
# Explanation:
#
# The bottom `'O'` region is not captured
# because it touches the edge of the board,
# so it cannot be surrounded.
#
# **Example 2:**
#
# ```java
# Input: board = [["X"]]
#
# Output: [["X"]]
# ```
#
# **Constraints:**
#
# - `1 <= board.length, board[i].length <= 200`
# - `board[i][j]` is `'X'` or `'O'`.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        safe = set()

        ROWS = len(board)
        COLS = len(board[0])

        # Find all O cells connected to the border
        def dfs(x, y):
            if (
                x < 0 or y < 0 or
                x >= COLS or y >= ROWS or
                board[y][x] == "X" or
                (x, y) in safe
            ):
                return

            safe.add((x, y))

            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        # Top and bottom borders
        for col in range(COLS):
            dfs(col, 0)
            dfs(col, ROWS - 1)

        # Left and right borders
        for row in range(ROWS):
            dfs(0, row)
            dfs(COLS - 1, row)

        # Capture all O cells not connected to the border
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and (col, row) not in safe:
                    board[row][col] = "X"