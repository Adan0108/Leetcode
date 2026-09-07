# Longest Repeating Character Replacement (Sliding Window)
#
# You are given a string `s` containing only uppercase English
# characters and an integer `k`.
#
# You can choose up to `k` characters from the string and replace
# them with any other uppercase English character.
#
# After performing at most `k` replacements, return the length of
# the longest substring that contains only one distinct character.
#
# Example 1:
#
# Input: s = "XYYX", k = 2
#
# Output: 4
#
# Explanation:
#
# Replace both "X" characters with "Y", or replace both "Y"
# characters with "X".
#
# Example 2:
#
# Input: s = "AAABABB", k = 1
#
# Output: 5
#
# Constraints:
#
# 1 <= s.length <= 100,000
# 0 <= k <= s.length
# `s` contains only uppercase English characters.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = 0

        l = 0

        for r in range(len(s)):
            count[s[r]] += 1

            # Number of replacements needed:
            # window length - frequency of the most common character
            while (r - l + 1) - max(count.values()) > k:

                # Remove the left character from the window.
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        # Time: O(26n), because there are only 26 uppercase characters.
        # Space: O(26)
        return res


# Dry run:
#
# s = "BBAABA", k = 2
#
# r = 0:
# Window = "B"
# Length = 1, highest frequency = 1
# Replacements needed = 1 - 1 = 0 <= 2
#
# r = 1:
# Window = "BB"
# Length = 2, highest frequency = B = 2
# Replacements needed = 2 - 2 = 0 <= 2
#
# r = 2:
# Window = "BBA"
# Length = 3, highest frequency = B = 2
# Replacements needed = 3 - 2 = 1 <= 2
#
# r = 3:
# Window = "BBAA"
# Length = 4, highest frequency = 2
# Replacements needed = 4 - 2 = 2 <= 2
#
# r = 4:
# Window = "BBAAB"
# Length = 5, highest frequency = B = 3
# Replacements needed = 5 - 3 = 2 <= 2
#
# r = 5:
# Window = "BBAABA"
# Length = 6, highest frequency = 3
# Replacements needed = 6 - 3 = 3 > 2
#
# Move l forward and remove the first "B".
#
# New window = "BAABA"
# Length = 5, highest frequency = A = 3
# Replacements needed = 5 - 3 = 2 <= 2
#
# Final result = 5