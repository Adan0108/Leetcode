# # Invert Binary Tree
#
# **EasyTopics**
#
# You are given the root of a binary tree `root`.
# Invert the binary tree and return its root.
#
# **Example 1:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/ac124ee6-207f-41f6-3aaa-dfb35815f200/public)
#
# ```java
# Input: root = [1,2,3,4,5,6,7]
#
# Output: [1,3,2,7,6,5,4]
# ```
#
# **Example 2:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/e39e8d4f-9946-4f99-ee3d-0d4df08d4d00/public)
#
# ```java
# Input: root = [3,2,1]
#
# Output: [3,1,2]
# ```
#
# **Example 3:**
#
# ```java
# Input: root = []
#
# Output: []
# ```
#
# **Constraints:**
#
# - `0 <= The number of nodes in the tree <= 100`.
# - `-100 <= Node.val <= 100`

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        def recur(root):
            if not root:
                return None

            # Swap left and right children
            tmp = root.left
            root.left = root.right
            root.right = tmp

            # Invert both subtrees
            recur(root.left)
            recur(root.right)

            return root

        return recur(root)