class HashTable:
    
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size


    def put(self, key, data):
        hash_val = self.hash_function(key)
        if self.slots[hash_val] is None:
            self.slots[hash_val] = key
            self.data[hash_val] = data
        elif self.slots[hash_val] == key:
            self.data[hash_val] = data
        else:
            while self.slots[hash_val] is not None and self.slots[hash_val] != key:
                hash_val = self.rehash(hash_val) # infinite loop if table is full
            if self.slots[hash_val] is None:
                self.slots[hash_val] = key
            self.data[hash_val] = data

    def get(self, key):
        start_slot = self.hash_function(key)
        hash_val = self.hash_function(key)
        while self.slots[hash_val] is not None and self.slots[hash_val] != key:
            hash_val = self.rehash(hash_val)
            if hash_val == start_slot:
                return None
        return self.data[hash_val]


table = HashTable()
table.put(0, 'zero')
table.put(1, 'one')
table.put(2, 'two')
table.put(3, 'three')
table.put(4, 'four')
table.put(5, 'five')
table.put(6, 'six')
table.put(7, 'seven')
table.put(8, 'eight')
table.put(9, 'nine')
table.put(10, 'ten')
table.put(11, 'eleven')
print(table.slots)
print(table.data)
print(table.get(0))
