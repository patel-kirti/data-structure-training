class Hashing:
    def __init__(self):
        self.hashmap = [[] for i in range(10)]

    def insert(self, key, value):
        hash_key = hash(key) % len(self.hashmap)
        key_exists = False
        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

    def search(self, key):
        hash_key = hash(key) % len(self.hashmap)
        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v

    def display(self):
        for i in range(len(self.hashmap)):
            print(i, end=' ')
            for j in self.hashmap[i]:
                print("-->", end=' ')
                print(j, end=' ')
            print()

    def delete(self, key):
        hash_key = hash(key) % len(self.hashmap)
        key_exists = False
        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            del bucket[i]
            print('Key {} deleted'.format(key))
        else:
            print('Key {} not found'.format(key))


h = Hashing()
h.insert(10, 'A')
h.insert(26, 'B')
h.insert(20, 'C')
h.insert(25, 'D')
h.insert(21, 'E')
h.insert(81, 'F')
h.insert(4, 'G')
h.insert(9, 'H')
h.display()
print("Searching node :-", h.search(81))
h.delete(4)
h.display()
