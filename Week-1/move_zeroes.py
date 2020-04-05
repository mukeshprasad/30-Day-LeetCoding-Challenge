# Move Zeroes

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

## Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Note:
# 1. You must do this in-place without making a copy of the array.
# 2. Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        next = 0
        for i in nums:
            if i != 0:
                nums[next] = i
                next += 1

        for i in range(next, len(nums)):
            nums[i] = 0

        print(nums)
