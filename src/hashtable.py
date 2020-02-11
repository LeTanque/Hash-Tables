# '''
# Linked List hash table key/value pair
# '''
# Collision is when two entries in a hash table have the
# same key(?)
# We use indices 0 and 1 because it's a tuple


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            print(f"WARN: Collision has occured at index {index}")
        else:
            self.storage[index] = (key, value)
        return

    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            if self.storage[index][0] == key:
                self.storage[index] = None
            else:
                print(f"WARN: Collision has occured at index {index}")
        else:
            print(f"WARN: Key {key} not found")
        return

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Store key:val so user on retrieve can know duplicate index
        '''
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            if self.storage[index][0] == key:
                return self.storage[index][1]
            else:
                print(f"WARN: Collision has occured at index {index}")
        else:
            return None
        return

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        '''
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        for item in old_storage:
            self.insert(item[0], item[1])



if __name__ == "__main__":
    ht1 = HashTable(1)
    ht1.insert("key1", "Hello")
    ht1.insert("halo", "Goodbye")

    print(ht1.storage)

    # ht = HashTable(2)

    # ht.insert("line_1", "Tiny hash table")
    # ht.insert("line_2", "Filled beyond capacity")
    # ht.insert("line_3", "Linked list saves the day!")

    # print("")

    # # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print("")
