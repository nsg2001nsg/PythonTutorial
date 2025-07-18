class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.tail:
            node = self.tail
            node.next = new_node
            new_node.prev = node
            self.tail = new_node
        else:
            self.head = self.tail = new_node
        self.length += 1
        return

    def prepend(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            temp = new_node.next
            temp.prev = new_node
            self.head = new_node
        else:
            self.head = self.tail = new_node
        self.length += 1
        return

    def append_at(self, data, index):
        if index == 0 and self.head:
            self.prepend(data)
        elif index == 0 and not self.head:
            new_node = Node(data)
            self.head = self.tail = new_node
            self.length += 1
        elif index == self.length:
            self.append(data)
        elif 0 < index < self.length:
            new_node = Node(data)
            if index <= self.length // 2:
                node = self.head
                while index:
                    node = node.next
                    index -= 1
            else:
                node = self.tail
                for _ in range(1, self.length - index):
                    node = node.prev
            prev = node.prev
            prev.next = new_node
            new_node.next = node
            node.prev = new_node
            new_node.prev = prev
            self.length += 1
        else:
            print("Invalid Index!")
        return

    def display(self):
        if self.head:
            node = self.head
            while node:
                print(node.data, end=" ")
                node = node.next
            print()
            return
        print("List is Empty!")

    def display_reverse(self):
        if self.tail:
            node = self.tail
            while node:
                print(node.data, end=" ")
                node = node.prev
            print()
            return
        print("List is Empty!")


ll1 = DoublyLinkedList()
ll1.append(1)
ll1.append(2)
# ll1.append(3)
# ll1.append(4)
# ll1.append(5)
# ll1.append(6)
# ll1.append(7)
ll1.append(8)
ll1.append(9)
# ll1.append(10)
# ll1.append(11)
# ll1.display()
# ll1.display_reverse()
ll1.append_at(13, 0)
ll1.display()
ll1.append_at(4, 3)
ll1.display()
print('length: ', ll1.length)
