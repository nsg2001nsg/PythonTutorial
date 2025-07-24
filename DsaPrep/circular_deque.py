class Deque:

    def __init__(self, capacity):
        self.deque = [None] * capacity
        self.size = 0
        self.front = 0
        self.rear = -1
        self.capacity = capacity

    def enqueue_right(self, value):
        if self.size < self.capacity:
            self.rear = (self.rear + 1) % self.capacity
            self.deque[self.rear] = value
            self.size += 1
            return
        print("Queue is Full!")

    def enqueue_left(self, value):
        if self.size < self.capacity:
            self.front = (self.front - 1) % self.capacity
            self.deque[self.front] = value
            self.size += 1
            return
        print("Queue is Full!")

    def dequeue_left(self):
        if self.size > 0:
            popped = self.deque[self.front]
            self.deque[self.front] = None
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            if self.size == 0:
                self.front = 0
                self.rear = -1
            return popped
        print("Queue is Empty!")
        return

    def dequeue_right(self):
        if self.size > 0:
            popped = self.deque[self.rear]
            self.deque[self.rear] = None
            self.rear = (self.rear - 1) % self.capacity
            self.size -= 1
            if self.size == 0:
                self.front = 0
                self.rear = -1
            return popped
        print("Queue is Empty!")
        return

    def __str__(self):
        rep = []
        x = self.front
        for _ in range(self.size):
            if self.deque[x] is not None:
                rep.append(self.deque[x])
            x = (x + 1) % self.capacity
        return f"Current Queue: {rep}"

    def peek(self):
        if self.size != 0:
            return self.deque[self.front]
        return None

    def is_empty(self):
        return not self.size

    def is_full(self):
        return self.size == self.capacity


d = Deque(10)
print(d)
d.enqueue_left(5)
d.enqueue_left(11)
d.enqueue_right(6)
d.enqueue_right(7)
d.enqueue_right(8)
d.enqueue_right(9)
d.dequeue_left()
d.dequeue_right()
d.dequeue_right()
d.dequeue_right()
d.dequeue_right()
d.dequeue_right()
print(d.peek())
print(d)
print(d.is_full())
print(d.is_empty())

d = Deque(5)
d.enqueue_right(1)
d.enqueue_right(2)
d.enqueue_right(3)
d.enqueue_right(4)
d.enqueue_right(5)
print(d)
d.dequeue_right()
d.dequeue_right()
d.enqueue_left(9)
d.enqueue_left(8)
print(d)



