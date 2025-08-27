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



