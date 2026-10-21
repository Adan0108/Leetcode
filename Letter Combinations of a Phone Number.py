# # Letter Combinations of a Phone Number (Backtracking)
#
# **MediumTopics**
#
# You are given a string `digits` made up of digits
# from `2` through `9` inclusive.
#
# Each digit (not including 1) is mapped to a set of characters
# as shown below.
#
# A digit could represent any one of the characters it maps to.
#
# Return all possible letter combinations that `digits`
# could represent.
#
# You may return the answer in **any order**.
#
# [Phone keypad letter mapping]
# (https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/d5eb2098-bd7f-47a1-554a-ad77a39f3100/public)
#
# **Example 1:**
#
# ```java
# Input: digits = "34"
#
# Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
# ```
#
# **Example 2:**
#
# ```java
# Input: digits = ""
#
# Output: []
# ```
#
# **Constraints:**
#
# - `0 <= digits.length <= 4`
# - `2 <= digits[i] <= 9`

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def backtracking(i, cur):

            # If current combination has one letter
            # for every digit, save it
            if len(cur) == len(digits):
                res.append(cur)
                return

            # Try every possible letter for digits[i]
            for c in phone[digits[i]]:
                backtracking(i + 1, cur + c)

        if digits:
            backtracking(0, "")

        return res