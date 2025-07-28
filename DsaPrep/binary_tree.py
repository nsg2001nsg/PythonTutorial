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

    def inorder(self):  # Left Root Right
        if self.root:
            node = self.root
            q = deque()
            flag = 1
            while node:
                if node.left:
                    if flag:
                        q.appendleft(node)
                        node = node.left
                        flag = 1
                        continue
                print(node.data, end=" ")
                if node.right:
                    node = node.right
                    flag = 1
                else:
                    try:
                        node = q.popleft()
                    except Exception:
                        return
                    flag = 0
        else:
            print("Tree is Empty!")

    def preorder(self):  # Root Left Right
        if self.root:
            node = self.root
            stack = []
            flag = 1
            while node:
                if flag:
                    print(node.data, end=" ")
                    if node.left:
                        stack.append(node)
                        node = node.left
                        flag = 1
                        continue
                if node.right:
                    node = node.right
                    flag = 1
                else:
                    try:
                        node = stack.pop()
                    except Exception:
                        return
                    flag = 0
        else:
            print("Tree is Empty!")

    def postorder(self):  # Left Right Root
        if self.root:
            node = self.root  # 1 2 4 6 4 2
            stack = []  # 1
            flag = 1  # 1 0
            count = 0
            while node and count < 100:
                count += 1
                if node.left and flag:
                    stack.append(node)
                    node = node.left
                    flag = 1
                    continue
                elif node.right and flag:
                    stack.append(node)                  #    1
                    node = node.right                   #  /   \
                    flag = 1                            # 2     3
                    continue                            #  \     \
                else:                                   #   4     5
                    print(node.data)                    #  /     /
                    try:                                # 6     7
                        node = stack.pop()
                    except Exception:
                        return
                    flag = 0
        else:
            print("Tree is Empty!")


# b = BinaryTree()
# b.display()
# b.insert(1)
# b.insert(2)
# b.insert(3)
# b.insert(4)
# b.insert(5)
# b.insert(6)
# b.insert(7)
# b.display()

bt = BinaryTree()
bt.root = Node(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.right = Node(4)
bt.root.left.right.left = Node(6)
bt.root.right.right = Node(5)
bt.root.right.right.left = Node(7)
bt.inorder()
print()
bt.preorder()
print()
bt.postorder()
