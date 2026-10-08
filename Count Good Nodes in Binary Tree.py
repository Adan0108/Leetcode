# # Count Good Nodes in Binary Tree
#
# **MediumTopics**
#
# Within a binary tree, a node `x` is considered **good**
# if the path from the root of the tree to the node `x`
# contains no nodes with a value greater than the value of node `x`.
#
# Given the root of a binary tree `root`,
# return the number of **good** nodes within the tree.
#
# **Example 1:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/9bf374f1-71fe-469e-2840-5d223d9d1b00/public)
#
# ```java
# Input: root = [2,1,1,3,null,1,5]
#
# Output: 3
# ```
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/8df65da7-abac-4948-9a92-0bc7a8dda100/public)
#
# **Example 2:**
#
# ```java
# Input: root = [1,2,-1,3,4]
#
# Output: 4
# ```
#
# **Constraints:**
#
# - `1 <= number of nodes in the tree <= 100,000`
# - `-100 <= Node.val <= 100`

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxNode):
            # If there is no node, this path contributes 0 good nodes
            if not node:
                return 0

            # A node is "good" if its value is greater than
            # or equal to every value seen on the path from root to this node.
            #
            # maxNode stores the maximum value seen so far on this path.
            if node.val >= maxNode:
                res = 1
            else:
                res = 0

            # Update the maximum value for the path
            # before moving down to the children.
            maxNode = max(node.val, maxNode)

            # Count good nodes in the left subtree
            res += dfs(node.left, maxNode)

            # Count good nodes in the right subtree
            res += dfs(node.right, maxNode)

            # Return total good nodes in this subtree
            return res

        # Start from the root.
        # The root is always a good node because there are no nodes
        # before it on the path.
        return dfs(root, root.val)