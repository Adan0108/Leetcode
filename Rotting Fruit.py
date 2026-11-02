# # Rotting Fruit (BFS)
#
# **MediumTopics**
#
# You are given a 2-D matrix `grid`.
#
# Each cell can have one of three possible values:
#
# - `0` representing an empty cell
# - `1` representing a fresh fruit
# - `2` representing a rotten fruit
#
# Every minute, if a fresh fruit is horizontally
# or vertically adjacent to a rotten fruit,
# then the fresh fruit also becomes rotten.
#
# Return the minimum number of minutes that must elapse
# until there are zero fresh fruits remaining.
#
# If this state is impossible within the grid,
# return `-1`.
#
# **Example 1:**
#
# [image]
# (https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/5daa219c-ae90-4027-41c3-6ea4d9158300/public)
#
# ```java
# Input: grid = [[1,1,0],[0,1,1],[0,1,2]]
#
# Output: 4
# ```
#
# **Example 2:**
#
# ```java
# Input: grid = [[1,0,1],[0,2,0],[1,0,1]]
#
# Output: -1
# ```
#
# **Constraints:**
#
# - `1 <= grid.length, grid[i].length <= 10`

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0          # Number of minutes
        fruits = 0       # Number of fresh oranges
        q = deque()      # Store all rotten oranges

        # Count fresh oranges and add rotten oranges to the queue
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fruits += 1

                if grid[row][col] == 2:
                    q.append((col, row))

        # Continue while there are fresh oranges
        # and rotten oranges that can spread
        while fruits > 0 and q:

            # Process all rotten oranges in the current minute
            for rotten in range(len(q)):
                x, y = q.popleft()

                # Check 4 directions
                directions = [
                    (x + 1, y),
                    (x - 1, y),
                    (x, y + 1),
                    (x, y - 1),
                ]

                for nx, ny in directions:

                    # Skip out-of-bound cells
                    if nx < 0 or ny < 0 or nx >= COLS or ny >= ROWS:
                        continue

                    # If the neighbor is a fresh orange
                    if grid[ny][nx] == 1:
                        fruits -= 1              # One less fresh orange
                        q.append((nx, ny))       # It can spread next minute
                        grid[ny][nx] = 2         # Mark it as rotten

            # One BFS layer = one minute
            res += 1

        # If no fresh orange remains, return minutes
        # Otherwise, some oranges cannot be reached
        return res if fruits == 0 else -1