# # Maximum Depth of Binary Tree
#
# **EasyTopics**
#
# Given the `root` of a binary tree, return its **depth**.
#
# The **depth** of a binary tree is defined as the number of nodes
# along the longest path from the root node down to the farthest leaf node.
#
# **Example 1:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/5ea6da77-7e43-43e0-dd9d-e879ca0b1600/public)
#
# ```java
# Input: root = [1,2,3,null,null,4]
#
# Output: 3
# ```
#
# **Example 2:**
#
# ```java
# Input: root = []
#
# Output: 0
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(root, cur_depth):
            if not root:
                return cur_depth

            cur_depth += 1
            left_depth = dfs(root.left,cur_depth)
            right_depth = dfs(root.right,cur_depth)
            return max(left_depth,right_depth)
        return dfs(root, 0)
        