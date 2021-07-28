class Queue:
    def __init__(self):
        self.__data__ = []
        self.__max_size__ = 10

    def display_queue(self):
        print(self.__data__)

    def enqueue(self, value):
        if len(self.__data__) <= self.__max_size__:
            self.__data__.insert(0, value)
        else:
            print("Queue is full!")

    def dequeue(self):
        if not self.__data__:
            print("Queue is empty.")
        else:
            return self.__data__.pop(0)

    def get_queue_data(self):
        return self.__data__

    def get_max_size(self):
        return self.__max_size__

    def set_max_size(self, size):
        return self.__max_size__ == size

    def is_empty(self):
        if not self.__data__:
            return True
        else:
            return False

    def is_full(self):
        if len(self.__data__) == self.__max_size__:
            return True
        else:
            return False

    def update(self, index, new_value):
        if self.is_empty() is False and len(self.get_queue_data()) >= index:
            temp_queue = Queue()
            elements_at = len(self.get_queue_data()) - index % 2
            for i in range(elements_at, len(self.get_queue_data())):
                temp_queue.enqueue(self.dequeue())
            self.dequeue()
            self.enqueue(new_value)
            for i in range(len(temp_queue.get_queue_data())):
                self.enqueue(temp_queue.dequeue())
                # self.dequeue()
        else:
            print("update")

    def reverse(self):
        if not self.is_empty():
            temp = self.dequeue()
            self.reverse()
            self.enqueue(temp)

    def sort_queue(self, data):
        if len(self.__data__) == 0 or data <= self.__data__[0]:
            self.enqueue(data)
        else:
            temp = self.dequeue()
            self.sort_queue(data)
            self.enqueue(temp)
            # self.dequeue()

    def sort(self):
        if len(self.__data__) != 0:
            temp = self.dequeue()
            self.sort()
            self.sort_queue(temp)



q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(8)
q.enqueue(40)
q.enqueue(5)
q.display_queue()
q.update(3, 10)
q.display_queue()
q.reverse()
q.display_queue()
q.sort()
q.display_queue()
