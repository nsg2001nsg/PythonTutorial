class CircularQueue:

    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, value):
        if self.size != self.capacity:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = value
            self.size += 1
            return
        print("Queue is full!")

    def dequeue(self):
        if self.size != 0:
            val = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            if self.size == 0:
                self.front = 0
                self.rear = -1
            return val
        print("Queue is empty")

    def peek(self):
        if self.size != 0:
            return self.queue[self.front]
        print("Queue is Empty")

    def __str__(self):
        qu = []
        x = self.front
        cap = 0
        while self.queue[x] is not None and cap < self.capacity:
            qu.append(self.queue[x])
            x = (x + 1) % self.capacity
            cap += 1
        return f"Current Queue: {qu}"


q = CircularQueue(10)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)
print(q)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue(11)
print(q)
print(q.peek())

q = CircularQueue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)  # [1,2,3,n,n]
q.dequeue()  # [n,2,3,n,n]
q.dequeue()  # [n,n,3,n,n]
q.enqueue(4)  # [n,n,3,4,n]
q.enqueue(5)  # [n,n,3,4,5]
q.dequeue()  # [n,n,n,4,5]
q.enqueue(8)  # [6,n,n,4,5]
print(q)
