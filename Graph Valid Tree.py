# # Graph Valid Tree
#
# **MediumTopics**
#
# Given `n` nodes labeled from `0` to `n - 1`
# and a list of **undirected** edges
# where each edge is a pair of nodes,
# determine whether these edges form a valid tree.
#
# **Example 1:**
#
# [image]
# (https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/cf8b3035-344d-455a-fcbe-cbe9d6121a00/public)
#
# ```java
# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
#
# Output: true
# ```
#
# **Example 2:**
#
# [image]
# (https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/09155553-b851-4439-203e-8a8064ea9000/public)
#
# ```java
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
#
# Output: false
# ```
#
# **Note:**
#
# - You can assume that no duplicate edges will appear.
# - Since all edges are `undirected`,
#   `[0,1]` is the same as `[1,0]`,
#   so both will not appear together.
#
# **Constraints:**
#
# - `1 <= n <= 2000`
# - `0 <= edges.length <= 5000`
# - `edges[i].length == 2`
# - `0 <= a_i, b_i < n`
# - `a_i != b_i`
# - There are no self-loops or repeated edges.

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # Empty graph is considered valid
        if not n:
            return True

        # Build adjacency list for undirected graph
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(i, prev):
            # If we visit the same node again,
            # there is a cycle
            if i in visited:
                return False

            visited.add(i)

            # Visit all neighbors
            for nei in adj[i]:

                # Skip the node we just came from
                # because the graph is undirected
                if nei == prev:
                    continue

                # If a cycle is found in any branch
                if not dfs(nei, i):
                    return False

            return True

        # A valid tree must:
        # 1. Have no cycle
        # 2. Have all nodes connected
        return dfs(0, -1) and n == len(visited)