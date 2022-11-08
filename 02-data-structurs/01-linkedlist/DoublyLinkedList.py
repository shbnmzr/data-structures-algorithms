class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, nodes):
        self.head = None
        self.rear = self.head
        self.length = len(nodes)
        if nodes:
            self.head = Node(nodes[0])
            self.head.prev = None
            current_node = self.head
            for item in nodes[1:]:
                new_node = Node(item)
                new_node.prev = current_node
                current_node.next = new_node
                current_node = current_node.next
            current_node.next = None
            self.rear = current_node
        return

    def traverse(self):
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next
        return

    def reverse_traverse(self):
        current_node = self.rear
        while current_node:
            yield current_node.data
            current_node = current_node.prev
        return

    def append(self, data):
        new_node = Node(data)
        self.rear.next = new_node
        new_node.prev = self.rear
        new_node.next = None
        self.rear = new_node
        return

    def delete(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                if current_node == self.head:
                    self.head = self.head.next
                    self.head.prev = None
                    current_node.next = None
                    self.length -= 1
                    return
                if current_node == self.rear:
                    self.rear = self.rear.prev
                    self.rear.next = None
                    current_node.prev = None
                    self.length -= 1
                    return
                prev_node = current_node.prev
                next_node = current_node.next
                prev_node.next = current_node.next
                next_node.prev = prev_node
                current_node.next, current_node.prev = None, None
                self.length -= 1
                return
            current_node = current_node.next
        return

    def insert(self, data, position):
        if position > self.length + 1:
            raise Exception('Given position does not match linkedlist\'s length.')
        if position == 1:
            new_node = Node(data)
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
            return
        current_position = 1
        current_node = self.head
        while current_position < position:
            current_node = current_node.next
            current_position += 1
        new_node = Node(data)
        new_node.prev = current_node.prev
        new_node.next = current_node
        next_node = current_node
        current_node = current_node.prev
        next_node.prev = new_node
        current_node.next = new_node
        self.length += 1
        return
