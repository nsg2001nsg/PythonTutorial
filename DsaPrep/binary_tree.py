from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.height = 0

    def insert(self, value):
        new_node = Node(value)
        if self.root:
            q = deque()  # []
            node = self.root
            while node:
                if node.left is None:
                    node.left = new_node
                    return
                else:
                    q.append(node.left)

                if node.right is None:
                    node.right = new_node
                    return
                else:
                    q.append(node.right)
                node = q.popleft()
        self.root = new_node

    def insert_mod(self, value):
        new_node = Node(value)
        if self.root:
            q = deque([self.root])
            while q:
                node = q.popleft()
                if node.left is None:
                    node.left = new_node
                    return
                else:
                    q.append(node.left)

                if node.right is None:
                    node.right = new_node
                    return
                else:
                    q.append(node.right)
        self.root = new_node

    def display(self):
        if self.root:
            q = deque()  # []
            node = self.root
            print(node.data)
            while node:
                if node.left is None:
                    return
                else:
                    print(node.left.data)
                    q.append(node.left)
                if node.right is None:
                    return
                else:
                    print(node.right.data)
                    q.append(node.right)
                node = q.popleft()
        print("Tree is Empty!")


b = BinaryTree()
b.display()
b.insert(1)
b.insert(2)
b.insert(3)
b.insert(4)
b.insert(5)
b.insert(6)
b.insert(7)
b.display()