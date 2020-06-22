'''
# Single Number II

# Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

# Note:
  Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:
  Input: [2,2,3,2]
  Output: 3

# Example 2:
  Input: [0,1,0,1,0,1,99]
  Output: 99
'''

* CHECK: https://leetcode.com/problems/single-number-ii/discuss/43294/Challenge-me-thx
        including comments
       
# SOLUTION: Constant Space
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = twos = 0
        for i in nums:
            ones = (ones ^ i) & ~twos
            twos = (twos ^ i) & ~ones         
        
        return ones  

# SOLUTION: Extra Space
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for key, value in Counter(nums).items():
            if value == 1:
                return key
