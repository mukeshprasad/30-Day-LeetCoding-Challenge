'''
# First Unique Number
# You have a queue of integers, you need to retrieve the first unique integer in the queue.

# Implement the FirstUnique class:

# FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
# int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
# void add(int value) insert value to the queue.

# Example 1:

# Input: 
  ["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
  [[[2,3,5]],[],[5],[],[2],[],[3],[]]
# Output: 
  [null,2,null,2,null,3,null,-1]

# Explanation: 
  FirstUnique firstUnique = new FirstUnique([2,3,5]);
  firstUnique.showFirstUnique(); // return 2
  firstUnique.add(5);            // the queue is now [2,3,5,5]
  firstUnique.showFirstUnique(); // return 2
  firstUnique.add(2);            // the queue is now [2,3,5,5,2]
  firstUnique.showFirstUnique(); // return 3
  firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
  firstUnique.showFirstUnique(); // return -1

'''

# SOLUTION - 1 : O(1) showFirstUnique

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.existing = set()
        self.unique = {}
        for val in nums:
            self.add(val)

    def showFirstUnique(self) -> int:
        for val in self.unique:
            return val
        return -1

    def add(self, value: int) -> None:
        if value in self.unique:
            del self.unique[value]
            self.existing.add(value)
        elif value not in self.existing:
            self.unique[value] = True
            
# SOLUTION - 2 : O(n) showFirstUnique

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dct = {}
        self.i = 0
        for self.i in nums:
            self.dct[self.i] = self.dct.get(self.i, 0) + 1

    def showFirstUnique(self) -> int:
        for num in self.dct.keys():
            if self.dct[num] == 1:
                return num
        return -1

    def add(self, value: int) -> None:
        self.nums.append(value)
        self.dct[value] = self.dct.get(value, 0) + 1

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
