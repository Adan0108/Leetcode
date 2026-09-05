# Longest Substring Without Repeating Characters (sliding window)
#
# Given a string `s`, find the length of the longest substring
# without duplicate characters.
#
# A substring is a continuous sequence of characters within a string.
#
# Example 1:
#
# Input: s = "zxyzxyz"
#
# Output: 3
#
# Explanation:
#
# The substring "xyz" is the longest substring without duplicate characters.
#
# Example 2:
#
# Input: s = "xxxx"
#
# Output: 1
#
# Constraints:
#
# 0 <= s.length <= 50,000
# `s` may contain printable ASCII characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        res = 0
        j = 0
        for i in range(len(s)):
            #loop until find that duplicate character to start new substring
            while s[i] in check:
                check.remove(s[j])
                j += 1
            check.add(s[i])
            cur = i - j + 1
            res = max(res, cur)
        return res