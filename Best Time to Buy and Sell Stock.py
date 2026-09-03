# Best Time to Buy and Sell Stock (Sliding Window)
#
# You are given an integer array `prices`, where `prices[i]` is the
# price of NeetCoin on the ith day.
#
# You may choose one day to buy one NeetCoin and choose a different
# day in the future to sell it.
#
# Return the maximum profit you can achieve.
#
# You may choose not to make any transaction, in which case the
# profit is 0.
#
# Example 1:
#
# Input: prices = [10,1,5,6,7,1]
#
# Output: 6
#
# Explanation:
#
# Buy at prices[1] = 1 and sell at prices[4] = 7.
#
# Profit = 7 - 1 = 6
#
# Example 2:
#
# Input: prices = [10,8,7,5,2]
#
# Output: 0
#
# Explanation:
#
# No profitable transaction can be made, so the maximum profit is 0.
#
# Constraints:
#
# 1 <= prices.length <= 100
# 0 <= prices[i] <= 100

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 
        lowest = prices[0]
        for i in range(1,len(prices)):
            if prices[i] > lowest:
                cur = prices[i] - lowest
                res = max(cur, res)
            else:
                lowest = prices[i]
        return res