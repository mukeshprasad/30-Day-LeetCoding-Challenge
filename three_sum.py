'''
# 3Sum

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
  Find all unique triplets in the array which gives the sum of zero.

# Note:
  The solution set must not contain duplicate triplets.

# Example:

  Given array nums = [-1, 0, 1, 2, -1, -4],

  A solution set is:
  [
    [-1, 0, 1],
    [-1, -1, 2]
  ]
'''
# SOLUTION:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 2.
        nums.sort()
        ans = set()
        for i, a in enumerate(nums[:-2]):
            if i > 0 and nums[i] == nums[i-1]: continue
            dct = {}
            for b in nums[i+1: ]:
                if b not in dct:
                    dct[-a-b] = 1
                else:
                    ans.add((a, -a-b, b))
        return map(list, ans)
        
        # 1.
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l, r = i + 1, n - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1; r -= 1
                    while l < r and nums[l] == nums[l-1]: l += 1
                    while l < r and nums[r] == nums[r+1]: r -= 1
        return res 
