'''
# Search Insert Position

# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:
  Input: [1,3,5,6], 5
  Output: 2
  
# Example 2:
  Input: [1,3,5,6], 2
  Output: 1

# Example 3:
  Input: [1,3,5,6], 7
  Output: 4
'''

# SOLUTION: Linear, Binary Search and Python bisect Module

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)
        
        #1. Binary Search - O(logN)
        low, high = 0, len(nums) - 1
        while(low <= high):
            mid = low + (high - low)//2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return low
        
        
        #2. Linear Search - O(N)
        if target > nums[-1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return 0 if i == 0 else i
