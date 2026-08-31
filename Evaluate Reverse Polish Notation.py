# Evaluate Reverse Polish Notation (Stack Problem)
#
# You are given an array of strings `tokens` that represents a valid
# arithmetic expression in Reverse Polish Notation.
#
# Return the integer that represents the result of the expression.
#
# The operands may be integers or the results of other operations.
#
# The operators include:
#
# "+"
# "-"
# "*"
# "/"
#
# Division between integers always truncates toward zero.
#
# Example 1:
#
# Input: tokens = ["1","2","+","3","*","4","-"]
#
# Output: 5
#
# Explanation:
#
# ((1 + 2) * 3) - 4 = 5
#
# Constraints:
#
# 1 <= tokens.length <= 10,000
#
# tokens[i] is "+", "-", "*", or "/",
# or a string representing an integer between -200 and 200.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                b = stack.pop()
                a = stack.pop()
                num = a + b
            elif c == "-":
                b = stack.pop()
                a = stack.pop()
                num = a - b
            elif c == "*":
                b = stack.pop()
                a = stack.pop()
                num = a * b
            elif c == "/":
                b = stack.pop()
                a = stack.pop()
                num = a / b
            else:
                num = c
            stack.append(int(num))
        num = stack.pop()
        return num
            
