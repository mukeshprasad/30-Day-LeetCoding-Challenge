'''
# Subsets

# Given a set of distinct integers, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.

# Example:
  Input: nums = [1,2,3]
  Output:
  [
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
  ]
'''
# SOLUTION:
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 1. Cascading
        subs = [[]]
        for num in nums:
            subs += [curr + [num] for curr in subs]
        return subs
    
        # 2. Backtracking
        def backtrack(first = 0, curr = []):
            if len(curr) == k:
                subs.append(curr[:])
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()
                
        subs = []
        n = len(nums)
        for i in range(n+1):
            backtrack()
        return subs
        
        # 3. Lexicographic (Binary Sorted) Subsets
        n = len(nums)
        output = []
        
        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            
            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
        return output
