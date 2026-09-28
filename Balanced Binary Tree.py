# # Balanced Binary Tree
#
# **EasyTopics**
#
# Given a binary tree, return `true` if it is **height-balanced**
# and `false` otherwise.
#
# A **height-balanced** binary tree is defined as a binary tree
# in which the left and right subtrees of every node differ
# in height by no more than 1.
#
# **Example 1:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/c19c3727-ea28-416c-3873-79ee75f2b400/public)
#
# ```java
# Input: root = [1,2,3,null,null,4]
#
# Output: true
# ```
#
# **Example 2:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/24fcc2da-e012-4f9e-856e-040f200f3c00/public)
#
# ```java
# Input: root = [1,2,3,null,null,4,null,5]
#
# Output: false
# ```
#
# **Example 3:**
#
# ```java
# Input: root = []
#
# Output: true
# ```

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def bottomUp(root):
            # Base case:
            # An empty tree is balanced and has height 0
            #
            # Return format:
            # [isBalanced, height]
            if not root:
                return [True, 0]

            # Check left subtree first
            # left[0] = whether left subtree is balanced
            # left[1] = height of left subtree
            left = bottomUp(root.left)

            # Check right subtree
            # right[0] = whether right subtree is balanced
            # right[1] = height of right subtree
            right = bottomUp(root.right)

            # Current tree is balanced only if:
            # 1. Left subtree is balanced
            # 2. Right subtree is balanced
            # 3. Difference between left and right height <= 1
            balanced = (
                left[0]
                and right[0]
                and abs(left[1] - right[1]) <= 1
            )

            # Return:
            # [whether current subtree is balanced,
            #  height of current subtree]
            #
            # Height = current node (1)
            #        + larger height between left and right subtree
            return [
                balanced,
                1 + max(left[1], right[1])
            ]

        # We only need the balanced result,
        # so return index 0 from [balanced, height]
        return bottomUp(root)[0]


            
            
            
        