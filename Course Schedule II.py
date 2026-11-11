# # Course Schedule II (topological sort)
#
# **MediumTopics**
#
# You are given an array `prerequisites`
# where `prerequisites[i] = [a, b]`
# means you must take course `b`
# before taking course `a`.
#
# For example:
#
# `[0, 1]`
#
# means you must take course `1`
# before taking course `0`.
#
# There are `numCourses` total courses,
# labeled from `0` to `numCourses - 1`.
#
# Return a valid ordering of courses
# that allows you to finish all courses.
#
# If there are multiple valid orderings,
# return **any** of them.
#
# If it is impossible to finish all courses,
# return an **empty array**.
#
# **Example 1:**
#
# ```java
# Input: numCourses = 3,
# prerequisites = [[1,0]]
#
# Output: [0,1,2]
# ```
#
# Explanation:
#
# Course `0` must be taken before course `1`.
#
# Course `2` has no prerequisites,
# so it can appear anywhere in the valid order.
#
# **Example 2:**
#
# ```java
# Input: numCourses = 3,
# prerequisites = [[0,1],[1,2],[2,0]]
#
# Output: []
# ```
#
# Explanation:
#
# The prerequisites create a cycle:
#
# 0 -> 1 -> 2 -> 0
#
# So it is impossible to finish all courses.
#
# **Constraints:**
#
# - `1 <= numCourses <= 1000`
# - `0 <= prerequisites.length <= 1000`
# - All prerequisite pairs are **unique**.

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # course -> list of prerequisites
        preMap = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)

        res = []

        # Courses that are completely checked
        visited = set()

        # Courses currently in the DFS path
        # Used to detect a cycle
        cycle = set()

        def dfs(course):
            # If course is already in current DFS path,
            # we found a cycle
            if course in cycle:
                return False

            # Already checked and safe
            if course in visited:
                return True

            # Add course to current DFS path
            cycle.add(course)

            # Finish all prerequisites first
            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            # Backtrack from current DFS path
            cycle.remove(course)

            # Mark course as completely checked
            visited.add(course)

            # Add course after all its prerequisites
            res.append(course)

            return True

        # Check every course because graph may be disconnected
        for c in range(numCourses):
            if not dfs(c):
                return []

        return res