from .LinkedList import *


def merge_k_lists(lists):
    k = len(lists)
    if k > 1:
        merged = lists[0]
        head = merged[0]
        current_node = head
        prev_node = current_node
        for li in lists[1:]:
            if li:
                new_node = li[0]
                while current_node and new_node:
                    if current_node.data > new_node.data:
                        prev_node.next = new_node
                        new_node.next = current_node
                        prev_node = prev_node.next
                        new_node = new_node.next
                    else:
                        prev_node = current_node
                        current_node = current_node.next


    return []
