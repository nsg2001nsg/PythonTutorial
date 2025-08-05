"""
496. Next Greater Element I
Easy
Topics
premium lock icon
Companies
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.



Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.


Constraints:

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2
"""


def nextGreaterElement(nums1, nums2):
    res = []
    for i in nums1:
        j = 0
        while j < len(nums2) - 1:
            v = nums2[j]
            if v == i:
                while j < len(nums2)-1:
                    if nums2[j+1] > v:
                        res.append(nums2[j+1])
                        break
                    j += 1
                res.append(-1)
                break
            j += 1
    return res


def nextGreaterElement_opt(nums1, nums2):
    next_greater = {}
    stack = []
    for num in nums2:
        while stack and num > stack[-1]:
            smaller = stack.pop()
            next_greater[smaller] = num
        stack.append(num)

    for rest in stack:
        next_greater[rest] = -1

    return [next_greater[v] for v in nums1]


print(nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
print(nextGreaterElement([2,4], [2,1,3,4]))
print(nextGreaterElement_opt([4, 1, 2], [1, 3, 4, 2]))
print(nextGreaterElement_opt([2,4], [2,1,3,4]))
