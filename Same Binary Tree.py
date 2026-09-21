# # Same Binary Tree
#
# **EasyTopics**
#
# Given the roots of two binary trees `p` and `q`,
# return `true` if the trees are **equivalent**,
# otherwise return `false`.
#
# Two binary trees are considered **equivalent**
# if they share the exact same structure
# and the nodes have the same values.
#
# **Example 1:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/e78fc10c-4692-471f-5261-61e9be4f3a00/public)
#
# ```java
# Input: p = [1,2,3], q = [1,2,3]
#
# Output: true
# ```
#
# **Example 2:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/0b0ee764-c643-46ff-cb3f-86ce8b58ab00/public)
#
# ```java
# Input: p = [4,7], q = [4,null,7]
#
# Output: false
# ```
#
# **Example 3:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/4d811f95-0488-490b-1f4f-fc5489df0f00/public)
#
# ```java
# Input: p = [1,2,3], q = [1,3,2]
#
# Output: false
# ```
#
# **Constraints:**
#
# - `0 <= The number of nodes in both trees <= 100`.
# - `-100 <= Node.val <= 100`

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(tree1, tree2):

            # Both are None -> same
            if not tree1 and not tree2:
                return True

            # Only one is None -> different structure
            if not tree1 or not tree2:
                return False

            # Values are different
            if tree1.val != tree2.val:
                return False

            # Both left subtrees AND right subtrees must be the same
            return (
                dfs(tree1.left, tree2.left)
                and
                dfs(tree1.right, tree2.right)
            )

        return dfs(p, q)