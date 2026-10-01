# # Binary Tree Level Order Traversal
#
# **MediumTopics**
#
# Given a binary tree `root`, return the level order traversal of it
# as a nested list, where each sublist contains the values of nodes
# at a particular level in the tree, from left to right.
#
# **Example 1:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/a4639809-0754-4eda-221f-a4cd58bd9c00/public)
#
# ```java
# Input: root = [1,2,3,4,5,6,7]
#
# Output: [[1],[2,3],[4,5,6,7]]
# ```
#
# **Example 2:**
#
# ```java
# Input: root = [1]
#
# Output: [[1]]
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
# - `0 <= The number of nodes in the tree <= 2000`.
# - `-1000 <= Node.val <= 1000`

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#BFS
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []

        q = deque()
        q.append(root)

        while q:
            #calculate number of node at that level
            length = len(q)
            level = []

            #loop through the current level to take their value
            for i in range(length):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    #append their children for next level
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res
        