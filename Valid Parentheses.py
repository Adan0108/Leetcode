# Valid Parentheses (Stack problem)
#
# Given a string `s` containing only the characters:
# `(`, `)`, `{`, `}`, `[` and `]`,
# determine whether the input string is valid.
#
# A string is valid if:
#
# 1. Every opening bracket is closed by the same type of bracket.
# 2. Opening brackets are closed in the correct order.
# 3. Every closing bracket has a corresponding opening bracket.
#
# Example 1:
#
# Input: s = "[]"
# Output: True
#
# Example 2:
#
# Input: s = "([{}])"
# Output: True
#
# Example 3:
#
# Input: s = "[(])"
# Output: False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # Opening bracket : matching closing bracket
        parentheses = {
            "[": "]",
            "(": ")",
            "{": "}"
        }

        for c in s:

            # If c is an opening bracket, add it to the stack.
            if c in parentheses:
                stack.append(c)

            # Otherwise, c is a closing bracket.
            else:

                # Invalid if there is no opening bracket to match.
                if len(stack) == 0:
                    return False

                # Invalid if c does not match the latest opening bracket.
                if c != parentheses[stack[-1]]:
                    return False

                # Remove the successfully matched opening bracket.
                stack.pop()

        # Valid only when every opening bracket has been matched.
        if len(stack) == 0:
            return True

        return False