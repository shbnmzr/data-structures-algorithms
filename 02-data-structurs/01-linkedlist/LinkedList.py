class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, nodes):
        self.head = None
        self.length = 0
        if nodes is not None:
            self.head = Node(nodes[0])
            current_node = self.head
            for item in nodes[1:]:
                new_node = Node(item)
                current_node.next = new_node
                current_node = current_node.next
            current_node.next = None

    def traverse(self):
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next


def main():
    nodes = ['a', 'b', 'c', 'd']
    linkedlist = LinkedList(nodes)
    for item in linkedlist.traverse():
        print(item)


if __name__ == '__main__':
    main()
