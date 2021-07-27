class HashTable:
    def __init__(self):
        self.size = 12
        self.num = 5
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

    def h1(self, key):
        return key % self.size

    def h2(self, key):
        return key % self.num

    def double_hashing(self, key, position):
        found = False
        limit = 50
        i = 2
        while i <= limit:
            new_position = (i * self.h1(key) + self.h2(key)) % self.size
            if self.table[new_position] == 0:
                found = True
                break
            else:
                i += 1
        return found, new_position

    def insert(self, key):
        if self.isfull():
            print("Hash table is full")
            return False
        found = False
        position = self.h1(key)
        if self.table[position] == 0:
            self.table[position] = key
            print("Element " + str(key) + " at position " + str(position))
            found = True
            self.count += 1
        else:
            while not found:
                print("Collision has occured for element " + str(key) + " at position " + str(
                    position) + " finding new Position.")
                found, position = self.double_hashing(key, position)
                if found:
                    self.table[position] = key
                    self.count += 1
        return found

    def search(self, key):
        found = False
        position = self.h1(key)
        self.comparisons += 1
        if self.table[position] == key:
            return position
        else:
            limit = 50
            i = 1
            new_position = position
            while i <= limit:
                position = (i * self.h1(key) + self.h2(key)) % self.size
                self.comparisons+=1
                if self.table[position] == key:
                    found = True
                    break
                elif self.table[position] == 0:
                    found = False
                    break
                else:
                    i += 1
            if found:
                return position
            else:
                print("Not Found Element.")
                return found

    def delete(self, key):
        position = self.search(key)
        if position is not False:
            self.table[position] = 0
            print("Element " + str(key) + " is Deleted")
            self.count -= 1
        else:
            print("Element is not present in the Hash Table")
        return


h=HashTable()
h.insert(12)
h.insert(26)
h.insert(31)
h.insert(17)
h.insert(90)
h.insert(28)
h.insert(88)
h.insert(40)
h.insert(77)
h.display()
print("Searching Element :-", h.search(26))
h.delete(26)
h.display()
