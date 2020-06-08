'''
# Power of Two

# Given an integer, write a function to determine if it is a power of two.

# Example 1:

  Input: 1
  Output: true 
  Explanation: 2**0 = 1

# Example 2:

  Input: 16
  Output: true
  Explanation: 2**4 = 16

# Example 3:

Input: 218
Output: false
'''

# SOLUTION: Time -> O(1) <- Space - Bit Manipulation

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not(n & (n-1))
    
        # return n > 0 and n == (1 << int(math.log2(n)))
