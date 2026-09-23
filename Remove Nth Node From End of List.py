# # Remove Nth Node From End of List
# (use 1 pointer to find the length) (then use another pointer to remove the node)

# **MediumTopics**
#
# Given the `head` of a linked list and an integer `n`,
# remove the `nth` node from the end of the list
# and return its head.
#
# **Example 1:**
#
# ```java
# Input: head = [1,2,3,4], n = 2
#
# Output: [1,2,4]
# ```
#
# **Example 2:**
#
# ```java
# Input: head = [5], n = 1
#
# Output: []
# ```
#
# **Example 3:**
#
# ```java
# Input: head = [1,2], n = 2
#
# Output: [2]
# ```
#
# **Constraints:**
#
# - The number of nodes in the list is `sz`.
# - `1 <= sz <= 30`
# - `0 <= Node.val <= 100`
# - `1 <= n <= sz`

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        cur = head
        fast = head
        length = 0

        # Find total length
        while fast:
            length += 1
            fast = fast.next

        # If removing the first node
        if n == length:
            return head.next

        # Index of node to remove, counting from 0
        remove_index = length - n

        # Move cur to the node BEFORE the node we want to remove
        cur_dis = 0

        while cur_dis < remove_index - 1:
            cur = cur.next
            cur_dis += 1

        # Remove the node
        cur.next = cur.next.next

        return head
        