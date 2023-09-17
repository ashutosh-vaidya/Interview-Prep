class Stack_A:

    def __init__(self):
        self.__top = -1
        self.__stack = []

    def is_empty(self):
        return self.__top == -1

    def push(self, value):
        self.__stack.append(value)
        self.__top += 1

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return

        self.peek()
        del [self.__stack[self.__top]]
        self.__top -= 1

    def peek(self):
        if self.is_empty():
            print("Stack is empty")

        print(self.__stack[self.__top])

    def size(self):
        return len(self.__stack)

    def traverse(self):
        if self.is_empty():
            print("Stack is empty")

        for i in self.__stack[::-1]:
            print(i)

    def __len__(self):
        return  len(self.__stack)