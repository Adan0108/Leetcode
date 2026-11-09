# # Course Schedule (can add backtracking)
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
# Return `true` if it is possible
# to finish all courses.
#
# Otherwise, return `false`.
#
# **Example 1:**
#
# ```java
# Input: numCourses = 2, prerequisites = [[0,1]]
#
# Output: true
# ```
#
# Explanation:
#
# First take course `1`,
# which has no prerequisites,
# then take course `0`.
#
# **Example 2:**
#
# ```java
# Input: numCourses = 2,
# prerequisites = [[0,1],[1,0]]
#
# Output: false
# ```
#
# Explanation:
#
# To take course `1`,
# you must first take course `0`.
#
# But to take course `0`,
# you must first take course `1`.
#
# This creates a cycle,
# so it is impossible to finish all courses.
#
# **Constraints:**
#
# - `1 <= numCourses <= 1000`
# - `0 <= prerequisites.length <= 1000`
# - `prerequisites[i].length == 2`
# - `0 <= a[i], b[i] < numCourses`
# - All prerequisite pairs are **unique**.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # course -> prerequisites needed
        adj = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            adj[course].append(pre)

        # Courses currently in the DFS path
        visit = set()

        def dfs(course):
            # Found the same course in current path -> cycle
            if course in visit:
                return False

            # No prerequisite left to check
            if adj[course] == []:
                return True

            visit.add(course)

            # Check all prerequisites
            for pre in adj[course]:
                if not dfs(pre):
                    return False

            # Backtrack
            visit.remove(course)

            # Mark this course as already checked and safe
            adj[course] = []

            return True

        # Every course must be possible to finish
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True