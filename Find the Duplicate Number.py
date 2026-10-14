# # Find the Duplicate Number (LInk List fast and slow pointer)
#
# **MediumTopics**
#
# You are given an array of integers `nums` containing `n + 1` integers.
# Each integer in `nums` is in the range `[1, n]` inclusive.
#
# There is exactly **one repeated integer** in `nums`,
# and every other integer appears at most once.
#
# Return the repeated integer.
#
# **Example 1:**
#
# ```java
# Input: nums = [1,2,3,2,2]
#
# Output: 2
# ```
#
# **Example 2:**
#
# ```java
# Input: nums = [1,2,3,4,4]
#
# Output: 4
# ```
#
# Follow-up:
# Can you solve the problem **without** modifying the array `nums`
# and using `O(1)` extra space?
#
# **Constraints:**
#
# - `1 <= n <= 10,000`
# - `nums.length == n + 1`
# - `1 <= nums[i] <= n`

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Treat nums like a linked list:
        # index = node, nums[index] = next node
        # duplicate = cycle entrance

        slow = fast = 0

        # Phase 1: find a meeting point inside the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2: find cycle entrance
        # P = start -> entrance, C = cycle length
        # X = meeting point -> entrance
        #
        # 2(P + C - X) = P + 2C - X
        # => P = X
        #
        # Therefore both pointers moving 1 step
        # will meet at the cycle entrance (duplicate).
        slow2 = 0

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow