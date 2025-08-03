class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root:
            node = self.root
            while node:
                if new_node.data < node.data:
                    if node.left:
                        node = node.left
                    else:
                        node.left = new_node
                        return
                elif new_node.data > node.data:
                    if node.right:
                        node = node.right
                    else:
                        node.right = new_node
                        return
                else:
                    return
        else:
            self.root = new_node

    def inorder(self):
        if self.root:
            stack = [self.root]
            last_visited = set()
            while stack:
                node = stack.pop()
                if node.left and node not in last_visited:
                    stack.append(node)
                    stack.append(node.left)
                    last_visited.add(node)
                    continue
                print(node.data, end=" ")
                if node.right:
                    stack.append(node.right)
        else:
            print("Tree is Empty!")

    def inorder_recursive(self, node):
        if node is None:
            return
        self.inorder_recursive(node.left)
        print(node.data, end=" ")
        self.inorder_recursive(node.right)

    def preorder(self):
        if self.root:
            stack = [self.root]
            while stack:
                node = stack.pop()
                print(node.data, end=" ")
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        else:
            print("Tree is Empty!")

    def preorder_recursive(self, node):
        if node is None:
            return
        print(node.data, end=" ")
        self.preorder_recursive(node.left)
        self.preorder_recursive(node.right)

    def postorder(self):
        if self.root:
            stack = [self.root]
            last_visited = set()
            while stack:
                node = stack.pop()
                if node not in last_visited:
                    stack.append(node)
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)
                    last_visited.add(node)
                    continue
                print(node.data, end=" ")
        else:
            print("Tree is Empty!")

    def postorder_recursive(self, node):
        if node is None:
            return
        self.postorder_recursive(node.left)
        self.postorder_recursive(node.right)
        print(node.data, end=" ")

    def search(self, value):
        if self.root:
            node = self.root
            while node:
                if value < node.data:
                    node = node.left
                elif value > node.data:
                    node = node.right
                else:
                    return True
        return False

    def delete(self, value):
        if self.root:
            node = self.root
            if value < node:
                pass

    def height(self):
        if self.root is None:
            return -1

        stack = [(self.root, 0)]  # [2 1]
        max_depth = 0  # 0

        while stack:
            node, depth = stack.pop()  # 15 0
            max_depth = max(max_depth, depth)  # 0
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return max_depth


bst = BinarySearchTree()
# bst.root = Node(2)
# bst.root.left = Node(1)
# bst.root.left.left = Node(0)
# bst.root.right = Node(9)
# bst.root.right.left = Node(6)
# bst.root.right.left.left = Node(4)
# bst.root.right.left.right = Node(7)
# bst.inorder()
# print()
# bst.inorder_recursive(bst.root)
# print()
# bst.preorder()
# print()
# bst.preorder_recursive(bst.root)
# print()
# bst.postorder()
# print()
# bst.postorder_recursive(bst.root)
# print()
# print(bst.search(0))
# print(bst.search(4))
# print(bst.search(2))
# print(bst.search(7))
# print(bst.search(10))
bst.root = Node(15)
bst.root.left = Node(2)
bst.root.right = Node(19)
bst.root.left.left = Node(1)
bst.root.left.left.left = Node(0)
bst.root.left.right = Node(3)
bst.root.left.right.right = Node(11)
bst.root.left.right.right.left = Node(10)
bst.root.right = Node(19)
bst.root.right.left = Node(16)
bst.root.right.right = Node(20)
bst.postorder()
print()
print(bst.height())

