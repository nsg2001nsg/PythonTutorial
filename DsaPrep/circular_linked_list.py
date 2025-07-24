class Node:

    def __init__(self, value=None):
        self.data = value
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        self.length += 1
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
            return
        new_node.next = new_node
        self.head = self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)
        self.length += 1
        if self.head:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
            return
        new_node.next = new_node
        self.head = self.tail = new_node

    def pop(self):
        if self.head and self.length > 1:
            node = self.head
            prev = None
            while node.next != self.head:
                prev = node
                node = node.next
            prev.next = self.head
            self.tail = prev
            self.length -= 1
            return node.data
        elif self.length == 1:
            node = self.head
            self.head = self.tail = None
            self.length -= 1
            return node.data
        print("List is Empty")
        return None

    def delete(self, value):
        if self.head:
            node = self.head
            prev = None
            while node.next != self.head and node.data != value:
                prev = node
                node = node.next
            if node.data != value:
                print("Value Not Found!")
                return
            if node != self.head and node != self.tail:
                prev.next = node.next
            elif node == self.head == self.tail:
                self.head = self.tail = None
            elif node == self.head:
                self.head = self.head.next
            else:
                prev.next = self.head
                self.tail = prev
            self.length -= 1
            return
        print("List is Empty")

    def __str__(self):
        rep = []
        node = self.head
        for _ in range(self.length):
            rep.append(node.data)
            node = node.next
        return f"Current list: {rep}"

    def __len__(self):
        return self.length

    def is_empty(self):
        return self.length == 0


cl = CircularLinkedList()
print(cl)
cl.append(1)
cl.append(2)
cl.append(3)
cl.append(4)
cl.prepend(0)
print(cl)
cl.pop()
cl.pop()
cl.prepend(0)
cl.delete(5)
cl.delete(6)
print(cl)
print(cl.is_empty())
