'''
# Power of Four

# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example 1:

  Input: 16
  Output: true

# Example 2:

  Input: 5
  Output: false

# Follow up: Could you solve it without loops/recursion?
'''
# SOLUTION:
class Solution:
    def isPowerOfFour(self num: int) -> bool:
        # 1. O(1)
        return num > 0 and num & (num - 1) == 0 and num % 0x55555555 == num
        
        # 2. O(logn)
        return num > 0 and 4 ** int(math.log(num, 2) == num
        
        # 3. O(1)
        return num > 0 and math.log(num, 2) % 2 == .0
        '''
        Check Explanation Here: https://leetcode.com/problems/power-of-four/discuss/80461/Python-one-line-solution-with-explanations
        '''
