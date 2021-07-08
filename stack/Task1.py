# # Implement Queue using stack...

from Stack import Stack


class QueueUsingStack:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.size = 10

    def display(self):
        print("Queue currently contains:")
        print(self.stack1.get_stack_data())

    def push(self, value):
        while len(self.stack1.get_stack_data()) != 0:
            self.stack2.push(self.stack1.pop())
        self.stack1.push(value)
        while len(self.stack2.get_stack_data()) != 0:
            self.stack1.push(self.stack2.pop())

    def pop(self):
        if len(self.stack1.get_stack_data()) == 0:
            print("Queue is empty.")
        return self.stack1.pop()

    def get_max_size(self):
        return self.size

    def set_max_size(self, size):
        return self.size == size


q = QueueUsingStack()
q.push(1)
q.push(2)
q.push(3)
q.display()
q.pop()
q.display()
