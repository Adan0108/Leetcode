# # Valid Binary Search Tree
#
# **MediumTopics**
#
# Given the `root` of a binary tree,
# return `true` if it is a **valid binary search tree**,
# otherwise return `false`.
#
# A **valid binary search tree** satisfies the following constraints:
#
# - The left subtree of every node contains only nodes
#   with keys **less than** the node's key.
#
# - The right subtree of every node contains only nodes
#   with keys **greater than** the node's key.
#
# - Both the left and right subtrees are also binary search trees.
#
# **Example 1:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/18f9a316-8dc2-4e11-d304-51204454ac00/public)
#
# ```java
# Input: root = [2,1,3]
#
# Output: true
# ```
#
# **Example 2:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/6f14cb8d-efad-4221-2beb-fba2b19c8a00/public)
#
# ```java
# Input: root = [1,2,3]
#
# Output: false
# ```
#
# Explanation:
# The root node's value is 1,
# but its left child's value is 2,
# which is greater than 1.
#
# **Constraints:**
#
# - `1 <= The number of nodes in the tree <= 10000`.
# - `-1000000000 <= Node.val <= 1000000000`

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, low, high):
            # Empty subtree is valid
            if not root:
                return True

            # Current node must stay inside the allowed range:
            #
            # low < root.val < high
            #
            # Example:
            # if a node is in the right subtree of 5,
            # its value must be > 5
            #
            # if it is also in the left subtree of 10,
            # its value must also be < 10
            if not (low < root.val < high):
                return False

            # For the left subtree:
            # every value must still be > low,
            # but now must be < root.val
            #
            # So its valid range becomes:
            # (low, root.val)
            #
            # For the right subtree:
            # every value must be > root.val,
            # while still being < high
            #
            # So its valid range becomes:
            # (root.val, high)
            return (
                dfs(root.left, low, root.val)
                and
                dfs(root.right, root.val, high)
            )

        # Root initially has no restriction,
        # so its valid range is:
        # (-infinity, +infinity)
        return dfs(root, float("-inf"), float("inf"))