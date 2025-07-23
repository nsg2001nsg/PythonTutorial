class Deque:

    def __init__(self, capacity):
        self.deque = [None] * capacity
        self.size = 0
        self.front = 1
        self.rear = -1
        self.capacity = capacity

    def enqueue_right(self, value):
        if self.size < self.capacity:
            self.rear = (self.rear + 1) % self.capacity
            if self.rear == 0 and self.front == 0:
                self.rear += 1
            print(self.rear)
            self.deque[self.rear] = value
            self.size += 1
            return
        print("Queue is Full!")

    def enqueue_left(self, value):
        if self.size < self.capacity:
            self.front = (self.front - 1) % self.capacity
            if self.front == 0 and self.rear == 0:
                self.front -= 1
            print(self.front)
            self.deque[self.front] = value
            self.size += 1
            return
        print("Queue is Full!")

    def __str__(self):
        rep = []
        x = self.front
        for _ in range(self.capacity):
            if self.deque[x] is not None:
                rep.append(self.deque[x])
            x = (x + 1) % self.capacity
        return f"Current Queue: {rep}"

    def peek(self):
        if self.size != 0:
            return self.deque[self.front]
        return None


d = Deque(10)
print(d)
d.enqueue_left(5)
d.enqueue_right(6)
d.enqueue_right(7)
d.enqueue_right(8)
d.enqueue_right(9)
d.enqueue_right(10)
d.enqueue_left(11)
d.enqueue_left(12)
d.enqueue_left(13)
d.enqueue_left(14)
d.enqueue_left(15)
print(d)


