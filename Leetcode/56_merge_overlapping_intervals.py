"""
56. Merge Intervals
Medium
Topics
premium lock icon
Companies
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""


def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])
    return merged


# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]  # Output: [[1,6],[8,10],[15,18]]
# print(merge(intervals))
# intervals = [[1, 4]]  # Output: [[1, 4]]
# print(merge(intervals))
# intervals = [[1, 4], [4, 5]]  # Output: [[1, 5]]
# print(merge(intervals))
intervals = [[1, 4], [0, 2], [3, 5]]  # Output: [[0, 5]]
print(merge(intervals))
