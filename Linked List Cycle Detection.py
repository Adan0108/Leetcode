# # Linked List Cycle Detection
#
# **EasyTopicsCompany TagssvgHints**
#
# Given the beginning of a linked list `head`, return `true`
# if there is a cycle in the linked list. Otherwise, return `false`.
#
# There is a cycle in a linked list if at least one node in the list
# can be visited again by following the `next` pointer.
#
# Internally, `index` determines the index of the beginning of the cycle,
# if it exists. The tail node of the list will set its `next` pointer
# to the `index-th` node.
#
# If `index = -1`, then the tail node points to `null`
# and no cycle exists.
#
# **Note:** `index` is **not** given to you as a parameter.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        rabbit = head

        while rabbit and rabbit.next:
            cur = cur.next
            rabbit = rabbit.next.next

            if cur == rabbit:
                return True

        return False