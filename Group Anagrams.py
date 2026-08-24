# Group Anagrams
#
# Given an array of strings strs, group all anagrams together
# into sublists. The output can be returned in any order.
#
# An anagram contains exactly the same characters as another
# string, but the characters may appear in a different order.
#
# Example 1:
# Input: strs = ["act", "pots", "tops", "cat", "stop", "hat"]
# Output: [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]
#
# Example 2:
# Input: strs = ["x"]
# Output: [["x"]]
#
# Example 3:
# Input: strs = [""]
# Output: [[""]]
#
# Constraints:
# 1 <= len(strs) <= 10,000
# 0 <= len(strs[i]) <= 100
# strs[i] contains only lowercase English letters.
#
# Recommended complexity:
# Time: O(m * n)
# Space: O(m)
#
# m is the number of strings.
# n is the length of the longest string.
#
# Hint:
# Count the frequency of the 26 lowercase letters in each string.
# Convert this frequency array into a tuple and use it as a
# dictionary key to group strings with identical character counts.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        check = {}
        for word in strs:
            count = [0] * 26
            for s in word:
                index = ord(s) - ord('a')
                count[index] += 1
            key = tuple(count)

            if key not in check:
                check[key] = []

            check[key].append(word)
        
        for key, value in check.items():
            res.append(value)
            
        return res
            

        