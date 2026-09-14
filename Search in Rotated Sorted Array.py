# # Search in Rotated Sorted Array (Binary Search)
# (find rotated point)
#
# **MediumTopics
#
# You are given an array of length `n` which was originally sorted
# in ascending order. It has now been **rotated** between `1` and `n` times.
#
# For example, the array `nums = [1,2,3,4,5,6]` might become:
#
# - `[3,4,5,6,1,2]` if it was rotated `4` times.
# - `[1,2,3,4,5,6]` if it was rotated `6` times.
#
# Given the rotated sorted array `nums` and an integer `target`,
# return the index of `target` within `nums`, or `-1` if it is not present.
#
# You may assume all elements in the sorted rotated array `nums`
# are **unique**.
#
# A solution that runs in `O(n)` time is trivial.
# Can you write an algorithm that runs in `O(log n)` time?
#
# **Example 1:**
#
# Input: nums = [3,4,5,6,1,2], target = 1
#
# Output: 4
# ```
#
# **Example 2:**
#
# Input: nums = [3,5,6,0,1,2], target = 4
#
# Output: -1
# ```
#
# **Constraints:**
#
# - `1 <= nums.length <= 1000`
# - `-1000 <= nums[i] <= 1000`
# - `-1000 <= target <= 1000`
# - All values of `nums` are **unique**.
# - `nums` is an ascending array that is possibly rotated.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m

            #check sorted portion to see which side the target on
            #if middle number < left -> we over the rotated point and vice versa

            #left sorted portion[if middle number > smallest number on left]
            #[3,4,5,6,1,2]
            if nums[m] >= nums[l]:
                #if target > nums[m] or targets < smallest number on left
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            #right portion[if middle number <= biggest number on right]   
            else:
                #if target < nums[m] or targets > largest number on right
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
