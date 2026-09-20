# # Add Two Numbers (Link List)
#
# **MediumTopics**
#
# You are given two **non-empty** linked lists, `l1` and `l2`,
# where each represents a non-negative integer.
#
# The digits are stored in **reverse order**,
# e.g. the number 321 is represented as:
#
# `1 -> 2 -> 3`
#
# in the linked list.
#
# Each of the nodes contains a single digit.
# You may assume the two numbers do not contain any leading zero,
# except the number `0` itself.
#
# Return the sum of the two numbers as a linked list.
#
# **Example 1:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/fee72e19-6a21-45a5-365e-3cb45aba9700/public)
#
# ```java
# Input: l1 = [1,2,3], l2 = [4,5,6]
#
# Output: [5,7,9]
#
# Explanation: 321 + 654 = 975.
# ```
#
# **Example 2:**
#
# ```java
# Input: l1 = [9], l2 = [9]
#
# Output: [8,1]
# ```
#
# **Constraints:**
#
# - `1 <= l1.length, l2.length <= 100`.
# - `0 <= Node.val <= 9`

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        store = 0
        total = ListNode()
        dummy = total

        # Add while both lists still have nodes
        while l1 and l2:

            val1 = l1.val
            val2 = l2.val
            cur = val1 + val2 + store

            # Calculate carry
            store = cur // 10

            #Calculate actual number append 
            cur = cur % 10

            # Create new node
            dummy.next = ListNode(cur)
            dummy = dummy.next

            l1 = l1.next
            l2 = l2.next
        
        # If l1 still has nodes
        while l1:
            cur = l1.val + store

            store = cur // 10
            cur = cur % 10

            dummy.next = ListNode(cur)
            dummy = dummy.next

            l1 = l1.next

        # If l2 still has nodes
        while l2:
            cur = l2.val + store

            store = cur // 10
            cur = cur % 10

            dummy.next = ListNode(cur)
            dummy = dummy.next

            l2 = l2.next

        # If there is still carry left
        if store:
            dummy.next = ListNode(store)

        return total.next

        