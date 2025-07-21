class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, data):
        new_node = Node(data)
        self.length += 1
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
            return
        self.head = self.tail = new_node
        return

    def dequeue(self):
        if self.head:
            node = self.head
            self.head = self.head.next
            self.length -= 1
            if not self.head:
                self.tail = None
            return node.data
        return None

    def peek(self):
        if self.head:
            return self.head.data
        return None

    def __len__(self):
        return self.length

    def __str__(self):
        rep = []
        node = self.head
        while node:
            rep.append(node.data)
            node = node.next
        return f"Queue: {rep}"

    def is_empty(self):
        return not self.length


q = Queue()
print(q.is_empty())
q.enqueue(0)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
print(q)
print(q.dequeue())
print(q)
print(q.peek())
print(q)
print(q.is_empty())
print(len(q))