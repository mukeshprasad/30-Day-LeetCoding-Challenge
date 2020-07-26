 '''
# Add Digits

# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

# Example:
  Input: 38
  Output: 2 
  Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.

 '''
 # SOLUTION
 class Solution:
    def addDigits(self, num: int) -> int
        # 1. Loop - log(N) Runtime
        digital_root = 0
        while num > 0:
            digital_root += num % 10
            num = num // 10
            if num == 0 and digital_root > 9:
                num = digital_root
                digital_root = 0
        return digital_root
        
        # O(1) Runtime
        if not num: return 0
        return 9 if num % 9 == 0 else num % 9
        
        # OR
        return 1 + (num - 1) % 9 if num else 0
