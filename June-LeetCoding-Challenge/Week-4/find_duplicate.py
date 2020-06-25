'''
# Find the Duplicate Number

# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
  prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

# Example 1:

  Input: [1,3,4,2,2]
  Output: 2

# Example 2:

  Input: [3,1,3,4,2]
  Output: 3

# Note:

  * You must not modify the array (assume the array is read only).
  * You must use only constant, O(1) extra space.
  * Your runtime complexity should be less than O(n2).
  * There is only one duplicate number in the array, but it could be repeated more than once.
'''
# SOLUTION: 
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
    
        #1. Floyd's Tortoise and Hare (Cycle Detection) - Linked List - II
        # O(N) Time and O(1) Space both
        
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
                
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare
        
        #2. sorting - O(NlogN) Time and O(N) Space
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]


        #3. set - O(N) both
        s = set()
        for i in nums:
            if i in s:
                return i
            s.add(i)
        
        
    
        #4. O(N^2) Time and O(N) Space
        return Counter(nums).most_common(1)[0][0]
