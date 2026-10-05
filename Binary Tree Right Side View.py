# # Binary Tree Right Side View
#
# **MediumTopics**
#
# You are given the `root` of a binary tree.
# Return only the values of the nodes that are visible
# from the right side of the tree,
# ordered from top to bottom.
#
# **Example 1:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/10f2e260-d7a8-4f46-a685-a7de5afd6d00/public)
#
# ```java
# Input: root = [1,2,3,null,4,null,5]
#
# Output: [1,3,5]
# ```
#
# **Example 2:**
#
# [image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/df99b5b2-a3b4-44a0-227d-5bb9ca6fd600/public)
#
# ```java
# Input: root = [1,2,3,4,null,null,null,5]
#
# Output: [1,3,4,5]
# ```
#
# **Example 3:**
#
# ```java
# Input: root = [1,null,2]
#
# Output: [1,2]
# ```
#
# **Example 4:**
#
# ```java
# Input: root = []
#
# Output: []
# ```
#
# **Constraints:**
#
# - `0 <= number of nodes in the tree <= 100`
# - `-100 <= Node.val <= 100`

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        q = deque([root])

        while q:
            qLen = len(q)
            rightNode = None

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightNode = node
                    q.append(node.left)
                    q.append(node.right)

            if rightNode:
                res.append(rightNode.val)
        
        return res
        

        