# # Word Search (Backtrack)
#
# **MediumTopics**
#
# Given a 2-D grid of characters `board` and a string `word`,
# return `true` if the word is present in the grid,
# otherwise return `false`.
#
# For the word to be present, it must be possible to form it
# with a path in the board using horizontally or vertically
# neighboring cells.
#
# The same cell may not be used more than once in a word.
#
# **Example 1:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/7c1fcf82-71c8-4750-3ddd-4ab6a666a500/public)
#
# ```java
# Input:
# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ],
# word = "CAT"
#
# Output: true
# ```
#
# **Example 2:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/79721392-44b6-4de7-c571-d3d1640ac100/public)
#
# ```java
# Input:
# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ],
# word = "BAT"
#
# Output: false
# ```
#
# **Constraints:**
#
# - `1 <= board.length, board[i].length <= 5`
# - `1 <= word.length <= 10`
# - `board` and `word` consist only of lowercase and uppercase English letters.


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        path = set()

        def dfs(r, c, i):
            # Matched every character in word
            if i == len(word):
                return True

            # Stop if:
            # - out of bounds
            # - current character does not match
            # - this cell is already used in current path
            if (
                r < 0 or c < 0
                or r >= ROWS or c >= COLS
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False

            # Mark current cell as used
            path.add((r, c))

            # Try all 4 directions
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )

            # Backtrack so this cell can be reused
            # by a different search path
            path.remove((r, c))

            return res

        # Try every cell as the starting point
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False