# Contiguous Array

# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

## Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

## Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50,000.

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0:-1}
        cdf = 0
        res = 0
        for i, num in enumerate(nums):
            if num == 1:
                cdf += 1
            if num == 0:
                cdf -= 1
            if cdf in d:
                res = max(res, i - d[cdf])
            else:
                d[cdf] = i
        return res
