class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            curr_node = self.head
            while curr_node.next != self.head:
                curr_node = curr_node.next

            curr_node.next = new_node;
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        curr_node = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = self.head
        else:
            while curr_node.next != self.head:
                curr_node = curr_node.next
            curr_node.next = new_node

        self.head = new_node

    def delete(self, key):
        if self.head is None:
            return
        if self.head.next == self.head and self.head.data == key:
            self.head = None
        elif self.head.data == key:
            curr_node = self.head
            while curr_node.next != self.head:
                curr_node = curr_node.next
            curr_node.next = self.head.next
            self.head = self.head.next

        else:
            curr_node = self.head
            prev = None
            while curr_node.next != self.head:
                prev = curr_node
                curr_node = curr_node.next
                # print('ss',curr_node.data)
                if curr_node.data == key:
                    prev.next = curr_node.next
                    curr_node = curr_node.next

    def lookup(self):
        curr_node = self.head

        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
            if curr_node == self.head:
                break


circularLls = CircularLinkedList()
# circularLls.append(1)
# circularLls.append(2)
# circularLls.append(3)
# circularLls.append(4)
# circularLls.prepend(0)
# circularLls.prepend(-1)
circularLls.delete(1)
circularLls.lookup()
