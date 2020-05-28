'''
# Counting Bits

# Given a non negative integer number num.
  For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

# Example 1:
  Input: 2
  Output: [0,1,1]

# Example 2:
  Input: 5
  Output: [0,1,1,2,1,2]

# Follow up:
  * It is very easy to come up with a solution with run time O(n*sizeof(integer)).
    But can you do it in linear time O(n) /possibly in a single pass?
  * Space complexity should be O(n).
  * Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''
# SOLUTION -1: O(N) Time and Space - Boss's Solution

class Solution:
    def countBits(self, num: int) -> List[int]:
        # Boss's Solution - 345832436
        res = [0] * (num + 1)
        for i in range(1, num + 1): res[i] = res[i >> 1] + (i & 1)
        return res
        
        # (i >> 1) <=> (i // 2)
        # (i & 1) <=> (i % 2)
        
# More: O(N) Time and Space

class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num+1)
        offset = 1
        for i in range(1, num+1):
            if offset * 2 == i:
                offset *= 2
            res[i] = res[i - offset] + 1
        return res
        
# General Way - Time Complexity: O(n*sizeof(integer))

class Solution:
    def countBits(self, num: int) -> List[int]:
        lst = []
        for i in range(num + 1):
            lst.append(bin(i).count('1'))
        return(lst)       
