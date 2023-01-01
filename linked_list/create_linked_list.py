class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def create_linked_list(values):
    head_node = Node(values[0])
    head = head_node
    for i in range(1, len(values)):
        node = Node(values[i])
        head.next = node
        head = head.next
    return head_node


def size_of_linked_list(head_node):
    size = 1
    while head_node.next is not None:
        head_node = head_node.next
        size += 1
    return size

def insert_node(head_node, value, index):
    pass



print(create_linked_list([1]).next)
print(size_of_linked_list(create_linked_list([1, 2, 2])))
