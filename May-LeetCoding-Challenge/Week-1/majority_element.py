'''
# Majority Element
Solution
# Given an array of size n, find the majority element.
  The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:
  Input: [3,2,3]
  Output: 3
# Example 2:
  Input: [2,2,1,1,1,2,2]
  Output: 2
'''

# SOLUTION - 1: Boyer-Moore Voting - O(N) time, O(1) space

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ele = nums[0]
        for num in nums:
            if count == 0:
                ele = num
            count += (1 if ele == num else -1)
        return ele
        
# SOLUTION - 2: Using Hashmap - O(N) time and space

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dct = Counter(nums)
        for key in dct:
            if dct[key] > (len(nums) // 2):
                return key
