class Stack:

    def __init__(self):
        self.__data__ = []
        self.stack1 = []
        self.__max_size__ = 10

    def display_stack(self):
        print(self.__data__)

    def push(self, value):
        if len(self.__data__) <= self.get_max_size():
            self.__data__.append(value)
        else:
            print("Stack is full!")
            return None

    def pop(self):
        if len(self.__data__) > 0:
            return self.__data__.pop()
        else:
            print("Stack is empty.")
            return None

    def get_stack_data(self):
        return self.__data__

    def get_max_size(self):
        return self.__max_size__

    def set_max_size(self, size):
        self.__max_size__ = size

    def is_empty(self):
        if len(self.__data__) == 0:
            return True
        else:
            return False

    def is_full(self):
        if len(self.__data__) == self.get_max_size():
            return True
        else:
            return False

    def update(self, index, new_value):
        if self.is_empty() is False and len(self.get_stack_data()) > index:
            temp_stack = Stack()
            elements_at = len(self.get_stack_data()) - index + 1
            for i in range(elements_at, len(self.get_stack_data())):
                temp_stack.push(self.pop())
            self.pop()
            self.push(new_value)
            for i in range(len(temp_stack.get_stack_data())):
                self.push(temp_stack.pop())
        else:
            print("update")

    def stack_reverse(self, item):
        if self.is_empty():
            self.push(item)
        else:
            data = self.pop()
            self.stack_reverse(item)
            self.push(data)

    def reverse(self):
        if self.is_empty() is False:
            data = self.pop()
            self.reverse()
            self.stack_reverse(data)

    def sort_stack(self, data):
        if len(self.__data__) == 0 or data > self.__data__[-1]:
            self.push(data)
        else:
            temp = self.pop()
            self.sort_stack(data)
            self.push(temp)

    def sort(self):
        if len(self.__data__) != 0:
            temp = self.pop()
            self.sort()
            self.sort_stack(temp)


s = Stack()
s.push(11)
s.push(5)
s.push(10)
s.push(4)
s.update(2, 8)
print("Updated Element :",s.display_stack())
s.reverse()
print("Reversed Element :",s.display_stack())
s.sort()
print("Sorted Element :", s.display_stack())


