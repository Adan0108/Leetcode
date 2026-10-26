# # Palindrome Partitioning
#
# **MediumTopics**
#
# Given a string `s`, split `s` into substrings
# where every substring is a palindrome.
#
# Return all possible lists of palindromic substrings.
#
# You may return the solution in **any order**.
#
# **Example 1:**
#
# ```java
# Input: s = "aab"
#
# Output: [["a","a","b"],["aa","b"]]
# ```
#
# **Example 2:**
#
# ```java
# Input: s = "a"
#
# Output: [["a"]]
# ```
#
# **Constraints:**
#
# - `1 <= s.length <= 20`
# - `s` contains only lowercase English letters.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []

        def isPalindrome(s):
            return s == s[::-1]

        def backtracking(i):
            # If we used the whole string,
            # cur is one valid partition
            if i == len(s):
                res.append(cur.copy())
                return

            # Try every substring starting from i
            for c in range(i, len(s)):
                part = s[i:c + 1]

                # Only choose palindrome substring
                if isPalindrome(part):
                    cur.append(part)

                    # Continue after this substring
                    backtracking(c + 1)

                    # Undo choice
                    cur.pop()

        backtracking(0)
        return res

