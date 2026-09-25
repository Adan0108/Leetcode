# # Diameter of Binary Tree
#
# **EasyTopics**
#
# The **diameter** of a binary tree is defined as the **length**
# of the longest path between any two nodes within the tree.
#
# The path does not necessarily have to pass through the root.
#
# The **length** of a path between two nodes in a binary tree
# is the number of edges between the nodes.
#
# Note that the path can not include the same node twice.
#
# Given the root of a binary tree `root`,
# return the **diameter** of the tree.
#
# **Example 1:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/90e1d7a0-4322-4c5d-c59b-dde2bf92bb00/public)
#
# ```java
# Input: root = [1,null,2,3,4,5]
#
# Output: 3
# ```
#
# Explanation:
# 3 is the length of the path `[1,2,3,5]`
# or `[5,3,2,4]`.
#
# **Example 2:**
#
# ```java
# Input: root = [1,2,3]
#
# Output: 2
# ```
#
# **Constraints:**
#
# - `1 <= number of nodes in the tree <= 100`
# - `-100 <= Node.val <= 100`

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            
            # Get the height of left and right subtree
            left = dfs(root.left)
            right = dfs(root.right)

            # Diameter passing through current node
            # = left subtree height + right subtree height
            res = max(res, left + right)
            
            # Return the height of current subtree to parent
            # so the parent can calculate its own diameter
            return 1 + max(left, right)
        
        dfs(root)

        return res