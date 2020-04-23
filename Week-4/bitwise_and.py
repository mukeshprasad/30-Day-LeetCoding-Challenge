# Bitwise AND of Numbers Range

# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

## Example 1:
  # Input: [5,7]
  # Output: 4
  
## Example 2:
  # Input: [0,1]
  # Output: 0
 
import math
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        c = 0
        while(m != n):
            m >>= 1
            n >>= 1
            c += 1
        return m << c

# OTHER SOLUTIONS:
# SOLUTION - 1

import math
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        return m & (-1 << (len(bin(m ^ n))-2 - int(m == n)))
        
# SOLUTION -2 

import math
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0:
            return 0
        start = int(math.log(n,2))
        end = int(math.log(m,2))
        if start != end:
            return 0

        ans = m
        for i in range(m + 1, n + 1):
            ans = ans & i
            
        return ans
