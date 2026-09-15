# # Car Fleet
# (Think of overlapping) (Also sorting)
# **MediumTopics**
#
# There are `n` cars traveling to the same destination on a one-lane highway.
#
# You are given two arrays of integers `position` and `speed`,
# both of length `n`.
#
# - `position[i]` is the position of the `ith car` (in miles)
# - `speed[i]` is the speed of the `ith` car (in miles per hour)
#
# The **destination** is at position `target` miles.
#
# A car can **not** pass another car ahead of it.
# It can only catch up to another car and then drive at the same speed
# as the car ahead of it.
#
# A **car fleet** is a non-empty set of cars driving at the same position
# and same speed. A single car is also considered a car fleet.
#
# If a car catches up to a car fleet the moment the fleet reaches
# the destination, then the car is considered to be part of the fleet.
#
# Return the number of **different car fleets** that will arrive
# at the destination.
#
# **Example 1:**
#
# ```java
# Input: target = 10, position = [1,4], speed = [3,2]
#
# Output: 1
# ```
#
# Explanation:
# The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet,
# meeting each other at 10, the destination.
#
# **Example 2:**
#
# ```java
# Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
#
# Output: 3
# ```
#
# Explanation:
# The cars starting at 4 and 7 become a fleet at position 10.
# The cars starting at 1 and 0 never catch up to the car ahead of them.
# Thus, there are 3 car fleets that will arrive at the destination.
#
# **Constraints:**
#
# - `n == position.length == speed.length`.
# - `1 <= n <= 100,000`
# - `0 < target <= 1,000,000`
# - `1 <= speed[i] <= 1,000,000`
# - `0 <= position[i] < target`
# - All the values of `position` are **unique**.

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i],speed[i]) for i in range(len(position))]

        curFleetime = 0
        fleet = 0

        #We can calculate the overlap time when car reach destination
        #If car behind too slow it can never catch up to the other car
        #We can do in reverse to calculate from the car nearest from the dest
        for dist, speed in sorted(pairs, reverse = True):
            destinationTime = (target - dist)/speed

            #If destinationTime of this car > curFleetime
            #Then it can never catch up to the front car
            if  destinationTime > curFleetime:
                fleet += 1

                #Because it slower then car behind it will have 
                #the same speed with it
                curFleetime = destinationTime

        return fleet
