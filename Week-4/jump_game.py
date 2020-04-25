# Jump Game

# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

## Example 1:

  # Input: [2,3,1,1,4]
  # Output: true
  # Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
## Example 2:

  # Input: [3,2,1,0,4]
  # Output: false
  # Explanation: You will always arrive at index 3 no matter what. Its maximum
               jump length is 0, which makes it impossible to reach the last index.

# SOLUTION - 1

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        prev_pos = len(nums) - 1
        for i in range(prev_pos, -1, -1):
            if i + nums[i] >= prev_pos:
                prev_pos = i
        return prev_pos == 0
        
# SOLUTION - 2

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        high = 0
        for i in range(len(nums)-1):
            if i > high:
                return False
            else:
                if i+nums[i] >= len(nums)-1:
                    return True
                if i+nums[i] > high:
                    high = i+nums[i]
        return False
