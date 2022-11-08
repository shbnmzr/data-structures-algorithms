class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, nodes):
        self.head = None
        self.rear = self.head
        self.length = 0
        if nodes is not None:
            self.head = Node(nodes[0])
            current_node = self.head
            self.length += 1
            for item in nodes[1:]:
                new_node = Node(item)
                current_node.next = new_node
                current_node = current_node.next
                self.length += 1
            self.rear = current_node
            current_node.next = None

    @property
    def get_length(self):
        return self.length

    def traverse(self):
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next
        return

    def append(self, data):
        current_node = Node(data)
        self.rear.next = current_node
        self.rear = self.rear.next
        self.rear.next = None
        self.length += 1
        return

    def delete(self, data):
        current_node = self.head
        prev_node = None
        while current_node:
            if current_node.data == data:
                if current_node == self.head:
                    self.head = self.head.next
                    return
                if current_node == self.rear:
                    prev_node.next = None
                    return
                prev_node.next = current_node.next
                current_node.next = None
                self.length -= 0
                return
            prev_node = current_node
            current_node = current_node.next
        return

    def insert(self, data, position):
        current_node = self.head
        prev_node = None
        if position > self.length + 1:
            raise Exception('Position does not match linkedlist\'s length.')

        if position == 1:
            new_node = Node(data)
            new_node.next = current_node
            self.head = new_node
            return
        current_pos = 1
        while current_pos < position:
            prev_node = current_node
            current_node = current_node.next
            current_pos += 1
        new_node = Node(data)
        new_node.next = current_node
        prev_node.next = new_node
        self.length += 1
        return
