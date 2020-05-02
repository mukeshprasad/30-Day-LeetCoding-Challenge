'''
# Jewels and Stones

# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are letters.
  Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example 1:
  Input: J = "aA", S = "aAAbbbb"
  Output: 3

# Example 2:
  Input: J = "z", S = "ZZ"
  Output: 0
  
# Note:
  S and J will consist of letters and have length at most 50.
  The characters in J are distinct.
 
'''
# SOLUTION 1 : O(N) time and O(N) space

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # 333147523 submission
        count = 0
        dct = {}
        for i in J:
            dct[i] = 1
        for i in S:
            if dct.get(i) != None:
                count += 1
        return count
        
# SOLUTION 2 : O(J*S) time and O(1) space

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # 333143598 submission
        count = 0
        for i in J:
            count += S.count(i)
        return count
        
# SOLUTION 3 : one liner

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum([S.count(i) for i in J])
