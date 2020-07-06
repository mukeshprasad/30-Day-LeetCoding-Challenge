'''
# Plus One

# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
  The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

  Input: [1,2,3]
  Output: [1,2,4]
  Explanation: The array represents the integer 123.

# Example 2:
  
  Input: [4,3,2,1]
  Output: [4,3,2,2]
  Explanation: The array represents the integer 4321.
'''
# SOLUTION: 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # num = ''.join(str(i) for i in digits)
        # num = int(num) + 1
        # return list(str(num))
        
        # 0.
        return list(str(int(''.join(str(i) for i in digits)) + 1))
        # 1.
        return map(int, list(str(int(''.join(map(str, digits))) + 1)))
    
        # 2. Best - Concise and Minimal
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits[0] += 1
        digits.append(0)
        return digits
        
        # 3.
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + [0] * len(digits)

        # 4.
        num = 0
        for i in range(len(digits)):
    	    num = num * 10 + digits[i]
        return [int(i) for i in str(num+1)]
        
        # 5.
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        
        i = -1
        n = len(digits)
        while n + i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1
            
        if n + i < 0: digits = [1] + digits
        else: digits[i] += 1
        return digits
