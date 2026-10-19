# # Generate Parentheses (Backtracking)
#
# **MediumTopics**
#
# You are given an integer `n`.
# Return all well-formed parentheses strings that you can generate
# with `n` pairs of parentheses.
#
# **Example 1:**
#
# ```java
# Input: n = 1
#
# Output: ["()"]
# ```
#
# **Example 2:**
#
# ```java
# Input: n = 3
#
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# ```
#
# You may return the answer in **any order**.
#
# **Constraints:**
#
# - `1 <= n <= 7`
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []

        def backtracking(openPa, closePa):

            # When we have n "(" and n ")",
            # current path is a valid combination
            if len(cur) == 2 * n:
                res.append("".join(cur))
                return

            # Choice 1: add "("
            # We can only add it if we have used less than n opening brackets
            if openPa < n:
                cur.append("(")

                # Explore this choice
                backtracking(openPa + 1, closePa)

                # Backtrack:
                # remove "(" before trying another choice
                cur.pop()

            # Choice 2: add ")"
            # We can only close if there is an unmatched "("
            #
            # Example:
            # open = 2, close = 1
            # => we are allowed to add ")"
            if closePa < openPa:
                cur.append(")")

                # Explore this choice
                backtracking(openPa, closePa + 1)

                # Backtrack
                cur.pop()

        backtracking(0, 0)
        return res