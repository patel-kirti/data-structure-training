class HashTable:
    def __init__(self):
        self.size =10
        self.table = list(0 for i in range(self.size))
        self.count = 0
        self.comparisons = 0

    def display(self):
        print("\n")
        for i in range(self.size):
            print(str(i) + "  -->  " + str(self.table[i]))

    def isfull(self):
        if self.count == self.size:
            return True
        else:
            return False

    def hash_func(self, key):
        return key % self.size

    def insert(self, key):
        if self.isfull():
            print("Hash table is full")
            return False
        isStored = False
        position = self.hash_func(key)
        if self.table[position] == 0:
            self.table[position] = key
            print("Element " + str(key) + " at position " + str(position))
            isStored = True
            self.count += 1
        else:
            print("Collision has occured for element " + str(key) + " at position " + str(
                position) + " finding new Position.")
            while self.table[position] != 0:
                position += 1
                if position >= self.size:
                    position = 0
            self.table[position] = key
            isStored = True
            self.count += 1
        return isStored

    def search(self, key):
        found = False
        position = self.hash_func(key)
        self.comparisons += 1
        if self.table[position] == key:
            return position
        else:
            temp = position - 1
            while position < self.size:
                if self.table[position] != key:
                    position += 1
                    self.comparisons += 1
                else:
                    return position
            position = temp
            while position >= 0:
                if self.table[position] != key:
                    position -= 1
                    self.comparisons += 1
                else:
                    return position
        if not found:
            print("Element not Found")
            return False

    def delete(self, key):
        position = self.search(key)
        if position is not False:
            self.table[position] = 0
            print("Element " + str(key) + " is Deleted")
            self.count -= 1
        else:
            print("Element is not present in the Hash Table")
        return


h = HashTable()
h.insert(10)
h.insert(26)
h.insert(20)
h.insert(25)
h.insert(21)
h.insert(81)
h.insert(4)
h.insert(9)
h.display()
print("Searching Element :-", h.search(81))
h.delete(81)
h.display()

