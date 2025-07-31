from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

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

    def postorder(self):
        if not self.root:
            print("Tree is empty")
            return

        stack = []
        result = []
        last_visited = None
        node = self.root

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                peek = stack[-1]
                # If right child exists and hasn't been visited yet
                if peek.right and last_visited != peek.right:
                    node = peek.right
                else:
                    result.append(peek.data)
                    last_visited = stack.pop()

        print("Postorder:", *result)

    def postorder_mod(self):  # Left Right Root
        if self.root:
            stack = [self.root]
            visited = set()
            left = set()
            while stack:
                node = stack.pop()
                if node.left and node not in left:
                    stack.append(node)
                    stack.append(node.left)
                    left.add(node)
                    continue
                elif node.right and node not in visited:
                    visited.add(node)
                    stack.append(node)
                    stack.append(node.right)
                    continue
                print(node.data, end=" ")
        else:
            print("Tree is Empty!")

    def height(self, node):
        if node is None:
            return -1
        left = self.height(node.left)
        right = self.height(node.right)
        return 1 + max(left, right)


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

# bt = BinaryTree()
# bt.root = Node(1)
# bt.root.left = Node(2)
# bt.root.right = Node(3)
# bt.root.left.right = Node(4)
# bt.root.left.right.left = Node(6)
# bt.root.right.right = Node(5)
# bt.root.right.right.left = Node(7)

bt = BinaryTree()
bt.root = Node(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)
bt.inorder()
print()
bt.preorder()
print()
bt.postorder_mod()
print()
print(bt.height(bt.root))
