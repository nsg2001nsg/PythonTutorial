"""
215. Kth Largest Element in an Array
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""

import heapq


def findKthLargest(nums, k):
    nums = sorted(nums, reverse=True)  # sorting is O(n log n) - NOT OPTIMAL to sort the whole array when we only need 1
    return nums[k - 1] if nums else None


class Solution:

    def findKthLargest_opt(self, nums, k):
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappush(min_heap, num)  # or heapq.heappushpop()
                heapq.heappop(min_heap)
        return min_heap[0] if k <= len(nums) else None


print(findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
print(findKthLargest([], 1))  # 4
print(findKthLargest([], 2))  # 4
sol = Solution()
print(sol.findKthLargest_opt([3, 2, 1, 5, 6, 4], 2))  # 5
print(sol.findKthLargest_opt([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
print(sol.findKthLargest_opt([4, 4, 4, 4, 5], 4), "bugger")  # 4
print(sol.findKthLargest_opt([], 1))  # 4
print(sol.findKthLargest_opt([], 2))  # 4
