'''
# Single Element in a Sorted Array

# You are given a sorted array consisting of only integers where every element appears exactly twice,
  except for one element which appears exactly once. Find this single element that appears only once.

# Example 1:
  Input: [1,1,2,3,3,4,4,8,8]
  Output: 2
  
# Example 2:
  Input: [3,3,7,7,10,11,11]
  Output: 10
 
# Note: Your solution should run in O(log n) time and O(1) space.
'''

# SOLUTION - 1: O(NlogN) time and O(1) space

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while(low < high):
            mid = low + (high - low)//2
            temp = mid ^ 1  # if mid odd then mid - 1; if even mid + 1
            if nums[mid] == nums[temp]:
                low = mid + 1
            else:
                high = mid
        return nums[low]

# SOLUTION - 2: O(N) time and O(1) space

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # 338286491 submission
        ans = nums[0]
        for i in nums[1:]:
            ans ^= i
        return ans

# SOLUTION - 3: Similar to SOLUTION - 1

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while(low < high):
            mid = (low + high)//2
            if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                low = mid + 1
            else:
                high = mid
        return nums[low
