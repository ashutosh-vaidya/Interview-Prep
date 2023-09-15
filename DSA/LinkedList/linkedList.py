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
            raise ValueError("LinkedList is empty, use append or insert_head instead")

        # traverse till the after node
        curr = self.head
        while curr is not None:
            if curr.data == after:
                break
            curr = curr.next

        # Case : if after does not exist
        if curr is None:
            raise ValueError(f"Value {after} does not exists in the linked list")

        # else
        # create new_node
        new_node = Node(value)

        # link curr.next to new_node next
        new_node.next = curr.next
        # link new_node to curr
        curr.next = new_node

        # increase the counter
        self.__increment_node_count()

    # inserting at middle (insert_before)
    def insert_before(self, before, value):
        # check if linkedlist is empty
        if self.head is None:
            raise ValueError("LinkedList is empty, use append or insert_head instead")

        # if before is head, call insert at head
        if self.head.data == before:
            self.insert_head(value)
            return

        # else
        # traverse till the before node - 1
        curr = self.head.next  # we already handled head
        while curr.next is not None:
            if curr.next.data == before:
                # create new node
                new_node = Node(value)
                new_node.next = curr.next
                curr.next = new_node
                self.__increment_node_count()
                return
            curr = curr.next

        raise ValueError(f"Value {before} does not exists in the linked list")

    # clear
    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head is None:
            return "Linkedlist is empty."

        self.head = self.head.next
        self.__decrement_node_count()

    # remove from tail
    def pop(self):
        if self.head is None:
            return "Linkedlist is empty."

        curr = self.head
        if curr.next is None:
            # linkedlist only contains head
            print(self.head.data)
            return self.delete_head()

        # traverse till tail - 1 node (second last node)
        while curr.next.next is not None:
            curr = curr.next

        # second last node
        print(curr.next.data)
        curr.next = None
        self.__decrement_node_count()

    # remove by value (remove)
    def remove(self, value):
        if self.head is None:
            raise ValueError(f"Trying to remove from empty linked list")

        if self.head.data == value:
            # remove head
            return self.delete_head()

        curr = self.head.next  # head is already handled
        # Travers till curr.next = value
        while curr.next is not None:
            if curr.next.data == value:
                # link curr.next.next to curr.next
                # this will break the connection between curr and value
                # and hence value will be removed
                curr.next = curr.next.next
                return
            curr = curr.next

        # if value does not exist
        raise ValueError(f"Value {value} does not exists in the linked list")

    # Search by value
    def search(self, value):
        index = 0
        curr = self.head

        while curr is not None:
            if curr.data == value:
                return index
            curr = curr.next
            index += 1

        return f"{value} does not exists in the linkedlist"

    # search by index
    def __getitem__(self, index):
        # TODO: Implement negative indexing
        curr = self.head
        __index = 0

        while curr is not None:
            if __index == index:
                return curr.data
            curr = curr.next
            __index += 1

        raise IndexError("Out of bound")

    # delete by index
    def __delitem__(self, key):
        # TODO: Implement negative indexing
        if self.head is None:
            raise IndexError("Trying to delete from empty linkedlist")

        if key == 0:
            # delete head
            return self.delete_head()

        curr = self.head.next
        index = 1

        while curr.next is not None:
            if index == key - 1: # key - 1 because we want to stop before index
                # link curr.next.next with curr.next
                curr.next = curr.next.next
                self.__decrement_node_count()
                return
            curr = curr.next
            index += 1

        raise IndexError("Index out of bound")