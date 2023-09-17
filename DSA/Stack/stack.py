from node import Node


class Stack:

    def __init__(self):
        self.top = None
        # no of items in stack
        self.n = 0

    def is_empty(self):
        return self.top is None

    def increment_stack_size(self):
        self.n += 1

    def decrement_stack_size(self):
        self.n -= 1

    def push(self, value):
        # create new node
        new_node = Node(value)
        # check if stack is not empty
        if not self.is_empty():
            new_node.next = self.top
        # set self.top as new_node
        self.top = new_node
        self.increment_stack_size()

    def pop(self):
        # check if stack is empty
        if self.is_empty():
            return "Stack is empty"

        # print the data which will be popped
        print(self.top.data)
        # move top to top.next
        self.top = self.top.next
        self.decrement_stack_size()

    def peek(self):
        # check if stack is empty
        if self.is_empty():
            return "Stack is empty"

        print(self.top.data)

    def traverse(self):
        # check if stack is empty
        if self.is_empty():
            return "Stack is empty"

        result = ""
        curr = self.top
        while curr is not None:
            result = result + str(curr.data) + "\n"
            curr = curr.next
        print(result)

    def size(self):
        return self.n

    def __len__(self):
        return self.n


