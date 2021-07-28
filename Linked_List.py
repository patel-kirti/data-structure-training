# Implementing Linked_List...


class Element:
    def __init__(self, data=None, next=None, prv=None):
        self.data = data
        self.next = next


class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newdata = Element(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newdata
        else:
            self.head = newdata

    def print_data(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def delete(self, index):
        index_id = 1
        current_data = self.head
        prv_data = None

        while current_data is not None:
            if index_id == index:
                if prv_data is not None:
                    prv_data.next = current_data.next
                else:
                    self.head = current_data.next
                    return
            prv_data = current_data
            current_data = current_data.next
            index_id = index_id + 1

    def update(self, old, new):
        index = 0
        if self.head is None:
            return
        current = self.head
        while current.next != None:
            if current.data == old:
                current.data = new
            current = current.next
            index = index + 1

    def reverse(self):
        prv = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prv
            prv = current
            current = next
        self.head = prv

    def sort(self):
        current = self.head
        index = 0
        if self.head == None:
            return
        else:
            while current != None:
                index = current.next
                while index != None:
                    if current.data > index.data:
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next


l = Linked_List()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
l.insert(5)
l.print_data()
print("Deleted element in Linled List")
l.delete(2)
l.print_data()
print("Updated Data in Linled List")
l.update(4, 40)
l.print_data()
print("Reverse Linled List")
l.reverse()
l.print_data()
print("Sorting Linled List")
l.sort()
l.print_data()
