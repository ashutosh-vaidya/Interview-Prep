class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        # no of nodes in the linked list
        self.n = 0

    def __increment_node_count(self):
        self.n += 1

    def __decrement_node_count(self):
        self.n -= 1

    # returns the number of nodes present in the linkedlist
    def __len__(self):
        return self.n

    # override the __str__ to be able to print linkedlist
    def __str__(self):
        result = ""
        curr = self.head
        while curr is not None:
            result = result + str(curr.data) + " -> "
            curr = curr.next

        return result[:-3]

    # insert from head
    def insert_head(self, value):
        # create new node
        new_node = Node(value)

        # if linkedlist is empty set new node as a head
        if self.head is None:
            self.head = new_node
            self.__increment_node_count()
            return

        # else
        # link the head to new_node
        new_node.next = self.head

        # Assign new_node as a head
        self.head = new_node

        # increase the node count
        self.__increment_node_count()

    # insert at the tail, append
    def append(self, value):
        # create new node
        new_node = Node(value)

        # if linkedlist is empty set new_node as head
        if self.head is None:
            self.head = new_node
            return

        # else
        # traverse to the tail of linkedlist
        curr = self.head
        while curr.next is not None:
            curr = curr.next

        # we have reached the tail
        # link new_node with the tail
        curr.next = new_node

        # increase the node count
        self.__increment_node_count()

    # inserting at middle (insert_after)
    def insert_after(self, after, value):
        # check if linkedlist is empty
        if self.head is None:
            raise ValueError("LinkedList is empty, used append or insert_head instead")

        # create new_node
        new_node = Node(value)

        # traverse till the after node
        curr = self.head
        while curr.next is not None:
            if curr.data == after:
                break
            curr = curr.next

        # case 1: curr is at the tail
        if curr.next is None:
            curr.next = new_node
        # case 2: curr is not at tail
        else:
            # link curr.next to new_node next
            new_node.next = curr.next
            # link new_node to curr
            curr.next = new_node

        # increase the counter
        self.__increment_node_count()
