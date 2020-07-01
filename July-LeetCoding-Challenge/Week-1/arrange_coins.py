'''
# Arranging Coins

# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

# Given n, find the total number of full staircase rows that can be formed.

# n is a non-negative integer and fits within the range of a 32-bit signed integer.

# Example 1:
  n = 5
  The coins can form the following rows:
  ¤
  ¤ ¤
  ¤ ¤

  Because the 3rd row is incomplete, we return 2.

# Example 2:
  n = 8
  The coins can form the following rows:
  ¤
  ¤ ¤
  ¤ ¤ ¤
  ¤ ¤

  Because the 4th row is incomplete, we return 3.
'''
# SOLUTION:
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # 1. Time -> O(1) <- Space
        return int((2*n + 0.25)**0.5 - 0.5)
        
        # 2. Binary Search - O(logN) - Time and O(1) - Space
        low, high = 0, n
        while low <= high:
            k = (low + high)//2
            curr = k * (k + 1)//2
            if curr == n:
                return k
            if n < curr:
                high = k - 1
            else:
                low = k + 1
        return high                
