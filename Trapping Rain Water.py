# Trapping Rain Water
#
# You are given an array of non-negative integers `height` which
# represents an elevation map. Each value `height[i]` represents
# the height of a bar, which has a width of 1.
#
# Return the total amount of water that can be trapped between the bars.
#
# Example 1:
#
# Input: height = [0,2,0,3,1,0,1,3,2,1]
#
# Output: 9
#
# Constraints:
#
# 1 <= height.length <= 20,000
# 0 <= height[i] <= 100,000


###
# To solve this think of each case can happen:
# - Think of what make a pool
# - Edge case that can happen so we have to move the pointer
# until meet the condition to stop

class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l , r = 0 , 1

        while r < len(height):
            #case 1: calculate pool when height[r] >= height[l]
            #100% is a pool there if there is a gap
            if height[r] >= height[l]:

                # Calculate the water between l and r.
                cal_l = l + 1

                while cal_l < r:
                    water += height[l] - height[cal_l]
                    cal_l += 1
                # The right bar becomes the new left boundary.
                l = r
                r += 1

            #case 2: if height[r] < height[l]
            #then we loop until we find an equal or higher bar(pool)
            elif height[r] < height[l]:           
                r += 1
                # If we reach the end without finding an equal
                # or higher bar, find the tallest remaining bar.
                if r == len(height):
                    tallest = l + 1
                    check = l + 1
                    
                    #create an another high bar as other r already end
                    #Use tallest to find the end of the pool
                    while check < len(height):
                        if height[check] > height[tallest]:
                            tallest = check

                        check += 1

                    # Calculate water using the tallest remaining
                    # bar as the right boundary.
                    cal_l = l + 1

                    while cal_l < tallest:
                        water += height[tallest] - height[cal_l]
                        cal_l += 1

                    # The tallest bar becomes the new left boundary.
                    l = tallest
                    r = l + 1
        return water
            
            


        