# Implement Stack using Queue..

from Queue import Queue


class StackUsingQueue:

    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.size = 10

    def display(self):
        print("Stack currently contains:")
        print(self.queue1.get_queue_data())

    def enqueue(self, value):
        while len(self.queue1.get_queue_data()) == self.queue2:
            self.queue2.enqueue(self.queue1.enqueue(value))
        self.queue1.__data__.append(value)

        while len(self.queue2.get_queue_data()) == self.queue1:
            self.queue1.enqueue(self.queue2.enqueue())

    def dequeue(self):
        if not self.queue1.get_queue_data():
            return None
        else:
            return self.queue1.dequeue()


s = StackUsingQueue()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.display()
s.dequeue()
s.display()
