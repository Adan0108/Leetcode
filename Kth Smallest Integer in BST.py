# # Kth Smallest Integer in BST
#
# **MediumTopics**
#
# Given the `root` of a binary search tree, and an integer `k`,
# return the `kth` smallest value (**1-indexed**) in the tree.
#
# A **binary search tree** satisfies the following constraints:
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
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/02eca3db-f72f-4277-7134-faec4f02e500/public)
#
# ```java
# Input: root = [2,1,3], k = 1
#
# Output: 1
# ```
#
# **Example 2:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/dca6c42d-2327-4036-f7f2-3e99d8203100/public)
#
# ```java
# Input: root = [4,3,5,2,null], k = 4
#
# Output: 5
# ```
#
# **Constraints:**
#
# - `1 <= k <= The number of nodes in the tree <= 10,000`.
# - `0 <= Node.val <= 10,000`

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []

        def dfs(root):
            if not root:
                return

            # Visit left subtree first
            dfs(root.left)

            # Take left first then return to the current node , then get it right as the right is always bigger than root
            # left < node < right
            # Then visit current node
            stack.append(root.val)

            # Then visit right subtree
            dfs(root.right)

        dfs(root)

        # k is 1-based, list index is 0-based
        return stack[k - 1]