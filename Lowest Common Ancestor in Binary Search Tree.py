# # Lowest Common Ancestor in Binary Search Tree
#
# **MediumTopics**
#
# Given a binary search tree (BST) where all node values are **unique**,
# and two nodes from the tree `p` and `q`,
# return the lowest common ancestor (LCA) of the two nodes.
#
# The lowest common ancestor between two nodes `p` and `q`
# is the lowest node in a tree `T` such that both `p` and `q`
# are descendants.
#
# The ancestor is allowed to be a descendant of itself.
#
# **Example 1:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/2080ee6a-3d27-4cd5-0db2-07672ead8200/public)
#
# ```java
# Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8
#
# Output: 5
# ```
#
# **Example 2:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/2080ee6a-3d27-4cd5-0db2-07672ead8200/public)
#
# ```java
# Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4
#
# Output: 3
# ```
#
# Explanation:
# The LCA of nodes 3 and 4 is 3,
# since a node can be a descendant of itself.
#
# **Constraints:**
#
# - `2 <= The number of nodes in the tree <= 100`.
# - `-100 <= Node.val <= 100`
# - `p != q`
# - `p` and `q` will both exist in the BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(
        self,
        root: TreeNode,
        p: TreeNode,
        q: TreeNode
    ) -> TreeNode:

        # Start searching from the root
        cur = root

        while cur:

            # If both p and q are greater than current node,
            # then both nodes must be in the right subtree.
            # p = 7, q = 9
            # both > 5
            # => move right
            if q.val > cur.val and p.val > cur.val:
                cur = cur.right

            # If both p and q are smaller than current node,
            # then both nodes must be in the left subtree.
            # p = 1, q = 4
            # both < 5
            # => move left
            elif q.val < cur.val and p.val < cur.val:
                cur = cur.left

            # Otherwise:
            #
            # p and q are on different sides of cur
            # OR cur itself is p or q.
            #
            # That means cur is the lowest node
            # where the paths to p and q split.
            #
            # Therefore cur is the Lowest Common Ancestor.
            else:
                return cur
            
          #if not root or not p or not q:
          #    return None
          #if (max(p.val, q.val) < root.val):
          #    return self.lowestCommonAncestor(root.left, p, q)
          #elif (min(p.val, q.val) > root.val):
          #    return self.lowestCommonAncestor(root.right, p, q)
          #else:
          #    return root