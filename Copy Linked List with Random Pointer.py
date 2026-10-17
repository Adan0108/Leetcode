# # Copy Linked List with Random Pointer
#
# **MediumTopics**
#
# You are given the head of a linked list of length `n`.
#
# Unlike a singly linked list, each node contains an additional
# pointer `random`, which may point to any node in the list,
# or `null`.
#
# Create a **deep copy** of the list.
#
# The deep copy should consist of exactly `n` **new** nodes,
# each including:
#
# - The original value `val` of the copied node
# - A `next` pointer to the new node corresponding to the `next`
#   pointer of the original node
# - A `random` pointer to the new node corresponding to the `random`
#   pointer of the original node
#
# **Note:**
# None of the pointers in the new list should point to nodes
# in the original list.
#
# Return the head of the copied linked list.
#
# In the examples, the linked list is represented as a list
# of `n` nodes.
#
# Each node is represented as a pair:
#
# `[val, random_index]`
#
# where `random_index` is the index of the node (0-indexed)
# that the `random` pointer points to,
# or `null` if it does not point to any node.
#
# **Example 1:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/5a5c2bdd-51e2-4795-4544-096af4b6cc00/public)
#
# ```java
# Input: head = [[3,null],[7,3],[4,0],[5,1]]
#
# Output: [[3,null],[7,3],[4,0],[5,1]]
# ```
#
# **Example 2:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/6e56fa98-cf1e-4ca6-18d4-716dac4ba900/public)
#
# ```java
# Input: head = [[1,null],[2,2],[3,2]]
#
# Output: [[1,null],[2,2],[3,2]]
# ```
#
# **Constraints:**
#
# - `0 <= n <= 100`
# - `-100 <= Node.val <= 100`
# - Node values are not guaranteed to be unique.
# - `random` is `null` or is pointing to some node in the linked list.

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # Map old node -> copied node
        # Also map None -> None so next/random can safely point to None
        oldToCopy = {None: None}

        cur = head

        # First pass:
        # Create a copy of every node
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head

        # Second pass:
        # Connect next and random pointers using the map
        while cur:
            copyNode = oldToCopy[cur]

            copyNode.next = oldToCopy[cur.next]
            copyNode.random = oldToCopy[cur.random]

            cur = cur.next

        # Return the copied head
        return oldToCopy[head]