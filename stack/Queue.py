class Queue:
    def __init__(self):
        self.__data__ = []
        self.__max_size__ = 10

    def display_queue(self):
        print("Queue currently contains:")
        for Item in self.__data__:
            print(Item)

    def insert(self, value):
        if len(self.__data__) <= self.__max_size__:
            self.__data__.insert(0, value)
        else:
            print("Queue is full!")

    def remove(self):
        if self.__data__ == []:
            print("Queue is empty.")
        else:
            self.__data__.pop()

    def get_max_size(self):
        return self.__max_size__

    def set_max_size(self, size):
        return self.__max_size__ == size

    def is_empty(self):
        if self.__data__ == []:
            return True
        else:
            return False

    def is_full(self):
        if len(self.__data__) == self.__max_size__:
            return True
        else:
            return False


q = Queue()
print(q.get_max_size(), "max size")
q.insert(1)
q.display_queue()
q.insert(2)
q.display_queue()
q.insert(3)
q.display_queue()
q.insert(4)
q.display_queue()
q.remove()
q.display_queue()
