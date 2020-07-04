'''
# Ugly Number II

# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

# Example:

  Input: n = 10
  Output: 12
  # Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note:  
   * 1 is typically treated as an ugly number.
   * n does not exceed 1690.
'''
# SOLUTION:

class Solution:
    # 1. It's fastest to precompute and store all possibilities for lookup,
      and it's simplest to just generate them out of order and then sort them.
    ugly = sorted(2**a * 3**b * 5**c
                  for a in range(32) for b in range(20) for c in range(14))
    
    def nthUglyNumber(self, n):
        return self.ugly[n-1]

    # 2.  
  '''
    This generates the first n ugly numbers, in order from smallest to largest, in O(n) time.
    For each prime 2, 3 and 5, have an index to the next number that can be multiplied with the prime to produce a new ugly number.
    Update the three indexes and then add the smallest of the three candidate ugly numbers.    
  '''
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]: i2 += 1
            while ugly[i3] * 3 <= ugly[-1]: i3 += 1
            while ugly[i5] * 5 <= ugly[-1]: i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))    
        return ugly[-1]
