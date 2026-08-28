#Container With Most Water (2 Pointer Problem)

#You are given an integer array heights where heights[i] represents the height of the ith bar.
#You may choose any two bars to form a container. Return the maximum amount of water a container can store.
#Example 1:
#Input: height = [1,7,2,5,4,7,3,6]
#Output: 36
#Explanation: The bars at indices 1 and 7 have heights 7 and 6.
#The container has width 7 - 1 = 6 and height min(7, 6) = 6,
#so it can store 6 * 6 = 36 units of water.
#This is the maximum possible area.
#Example 2:
#Input: height = [2,2,2]
#Output: 4
#Constraints:
#2 <= height.length <= 100,000
#0 <= height[i] <= 10,000

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0 , len(heights) - 1
        largest = 0
        # in this problem 
        #height = min(l , r) if the other less then move that
        #width = distance of index far distance better total (in case both equal just move 1)
        #cur = height * width (take the max)
        
        while l < r:
            less = min(heights[l],heights[r])
            cur = less * (r - l)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] < heights[r]:
                r -= 1
            else:
                r -= 1
            largest = max(cur, largest)
        return largest
        