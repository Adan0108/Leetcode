# Daily Temperatures (STACK PROBLEM)
#
# You are given an array of integers `temperatures`, where
# `temperatures[i]` represents the temperature on the ith day.
#
# Return an array `result`, where `result[i]` is the number of days
# after the ith day before a warmer temperature appears.
#
# If there is no warmer future day, set `result[i]` to 0.
#
# Example 1:
#
# Input: temperatures = [30,38,30,36,35,40,28]
#
# Output: [1,4,1,2,1,0,0]
#
# Example 2:
#
# Input: temperatures = [22,21,20]
#
# Output: [0,0,0]
#
# Constraints:
#
# 1 <= temperatures.length <= 100,000
# 1 <= temperatures[i] <= 100

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for index in range(len(temperatures)):
            value = temperatures[index]

            #Only do the loop when there are index inside stack
            while len(stack):
                #Check current value if it greater than the stack
                if stack[-1][0] < value:
                    #If yes pop it out to calculate the diffrent
                    top_value, top_index = stack.pop()
                    diff = index - top_index
                    res[top_index] = diff
                    #assign the differrent from the higher temp day to that index
                else:
                    break
            stack.append((value,index))

        return res