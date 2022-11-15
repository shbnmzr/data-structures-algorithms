class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, li):
        if li:
            self.head = Node(data=li[0])
            current = self.head
            for item in li[1:]:
                new_node = Node(data=item)
                current.next = new_node
                current = current.next


def traverse(head):
    current_node = head
    while current_node:
        yield current_node.data
        current_node = current_node.next
    return head


def reverse(head):
    current = head
    new_head = None
    while current:
        new_node = Node(current.data, new_head)
        new_head = new_node
        current = current.next

    return new_head


def remove_nth_from_end(head, n=1):
    current = reverse(head)
    for i in traverse(head):
        print(i)
    prev = None
    counter = 1
    while counter < n:
        prev = current
        current = current.next
        counter += 1
    else:
        prev.next = current.next
        current.next = None

    return reverse(head)


def main():
    li = ['a', 'b', 'c', 'd']
    linkedlist = LinkedList(li)
    new_head = remove_nth_from_end(linkedlist.head, 3)

    # for i in traverse(new_head):
    #     print(i)


if __name__ == '__main__':
    main()
