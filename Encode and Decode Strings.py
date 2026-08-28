# Encode and Decode Strings (ARRAY PROBLEM)
#
# Design an algorithm to encode a list of strings into a single
# string. The encoded string is sent over a network and decoded
# back into the original list of strings.
#
# Machine 1 (sender) uses encode():
#
# def encode(strs: list[str]) -> str:
#     return encoded_string
#
# Machine 2 (receiver) uses decode():
#
# def decode(encoded_string: str) -> list[str]:
#     return decoded_strs
#
# The decoded list on Machine 2 must be identical to the original
# list given to Machine 1.
#
# Implement the encode() and decode() methods.
#
# Example 1:
# Input: strs = ["Hello", "World"]
# Output after encoding and decoding: ["Hello", "World"]
#
# Example 2:
# Input: strs = [""]
# Output after encoding and decoding: [""]
#
# Constraints:
# 0 <= len(strs) < 100
# 0 <= len(strs[i]) < 200
# strs[i] may contain any of the 256 valid ASCII characters.
#
# Follow-up:
# Create a generalized algorithm that works with any possible
# set of characters.
# 
# Recommended complexity:
# Time: O(m) for both encode() and decode()
# Space: O(m + n)
#
# m is the total length of all strings.
# n is the number of strings.
class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            number = len(word)
            res += str(number) + "#" + word
        return res


    def decode(self, s: str) -> List[str]:
        num = {"1","2","3","4","5","6","7","8","9","0"}
        res = []
        count = ""
        i = 0

        while i < len(s):
            if s[i] in num:
                count += s[i]

            elif s[i] == "#":
                count = int(count)
                word = ""
                j = i + 1

                while j < i + 1 + count:
                    word += s[j]
                    j += 1

                res.append(word)

                i = j - 1
                count = ""

            i += 1

        return res