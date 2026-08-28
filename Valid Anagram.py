# Valid Anagram (HASHMAP PROBLEM)
#
# Given two strings s and t, return True if the two strings are
# anagrams of each other. Otherwise, return False.
#
# Two strings are anagrams if they contain the same characters,
# with each character appearing the same number of times,
# regardless of order.
#
# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: True
#
# Example 2:
# Input: s = "jar", t = "jam"
# Output: False
#
# Example 3:
# Input: s = "x", t = "x"
# Output: True
#
# Constraints:
# 1 <= len(s), len(t) <= 5 * 10^4
# s and t consist of lowercase English letters.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checkS = defaultdict(int)
        checkT = defaultdict(int)

        for c in s:
            checkS[c] += 1
        
        for c in t:
            checkT[c] += 1

        return checkT == checkS
        