'''
# Number Complement

# Given a positive integer, output its complement number.
  The complement strategy is to flip the bits of its binary representation.

 

# Example 1:
  Input: 5
  Output: 2
  Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

# Example 2:
  Input: 1
  Output: 0
  
# Note:
  * The given integer is guaranteed to fit within the range of a 32-bit signed integer.
  * You could assume no leading zero bit in the integer’s binary representation.
  
'''  

# SOLUTION 1: O(1) time and O(1) space

import math
class Solution:
    def findComplement(self, num: int) -> int:
        # one - liner Solution
        return num ^ ((1 << (len(bin(num)) - 2)) - 1)
        
        # OR
        if num == 0:
            return 1
        total_bits = int(math.log(num)/math.log(2)) + 1
        return ((1 << total_bits) - 1) ^ num


# SOLUTION 2:

class Solution:
    def findComplement(self, num: int) -> int:
        b = bin(num)
        ans = ""
        for i in range(2,len(b)):
            if b[i] == '1':
                ans += '0'
            else:
                ans += '1'
        return int(ans, 2)
