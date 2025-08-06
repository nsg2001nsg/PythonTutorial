"""
347. Top K Frequent Elements
Medium
Topics
premium lock icon
Companies
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique
"""
import heapq
from collections import Counter


def topKFrequent(nums, k):  # [2,3,4,5,1]
    buckets = [[] for _ in range(len(nums) + 1)]
    for key, val in Counter(nums).items():
        buckets[val].append(key)
    res = []
    for bucket in buckets[::-1]:
        while bucket and k:
            res.append(bucket.pop())
            k -= 1
    return res


def topKFrequent_heap(nums, k):  # [2,3,4,5,1]
    min_heap = []
    freq_map = Counter(nums)
    for num, freq in freq_map.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (freq, num))
        else:
            heapq.heappush(min_heap, (freq, num))
            heapq.heappop(min_heap)
    return [val[1] for val in min_heap]


# topKFrequent([2, 2, 2, 3, 3, 3, 4, 5, 1], 5)
# topKFrequent([], 5)
# topKFrequent([1], 1)
print(topKFrequent_heap([2, 2, 3, 4, 1, 4, 4, 5], 2))
