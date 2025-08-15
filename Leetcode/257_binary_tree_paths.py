class treeNode:

    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


def binaryTreePaths(root):
    if not root:
        return []

    stack = [[root, str(root.value)]]
    result = []

    while stack:

        node, path = stack.pop()

        if not node.left and not node.right:  # if no child then append path to result
            result.append(path)

        if node.right:  # if right child is present append it before so left is processed first
            stack.append([node.right, path + "->" + str(node.right.value)])

        if node.left:
            stack.append([node.left, path + "->" + str(node.left.value)])

    return result




