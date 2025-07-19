class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return

    def pop(self):
        node = self.head
        if self.head and self.length > 1:
            self.head = node.next
            self.length -= 1
            return node.data
        elif self.length == 1:
            self.head = None
            self.length -= 1
            return node.data
        else:
            print("Stack is Empty!")
        return

    def peek(self):
        if self.head:
            return self.head.data
        print("Stack is Empty!")
        return

    def __len__(self):
        return self.length

    def __str__(self):
        if self.head:
            node = self.head
            rep = ""
            while node:
                rep += " " + str(node.data)
                node = node.next
            return f"Top ->{rep} -> Bottom"
        return "Stack is Empty"

    def is_empty(self):
        return not self.head

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next


stack1 = Stack()
print(stack1.is_empty())
stack1.push(7)
stack1.push(7)
stack1.push(0)
stack1.push(9)
stack1.push(6)
stack1.push(0)
stack1.push(3)
stack1.push(1)
print(stack1)
print('Popped:', stack1.pop())
print('Length:', len(stack1))
print('Top:', stack1.peek())
print(stack1)
for val in stack1:
    print(val)
