"""
102. Binary Tree Level Order Traversal
Medium
Topics
premium lock icon
Companies
Hint
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_order(root):
    if not root:
        return []

    q = deque(root)
    result = []
    while q:
        size = len(q)
        temp = []

        while size:
            node = q.popleft()
            temp.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            size -= 1
        result.append(temp)

    return result