'''
# Valid Perfect Square

# Given a positive integer num, write a function which returns True if num is a perfect square else False.
# Note:
  Do not use any built-in library function such as sqrt.

# Example 1:
   Input: 16
   Output: true
   
# Example 2:
   Input: 14
   Output: false
'''

# SOLUTION - 1: Best one - Newton's Method

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 336696703 submission
        r = num
        while r*r > num:
            r = (r + num/r) // 2
        return r*r == num
        
# SOLUTION - 2: Bitwise Trick
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
       root = 0
       bit = 1 << 15
       
       while bit > 0 :
           root |= bit
           if root > num // root:    
               root ^= bit                
           bit >>= 1        
       return root * root == num

# SOLUTION - 3: Binary Search

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        
        while left <= right:
            mid = left + (right-left)//2
            if  mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid -1
            else:
                left = mid +1
        return False
        
# SOLUTION - 4:  Math Trick for Square number is 1+3+5+ ... +(2n-1)

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while (num>0):
            num -= i
            i += 2       
        return num == 0
               
# SOLUTION - 5:

class Solution: Linear Method (Naive) - For comparison
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i ** 2 <= num:
            if i ** 2 == num:
                return True
            else:
                i += 1
        return False
    
