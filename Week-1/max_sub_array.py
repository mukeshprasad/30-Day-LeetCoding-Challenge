# Maximum Subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

## Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = -999999999999  # maxsize - 1
        curr_max = 0
        for i in nums:
            curr_max = curr_max + i
            if maximum < curr_max:
                maximum = curr_max
            if curr_max < 0:
                curr_max = 0
        return maximum
