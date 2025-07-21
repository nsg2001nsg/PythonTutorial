from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        print("Empty List")

    def peek(self):
        if self.queue:
            return self.queue[0]
        print("Empty List")

    def is_empty(self):
        return not self.queue

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return f"Current Queue: {list(self.queue)}"


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
