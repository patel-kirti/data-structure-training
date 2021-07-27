class HashTable:
    def __init__(self):
        self.size = 10
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

    def quadratic_probing(self, key, position):
        found = False
        limit = 50
        i = 1
        while i <= limit:
            new_position = position + (i ** 2)
            new_position = new_position % self.size
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
            isStored, position = self.quadratic_probing(key, position)
            if isStored:
                self.table[position] = key
                self.count += 1
        return isStored

    def search(self, key):
        found = False
        position = self.hash_func(key)
        self.comparisons += 1
        if self.table[position] == key:
            return position
        else:
            limit = 50
            i = 1
            new_position = position
            while i <= limit:
                newPosition = position + (i ** 2)
                newPosition = newPosition % self.size
                self.comparisons += 1
                if self.table[position] == key:
                    found = True
                    break
                elif self.table[position] == 0:
                    found = False
                    break
                else:
                    i += 1
            if found:
                return new_position
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


h = HashTable()
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

