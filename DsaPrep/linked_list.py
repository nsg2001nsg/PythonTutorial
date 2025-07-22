class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.length += 1
        return

    def display(self):
        if self.head:
            node = self.head
            while node:
                print(node.data, end=" ")
                node = node.next
        else:
            print("List is Empty!")
        print()

    def prepend(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, data, index):
        if self.head and 0 < index < self.length:
            new_node = Node(data)
            node = self.head
            prev = None
            while index:
                prev = node
                node = node.next
                index -= 1
            prev.next = new_node
            new_node.next = node
            self.length += 1
            return
        elif index == 0:
            self.prepend(data)
            return
        elif index == self.length:
            self.append(data)
            return
        print("Invalid index")
        return

    def delete(self, value):
        if self.head:
            node = self.head
            prev = None
            while node and node.data != value:
                prev = node
                node = node.next
            if node is None:
                print("Value not found")
                return
            if node != self.head and node != self.tail:
                prev.next = node.next
            elif self.head == node == self.tail:
                self.head = self.tail = None
            elif node == self.head:
                self.head = node.next
            elif node == self.tail:
                prev.next = None
                self.tail = prev
            self.length -= 1
            return
        print("Empty list!")
        return

    def delete_all(self, value):
        if self.head:
            node = self.head
            prev = None
            while node:
                if node.data == value:
                    if node != self.head and node != self.tail:
                        prev.next = node.next
                        node = prev.next
                    elif node == self.head:
                        self.head = node.next
                        node = self.head
                        if self.head is None:
                            self.tail = None
                    elif node == self.tail:
                        prev.next = None
                        self.tail = prev
                        node = None
                    self.length -= 1
                    continue
                prev = node
                node = node.next
        else:
            print("Empty list!")
        return

    def update(self, new_value, old_value):
        if self.length == 0:
            print("Empty list!")
            return
        node = self.head
        while node and node.data != old_value:
            node = node.next
        if node:
            node.data = new_value
            return
        print("Value not found")

    def update_all(self, data, value):
        if self.length == 0:
            print("Empty list!")
            return
        node = self.head
        while node:
            if node.data == value:
                node.data = data
            node = node.next

    def update_index(self, data, index):
        if self.head and 0 <= index < self.length:
            node = self.head
            while index:
                node = node.next
                index -= 1
            node.data = data
            return
        print("Invalid Index!")
        return

    def reverse(self):
        if self.head and self.length > 1:
            current = self.head
            prev = None
            while current.next:
                new = current.next
                current.next = prev
                prev = current
                current = new
            current.next = prev
            self.tail = self.head
            self.head = current
        else:
            print("Empty List!")
        return

    def pop(self):
        node = self.head
        if self.head and self.length > 1:
            prev = None
            while node.next:
                prev = node
                node = node.next
            prev.next = None
            self.length -= 1
            return node.data
        elif self.length == 1:
            self.head = self.tail = None
            self.length -= 1
            return node.data
        else:
            return None

    def pop_left(self):
        if self.head:
            node = self.head.data
            self.head = self.head.next
            self.length -= 1
            if self.head is None:
                self.tail = None
            return node
        return None

    def delete_index(self, index):
        if self.head:
            if 0 < index < self.length - 1:
                node = self.head
                prev = None
                for _ in range(index):
                    prev = node
                    node = node.next
                prev.next = node.next
                self.length -= 1
                return node.data
            elif index == 0:
                return self.pop_left()
            elif index == self.length - 1:
                return self.pop()
            else:
                print("Invalid index")
                return None
        else:
            print("List is Empty!")
            return None

    def find(self, value):
        if self.head:
            node = self.head
            while node:
                if node.data == value:
                    return True
                node = node.next
            return False
        print('List is Empty!')

    def get(self, index):
        if self.head and self.length > index >= 0:
            node = self.head
            while index:
                node = node.next
                index -= 1
            return node.data
        elif index >= self.length:
            print('Invalid Index!')
        else:
            print('List is Empty!')
        return

    def __len__(self):
        return self.length


if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(2)
    ll1.append(3)
    ll1.append(5)
    ll1.append(4)
    ll1.append(6)
    ll1.append(8)
    ll1.append(10)
    ll1.append(9)
    ll1.prepend(9)
    ll1.insert(99, 0)
    ll1.insert(12, 11)
    ll1.display()
    ll1.update(4, 99)
    ll1.display()
    ll1.update_all(0, 4)
    ll1.display()
    ll1.delete(5)
    ll1.append(8)
    ll1.append(8)
    ll1.display()
    ll1.delete_all(8)
    # ll1.reverse()
    ll1.display()
    print(ll1.pop())
    ll1.display()
    print(ll1.find(0))
    print(ll1.find(6))
    print(ll1.find(12))
    print(ll1.find(9))
    print('length:', ll1.length)
    print(ll1.get(10))
    ll1.update_index(13, 0)
    ll1.update_index(14, -1)
    ll1.update_index(15, 8)
    ll1.update_index(16, 9)
    ll1.display()
    ll1.pop_left()
    ll1.display()
    ll1.delete_index(0)
    ll1.display()
    ll1.delete_index(4)
    ll1.display()
    ll1.delete_index(5)
    ll1.display()
    ll1.delete_index(8)
    ll1.display()
