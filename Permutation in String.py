# # Permutation in String (slidng window + hashmap)
#
# svg
#
# **MediumTopicsCompany TagssvgHints**
#
# You are given two strings `s1` and `s2`.
#
# Return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.
# That means if a permutation of `s1` exists as a substring of `s2`,
# then return `true`.
#
# Both strings only contain lowercase letters.
#
# **Example 1:**
#
# ```java
# Input: s1 = "abc", s2 = "lecabee"
#
# Output: true
# ```
#
# Explanation:
# The substring `"cab"` is a permutation of `"abc"`
# and is present in `"lecabee"`.
#
# **Example 2:**
#
# ```java
# Input: s1 = "abc", s2 = "lecaabee"
#
# Output: false
# ```
#
# **Constraints:**
#
# - `1 <= s1.length, s2.length <= 10000`
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check = defaultdict(int)

        for c in s1:
            check[c] += 1

        # Keep original requirement because a character may disappear
        # from check after its count becomes 0
        need = dict(check)

        l = 0

        for r in range(len(s2)):
            c = s2[r]

            # Character is not part of s1 at all
            if c not in need:
                check = defaultdict(int, need)
                l = r + 1
                continue

            # c belongs to s1, but we already used enough of it
            # Move left until one c is returned back into check
            while c not in check:
                left_char = s2[l]

                if left_char in need:
                    check[left_char] += 1

                l += 1

            # Use current character
            check[c] -= 1

            if check[c] == 0:
                del check[c]

            # Nothing left to find = full permutation
            if len(check) == 0:
                return True

        return False
        