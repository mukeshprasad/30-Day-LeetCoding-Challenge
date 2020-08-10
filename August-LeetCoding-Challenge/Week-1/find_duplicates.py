'''
# Find All Duplicates in an Array

# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Example:
  Input:
  [4,3,2,7,8,2,3,1]
  
  Output:
  [2,3]
'''
# SOLUTION:
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # O(N) Time and O(1) Space
        res = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
        return res
        
        # O(N) Time and O(1) Space
        for i in range(len(nums)):
            while i != nums[i] - 1 and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        return [i for i, num in enumerate(nums) if i != num-1]
        
        # O(N) Time and O(N) Space
        return [num for num, count in Counter(nums).items() if count == 2]
