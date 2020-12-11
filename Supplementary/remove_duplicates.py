'''
# Remove Duplicates from Sorted Array II

# Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
  Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.
  
'''

# SOLUTION:

# O(N) Time and O(1) Space
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        return i
        
# Follow Up:
  # Remove the duplicates in-place such that duplicates appeared at most K times and return the new length.
  
  def remove_k_duplicates(self, nums: List[int]) -> int:
      i = 0
      for n in nums:
          if i < k or n > nums[i - k]:
              nums[i] = n
              i += 1
      return i
