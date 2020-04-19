# Search in Rotated Sorted Array

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.
# Your algorithm's runtime complexity must be in the order of O(log n).

## Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

## Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        O(n)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
        '''

        # O(log(n))
        if len(nums) < 1:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        low = 0
        high = len(nums) - 1
        while(low < high):
            if(nums[low] == target):
                return low
            if(nums[high] == target):
                return high
            pivot = (low+high)//2
            if nums[pivot] == target:
                return pivot

            if (nums[low] < nums[pivot]):

                if (target > nums[pivot] or target < nums[low]):
                    low = pivot + 1
                else:
                    high = pivot - 1

            else:
                if (target < nums[pivot] or target > nums[high]):
                    high = pivot - 1
                else:
                    low = pivot + 1

        return -1
