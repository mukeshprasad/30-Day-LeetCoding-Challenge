'''
# Largest Divisible Subset

# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
  Si % Sj = 0 or Sj % Si = 0.

# If there are multiple solutions, return any subset is fine.

# Example 1:

  Input: [1,2,3]
  Output: [1,2] (of course, [1,3] will also be ok)

# Example 2:

  Input: [1,2,4,8]
  Output: [1,2,4,8]
'''

# SOLUTION: O(N**2) - Time
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        #1. 353016795 97.2% - O(N**2)
        dct = {-1: set()}
        for x in sorted(nums):
            dct[x] = max((dct[d] for d in dct if x % d == 0), key=len) | {x}
        return list(max(dct.values(), key=len))
    
        #2. Other Solution
        n = len(nums)
        if n == 0: return []
        nums = sorted(nums)
        dp = [ [nums[i]] for i in range(n)]
        answer = [nums[0]]
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    t = dp[j] + [nums[i]]
                    if len(t) > len(dp[i]):
                        dp[i] = list(t)
                    if len(dp[i]) > len(answer):
                        answer = dp[i]
        return answer
