'''
# Find Minimum in Rotated Sorted Array II

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
  (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# The array may contain duplicates.

# Example 1:
  Input: [1,3,5]
  Output: 1

# Example 2:

  Input: [2,2,2,0,1]
  Output: 0
'''
# SOLUTION:
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1.
        if len(nums) == 1: return nums[0]
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] < nums[high]:
                high = mid
            else:
                high -= 1
        return nums[low]
        
        # 2.
        if len(nums) == 1: return nums[0]
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] < nums[high]:
                high = mid
            if nums[high-1] > nums[high]:
                low = mid
                break
            h -= 1
        return nums[low]
