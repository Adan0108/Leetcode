# # Number of Connected Components in an Undirected Graph
#
# **MediumTopics**
#
# You have an undirected graph of `n` nodes
# labeled from `0` to `n - 1`.
#
# You are given an integer `n`
# and an array `edges`.
#
# `edges[i] = [aᵢ, bᵢ]` means there is an edge
# between node `aᵢ` and node `bᵢ`.
#
# Return the number of connected components
# in the graph.
#
# **Example 1:**
#
# [image]
# (https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/d99cd414-340e-4c6f-083b-1f00fdf9eb00/public)
#
# ```java
# Input:
# n = 5, edges = [[0,1],[1,2],[3,4]]
#
# Output: 2
# ```
#
# **Example 2:**
#
# [image]
# (https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/3f57f075-5114-473a-b198-b6da0da1cd00/public)
#
# ```java
# Input:
# n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
#
# Output: 1
# ```
#
# **Constraints:**
#
# - `1 <= n <= 2000`
# - `1 <= edges.length <= 5000`
# - `edges[i].length == 2`
# - `0 <= aᵢ < n`
# - `0 <= bᵢ < n`
# - `aᵢ != bᵢ`
# - There are no repeated edges.

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i: [] for i in range(n)}
        visited = set()
        count = 0

        # Build undirected graph
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(i):
            # Already part of a component we visited
            if i in visited:
                return False

            visited.add(i)

            # Visit the whole connected component
            for nei in adj[i]:
                dfs(nei)

            return True

        # Try starting DFS from every node
        for i in range(n):
            # True means this is a new component
            if dfs(i):
                count += 1

        return count