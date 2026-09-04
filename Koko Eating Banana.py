# Koko Eating Bananas (Binary Search)
#
# You are given an integer array `piles`, where `piles[i]` is the
# number of bananas in the ith pile.
#
# You are also given an integer `h`, which represents the number
# of hours available to eat all the bananas.
#
# You may choose a bananas-per-hour eating rate of `k`.
#
# During each hour, you may choose one pile and eat `k` bananas
# from that pile.
#
# If the pile has fewer than `k` bananas, you can finish that pile,
# but you cannot eat from another pile during the same hour.
#
# Return the minimum integer `k` that allows you to eat all the
# bananas within `h` hours.
#
# Example 1:
#
# Input: piles = [1,4,3,2], h = 9
#
# Output: 2
#
# Explanation:
#
# With an eating rate of 2, all bananas can be eaten in 6 hours.
#
# With an eating rate of 1, eating all bananas would require 10 hours,
# which exceeds h = 9.
#
# Therefore, the minimum eating rate is 2.
#
# Example 2:
#
# Input: piles = [25,10,23,4], h = 4
#
# Output: 25
#
# Constraints:
#
# 1 <= piles.length <= 10,000
# piles.length <= h <= 1,000,000,000
# 1 <= piles[i] <= 1,000,000,000

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1 , max(piles)
        res = r
        #instead of doing brute force starting from 1
        #we can do the binary search to // 2 the time finding it
        #and we can use the ceil() to round up the float number

        while l <= r:
            k = l + (r - l) // 2

            eatTime = 0
            for pile in piles:
                eatTime += math.ceil(float(pile) / k)

            if eatTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res