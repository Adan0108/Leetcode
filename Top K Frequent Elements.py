# Top K Frequent Elements (HASHMAP PROBLEM) (BUCKETSORT PROBLEM)
#
# Given an integer array nums and an integer k, return the k most
# frequent elements in the array.
#
# The test cases guarantee that the answer is always unique.
# The output can be returned in any order.
#
# Example 1:
# Input: nums = [1, 2, 2, 3, 3, 3], k = 2
# Output: [2, 3]
#
# Example 2:
# Input: nums = [7, 7], k = 1
# Output: [7]
#
# Constraints:
# 1 <= len(nums) <= 10^4
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums
#
# Recommended complexity:
# Time: O(n)
# Space: O(n)
#
# n is the size of the input array.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        arr = []

        for key, value in count.items():
            arr.append([value,key])

        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        