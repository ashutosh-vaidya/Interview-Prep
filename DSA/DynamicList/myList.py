import ctypes


class MyList:

    def __init__(self):
        self.size = 1
        self.n = 0
        # Create a c type array with capacity = self.size
        self.array = self.__create_array(self.size)

    # private methods
    def __resize_array(self) -> None:
        new_capacity = self.size * 2
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
            self.__resize_array()
        self.array[self.n] = val
        self.n += 1

    # 4. print
    def __str__(self):
        # [1,2,3]:
        result = ""
        if self.n > 0:
            for i in range(self.n):
                result = result + str(self.array[i]) + ","
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

    # 8. index
    def index(self, value):
        # TODO: The optional arguments start and end
        for i in range(self.n):
            if self.array[i] == value:
                return i
        else:
            return f"ValueError: {value} is not in list"

    # 9. insert
    def insert(self, pos, value):
        # TODO: Implement negative indexing
        # check if array is at full capacity and resize it
        if self.n == self.size:
            self.__resize_array()

        # if user gives a index which is out of bound then as per list implementation make it last index
        if pos > self.n:
            pos = self.n

        if pos <= self.n:
            for i in range(self.n, pos, -1):
                self.array[i] = self.array[i - 1]

        self.array[pos] = value
        self.n = self.n + 1

    # 10. delete
    def __delitem__(self, key):
        # TODO : Negative indexing
        if key > self.n:
            # TODO: Check why this is not getting returned
            # print("here")
            return "IndexError: list assignment index out of range"

        # left shift the values from key onward by 1
        for i in range(key, self.n - 1, 1):
            self.array[i] = self.array[i + 1]

        self.n -= 1

    # 11. remove
    def remove(self, value):
        # 1. Find the index of the value
        index = self.index(value)
        if type(index) == int:
            self.__delitem__(index)
        else:
            return "ValueError: list.remove(x): x not in list"

