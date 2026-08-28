# Valid Sudoku (HASHMAP PROBLEM)

#
# Given a 9 x 9 Sudoku board, return True if the board is valid.
# Otherwise, return False.
#
# A Sudoku board is valid when:
#
# 1. Each row contains no duplicate digits from 1 to 9.
# 2. Each column contains no duplicate digits from 1 to 9.
# 3. Each 3 x 3 sub-box contains no duplicate digits from 1 to 9.
#
# A board does not need to be complete or solvable to be valid.
# Empty cells are represented by ".".
#
# Example 1:
# Input:
# board = [
#     ["1", "2", ".", ".", "3", ".", ".", ".", "."],
#     ["4", ".", ".", "5", ".", ".", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", ".", "3"],
#     ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
#     [".", ".", ".", "8", ".", "3", ".", ".", "5"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", ".", ".", ".", ".", ".", "2", ".", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "8"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
# ]
#
# Output: True
#
# Example 2:
# Input:
# board = [
#     ["1", "2", ".", ".", "3", ".", ".", ".", "."],
#     ["4", ".", ".", "5", ".", ".", ".", ".", "."],
#     [".", "9", "1", ".", ".", ".", ".", ".", "3"],
#     ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
#     [".", ".", ".", "8", ".", "3", ".", ".", "5"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", ".", ".", ".", ".", ".", "2", ".", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "8"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
# ]
#
# Output: False
#
# Explanation:
# The top-left 3 x 3 sub-box contains two "1" digits.
#
# Constraints:
# len(board) == 9
# len(board[i]) == 9
# board[i][j] is a digit from "1" to "9" or ".".
#
# Recommended complexity:
# Time: O(n^2)
# Space: O(n^2)
#
# n is the number of rows in the square grid.
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        validCol = defaultdict(set)
        validRow = defaultdict(set)
        validBox = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in validRow[r]
                    or board[r][c] in validCol[c]
                    or board[r][c] in validBox[(r // 3,c // 3)]):
                    return False
        
                validCol[c].add(board[r][c])
                validRow[r].add(board[r][c])
                validBox[(r // 3,c // 3)].add(board[r][c])
        
        return True

                
        