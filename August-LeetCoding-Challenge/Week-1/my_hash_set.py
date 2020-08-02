'''
# Design HashSet

# Design a HashSet without using any built-in hash table libraries.

# To be specific, your design should include these functions:
    add(value): Insert a value into the HashSet. 
    contains(value) : Return whether the value exists in the HashSet or not.
    remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.


# Example:

  MyHashSet hashSet = new MyHashSet();
  hashSet.add(1);         
  hashSet.add(2);         
  hashSet.contains(1);    // returns true
  hashSet.contains(3);    // returns false (not found)
  hashSet.add(2);          
  hashSet.contains(2);    // returns true
  hashSet.remove(2);          
  hashSet.contains(2);    // returns false (already removed)


# Note:
    * All values will be in the range of [0, 1000000].
    * The number of operations will be in the range of [1, 10000].
    * Please do not use the built-in HashSet library.

'''
# SOLUTION:
class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
    
    def add(self, key):
        bucket, idx = self._index(key)
        if idx >= 0:
            return
        bucket.append(key)
        
    def remove(self, key):
        bucket, idx = self._index(key)
        if idx >= 0:
            bucket.remove(key)
            
    def contains(self, key):
        _, idx = self._index(key):
        return idx >= 0
        
    def _hash(self, key):
        return key % hash
        
    def _index(self, key):
        hash = self._hash(key)
        bucket = self.buckets[hash]
        for idx, k in enumerate(bucket):
            if k == key:
                return bucket, idx
        return bucket, -1
# OTHER

class MyHashSet:
    def __init__(self):
        self.buckets = bytearray(10 ** 6)

    def add(self, key: int) -> None:
        self.buckets[key] = 1

    def remove(self, key: int) -> None:
        self.buckets[key] = 0
            
    def contains(self, key: int) -> bool:
        return self.buckets[key] == 1
