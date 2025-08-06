"""
739. Daily Temperatures
Medium
Topics
premium lock icon
Companies
Hint
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.



Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]


Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""


def dailyTemperatures(temperatures):
    stack = []
    nwd = {}
    for i, temp in enumerate(temperatures):
        while stack and stack[-1][0] < temp:
            cooler = stack.pop()
            nwd[cooler[1]] = i - cooler[1]
        stack.append([temp, i])

    for rest in stack:
        nwd[rest[1]] = 0
    return [nwd[v] for v in range(len(temperatures))]


def dailyTemperatures_opt(temperatures):
    stack = []
    res = [0] * len(temperatures)
    for i, temp in enumerate(temperatures):
        while stack and stack[-1][0] < temp:
            _, j = stack.pop()
            res[j] = i - j
        stack.append([temp, i])

    for rest in stack:
        res[rest[1]] = 0
    return [res[v] for v in range(len(temperatures))]


print(dailyTemperatures([30]))  # [0]
print(dailyTemperatures([]))  # []
print(dailyTemperatures([30, 40, 50, 60]))  # [1,1,1,0]
print(dailyTemperatures_opt([73, 74, 75, 73, 71, 69, 72, 76, 79]))  # [1,1,5,4,2,1,1,0,0]
print(dailyTemperatures([30, 60, 90]))  # [1,1,0]
