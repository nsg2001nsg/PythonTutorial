"""
Problem:
You are given a string s and an integer k.
Return the length of the longest substring that contains at most k distinct characters.

🔹 Example
Input:  s = "eceba", k = 2
Output: 3
Explanation: "ece" is the longest substring with at most 2 distinct characters.

Input:  s = "aa", k = 1
Output: 2
Explanation: "aa" is the longest substring with at most 1 distinct character.
"""

"""
def longest_substring(s, k):
    hashmap = dict()
    left = 0
    right = 0
    max_len = 0

    while right < len(s):
        # expand window by including s[right]
        hashmap[s[right]] = hashmap.get(s[right], 0) + 1

        # shrink if distinct > k
        while len(hashmap) > k:
            hashmap[s[left]] -= 1
            if hashmap[s[left]] == 0:
                del hashmap[s[left]]
            left += 1

        # update max length
        max_len = max(max_len, right - left + 1)

        # move right pointer
        right += 1

    return max_len


# [10, 5, 6, 4, 3, 2] k = 15
"""

"""
def longest_substring(arr, k):  # handles only positives
    sum_arr = arr[0]
    left, right = 0, 1
    size = 0

    while right < len(arr):

        if sum_arr == k:
            size = max(size, right-left)
        elif sum_arr > k:
            while sum_arr > k:
                sum_arr -= arr[left]
                left += 1

        right += 1
        if right < len(arr):
            sum_arr += arr[right]

    return size


print(longest_substring([10, 5, 6, 4, 3, 2], 15))
"""


def longest_subarray_sum_k(arr, k):  # handles positives and negatives
    prefix_sum = 0
    prefix_map = {}  # stores first occurrence of prefix_sum
    size = 0

    for i, num in enumerate(arr):
        prefix_sum += num

        if prefix_sum == k:
            size = max(size, i + 1)

        if (prefix_sum - k) in prefix_map:
            size = max(size, i - prefix_map[prefix_sum - k])

        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    return size
