import ctypes


class MyList:

    def __init__(self):
        self.size = 1
        self.n = 0
        # Create a c type array with capacity = self.size
        self.array = self.__create_array(self.size)

    # private methods
    def __resize_array(self, new_capacity: int) -> None:
        new_array = self.__create_array(new_capacity)
        for i in range(self.n):
            new_array[i] = self.array[i]
        self.size = new_capacity
        self.array = new_array

    # 1. Create List
    def __create_array(self, capacity: int):
        # Creates a c type array(static, referential) with size capacity
        return (capacity * ctypes.py_object)()

    # 2. len
    def __len__(self):
        return self.n

    # 3. append
    def append(self, val):
        if self.n == self.size:
            # The list is at full capacity, resize the list
            self.__resize_array(self.size * 2)
        self.array[self.n] = val
        self.n += 1

    # 4. print
    def __str__(self):
        # [1,2,3]:
        result = ""
        if self.n > 0:
            result = [str(item) + "," for item in self.array]
            # for i in range(self.n):
            # result = result + str(self.array[i]) + ","
        return "[" + result[:-1] + "]"

    # 5. indexing
    def __getitem__(self, index):
        # TODO: implement negative indexing
        if 0 <= index < self.n:
            return self.array[index]
        else:
            return 'IndexError: list index out of range'

    # 6. pop
    def pop(self):
        if self.n == 0:
            return "IndexError: pop from empty list"
        print(self.array[self.n - 1])
        self.n -= 1

    # 7. clear
    def clear(self):
        # TODO: see if we can change the implementation or can reuse code from __init__
        self.size = 1
        self.n = 0
        # Create a c type array with capacity = self.size
        self.array = self.__create_array(self.size)

    # 8. find
    # 9. insert
    # 10. delete
    # 11. remove
