class Stack:
    def __init__(self):
        self.data = []
        self.size = 10
    def DisplayStack(self):
        print("Stack currently contains:")
        for Item in self.data:
            print(Item)

    def Push(self,value):
        if len(self.data) <= self.size:
            self.data.append(value)
        else:
            print("Stack is full!")

    def Pop(self):
        if len(self.data) > 0:
            self.data.pop()
        else:
            print("Stack is empty.")
s=Stack()
s.Push(1)
s.DisplayStack()
s.Push(2)
s.DisplayStack()
s.Pop()
s.DisplayStack()


