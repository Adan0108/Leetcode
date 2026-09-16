# # Reorder Linked List
# (Find middle then reverse) (then start connect node)
# **Medium Topics**
#
# You are given the head of a singly linked-list.
#
# The positions of a linked list of `length = 7` for example,
# can initially be represented as:
#
# `[0, 1, 2, 3, 4, 5, 6]`
#
# Reorder the nodes of the linked list to be in the following order:
#
# `[0, 6, 1, 5, 2, 4, 3]`
#
# In the general case, label the nodes by their original zero-based positions
# from `0` to `n - 1`.
#
# After reordering, those original positions appear in this order:
#
# `[0, n-1, 1, n-2, 2, n-3, ...]`
#
# These numbers represent node positions, not the values stored in the nodes.
#
# You may not modify the values in the list's nodes,
# but instead you must reorder the nodes themselves.
#
# **Example 1:**
#
# ```java
# Input: head = [2,4,6,8]
#
# Output: [2,8,4,6]
# ```
#
# **Example 2:**
#
# ```java
# Input: head = [2,4,6,8,10]
#
# Output: [2,10,4,8,6]
# ```
#
# **Constraints:**
#
# - `1 <= Length of the list <= 1000`.
# - `1 <= Node.val <= 1000`

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # 1. Find the middle of the linked list
        #
        # slow moves 1 step
        # fast moves 2 steps
        #
        # Example:
        # 1 -> 2 -> 3 -> 4 -> 5
        #      slow will stop around middle
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # 2. Split the list into two halves
        #
        # First half:
        # 1 -> 2 -> 3
        #
        # Second half:
        # 4 -> 5
        second = slow.next

        # Cut the connection between the two halves
        slow.next = None


        # 3. Reverse the second half
        #
        # Before:
        # 4 -> 5
        #
        # After:
        # 5 -> 4
        prev = None

        while second:
            tmp = second.next

            second.next = prev

            prev = second
            second = tmp


        # 4. Merge the two halves alternately
        #
        # First:
        # 1 -> 2 -> 3
        #
        # Second:
        # 5 -> 4
        #
        # Result:
        # 1 -> 5 -> 2 -> 4 -> 3
        first = head
        second = prev

        while second:
            # Save the next nodes before changing pointers
            tmp1 = first.next
            tmp2 = second.next

            # Connect first node -> second node
            first.next = second

            # Connect second node -> next first node
            second.next = tmp1

            # Move both pointers forward
            first = tmp1
            second = tmp2