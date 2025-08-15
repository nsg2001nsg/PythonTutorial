"""
230. Kth Smallest Element in a BST
Medium
Topics
premium lock icon
Companies
Hint
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.



Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3


Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
"""
from collections import deque


class TreeNode:

    def __init__(self, data):
        self.val = data
        self.left, self.right = None, None


def kth_smallest_bst(root, k):
    stack = [root]
    visited = []
    # sort_tree = deque()  # to store values in case sorted tree is required (not in this case)
    count = 0
    while stack:
        node = stack.pop()
        if (node not in visited) and (node.left or node.right):
            flag = 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node)
                stack.append(node.left)
                flag = 0
            if flag:
                stack.append(node)
            visited.append(node)
        else:
            count += 1
            if count == k:
                return node.val


bst = TreeNode(5)
bst.left = TreeNode(3)
bst.left.right = TreeNode(4)
bst.left.left = TreeNode(2)
bst.left.left.left = TreeNode(1)
bst.right = TreeNode(6)

print(kth_smallest_bst(bst, 1))
print(kth_smallest_bst(bst, 2))
print(kth_smallest_bst(bst, 6))





