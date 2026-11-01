# # Islands and Treasure (BFS for efficient)
#
# **MediumTopicss**
#
# You are given a `m×n` 2D `grid`
# initialized with these three possible values:
#
# 1. `-1` - A water cell that *can not* be traversed.
# 2. `0` - A treasure chest.
# 3. `INF` - A land cell that *can* be traversed.
#
# We use the integer:
#
# `2^31 - 1 = 2147483647`
#
# to represent `INF`.
#
# Fill each land cell with the distance
# to its nearest treasure chest.
#
# If a land cell cannot reach a treasure chest,
# then the value should remain `INF`.
#
# Assume the grid can only be traversed
# up, down, left, or right.
#
# Modify the `grid` **in-place**.
#
# **Example 1:**
#
# ```java
# Input: [
#   [2147483647,-1,0,2147483647],
#   [2147483647,2147483647,2147483647,-1],
#   [2147483647,-1,2147483647,-1],
#   [0,-1,2147483647,2147483647]
# ]
#
# Output: [
#   [3,-1,0,1],
#   [2,2,1,-1],
#   [1,-1,2,-1],
#   [0,-1,3,4]
# ]
# ```
#
# **Example 2:**
#
# ```java
# Input: [
#   [0,-1],
#   [2147483647,2147483647]
# ]
#
# Output: [
#   [0,-1],
#   [1,2]
# ]
# ```
#
# **Constraints:**
#
# - `m == grid.length`
# - `n == grid[i].length`
# - `1 <= m, n <= 100`
# - `grid[i][j]` is one of `{-1, 0, 2147483647}`

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()

        #Push all the treasure location so they can all start at once
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((col,row))

        while q:
            x, y = q.popleft()

            directions = [
                (x + 1, y),
                (x - 1, y),
                (x, y + 1),
                (x, y - 1)
            ]

            for nx, ny in directions:
                # Out of bounds
                if nx < 0 or ny < 0 or nx >= COLS or ny >= ROWS:
                    continue
                # Ignore water, treasures,
                # and cells already updated
                if grid[ny][nx] != 2147483647:
                    continue

                grid[ny][nx] = grid[y][x] + 1
                q.append((nx, ny))

        