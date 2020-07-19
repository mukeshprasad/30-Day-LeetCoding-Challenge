'''
# Add Binary

# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:

  Input: a = "11", b = "1"
  Output: "100"

# Example 2:
  
  Input: a = "1010", b = "1011"
  Output: "10101"
 
# Constraints:
  * Each string consists only of '0' or '1' characters.
  * 1 <= a.length, b.length <= 10^4
  * Each string is either "0" or doesn't contain any leading zero.
'''
# SOLUTION:
class Solution:
    def addBinary(self, a: str, b: str) -> str
        # 1. Iterative
        res, carry = '', 0
        a, b = list(a), list(b)
        while a or b or carry:
            if a: carry += int(a.pop())
            if b: carry += int(b.pop())
            res = str(carry % 2) + res
            carry //= 2
        return res
        
    
        # 2. Recursive
        if len(a)==0: return b
        if len(b)==0: return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1],b[0:-1])+'0'
        else:
            return self.addBinary(a[0:-1],b[0:-1])+'1'
        
        # 3. Iterative
        m, n = len(a) - 1, len(b) - 1
        res, carry = '', 0
        while m >= 0 or n >= 0 or carry:
            t = (m >= 0 and a[m] == '1') + (n >= 0 and b[n] == '1')
            carry, rem = divmod(t + carry, 2)
            res = str(rem) + res
            m -= 1; n -= 1
        return res
        
        # 4. One-liner
        return bin(int(a, 2) + int(b , 2))[2:]
                
