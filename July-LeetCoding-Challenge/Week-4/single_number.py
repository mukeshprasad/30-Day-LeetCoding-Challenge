'''
# Single Number III

# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice.
  Find the two elements that appear only once.

# Example:

  Input:  [1,2,1,3,2,5]
  Output: [3,5]

# Note:

  1. The order of the result is not important. So in the above example, [5, 3] is also correct.
  2. Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

'''
# SOLUTION:
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # O(1) Space
        x = functools.reduce(xor, nums)
        nz = x & (x-1) ^ x
        num1 = reduce(xor, filter(lambda n: n & nz, nums))
        return [num1 ^ x, num1]
        
        # O(1) Space
        # https://leetcode.com/problems/single-number-iii/discuss/68900/Accepted-C%2B%2BJava-O(n)-time-O(1)-space-Easy-Solution-with-Detail-Explanations
        x = functools.reduce(xor, nums)
        x &= -x
        res = [0, 0]
        for num in nums:
            if num & x == 0: res[0] ^= num
            else: res[1] ^= num
        return res
        
        # O(N) Space
        return [key for key, value in Counter(nums).items() if value == 1]
        
