# Valid Palindrome (STRING PROBLEM)
#
# Given a string s, return True if it is a palindrome.
# Otherwise, return False.
#
# A palindrome reads the same forward and backward.
# The comparison is case-insensitive and ignores all
# non-alphanumeric characters.
#
# Alphanumeric characters include:
# Letters: A-Z and a-z
# Numbers: 0-9
#
# Example 1:
# Input: s = "Was it a car or a cat I saw?"
# Output: True
#
# Explanation:
# After removing non-alphanumeric characters and converting the
# letters to lowercase, the string becomes:
# "wasitacaroracatisaw"
#
# This string is a palindrome.
#
# Example 2:
# Input: s = "tab a cat"
# Output: False
#
# Explanation:
# After processing, the string becomes "tabacat", which is not
# a palindrome.
#
# Constraints:
# 1 <= len(s) <= 1000
# s contains only printable ASCII characters.
#
# Recommended complexity:
# Time: O(n)
# Space: O(1)
#
# n is the length of the input string.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l , r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isWord(s[l]):
                l += 1
            while r > l and not self.isWord(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l , r = l + 1, r - 1
        return True

    def isWord(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9')
        )
        