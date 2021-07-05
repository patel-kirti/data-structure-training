class Queue:
    def __init__(self):
        self.data = []
        self.size = 10

    def DisplayQueue(self):
        print("Queue currently contains:")
        for Item in self.data:
            print(Item)

    def Push(self, value):
        if len(self.data) <= self.size:
            self.data.insert(0,value)
        else:
            print("Queue is full!")

    def Pop(self):
        if self.data == []:
            print("Queue is empty.")
        else:
            self.data.pop()


q = Queue()
q.Push(1)
q.DisplayQueue()
q.Push(2)
q.DisplayQueue()
q.Push(3)
q.DisplayQueue()
q.Push(4)
q.DisplayQueue()
q.Pop()
q.Pop()
q.DisplayQueue()
