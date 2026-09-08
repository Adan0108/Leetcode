# Reverse Linked List
#
# Given the beginning of a singly linked list `head`, reverse the list
# and return the new beginning of the list.
#
# Example 1:
#
# Input: head = [0,1,2,3]
#
# Output: [3,2,1,0]
#
# Example 2:
#
# Input: head = []
#
# Output: []
#
# Constraints:
#
# 0 <= The length of the list <= 1,000
# -1,000 <= Node.val <= 1,000

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            # Save the next node before changing current.next.
            next_node = current.next

            # Reverse the direction.
            current.next = previous

            # Move previous forward.
            previous = current

            # Move current forward.
            current = next_node

        # Previous is now the new head.
        return previous