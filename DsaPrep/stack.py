class StackArray:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        return

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Stack is Empty!")
            return

    def peek(self):
        if self.stack:
            return self.stack[-1]
        print('Stack is Empty')

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return not self.stack

    def display(self):
        if self.stack:
            for x in self.stack[::-1]:
                print(x)
            return
        print('Stack is Empty')

    def __str__(self):
        return f"Current Stack: {self.stack[::-1]}" if self.stack else "Stack is Empty!"


stack1 = StackArray()
stack1.push(7)
stack1.push(7)
stack1.push(0)
stack1.push(9)
stack1.push(6)
stack1.push(0)
stack1.push(3)
stack1.push(1)
stack1.push(6)
stack1.push(8)
stack1.display()
print()
print('popped:', stack1.pop())
print(stack1.is_empty())
print(stack1.size())
print(stack1.peek())
print(stack1)

