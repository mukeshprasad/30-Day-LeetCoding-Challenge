'''
# Contiguous Array

# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
  Input: [0,1]
  Output: 2
  Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

# Example 2:
  Input: [0,1,0]
  Output: 2
  Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

# Note: The length of the given binary array will not exceed 50,000.
'''

# SOLUTION - 1: Brute-Force - Time Limit Exceeded(TLE) - O(N^2) Time and O(1) Space

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxlen = 0;
        for start in range(len(nums)):
            zeroes = 0
            ones = 0
            for end in range(start, len(nums)):
                if nums[end] == 0:
                    zeroes += 1
                else:
                    ones += 1
                if (zeroes == ones):
                    maxlen = max(maxlen, end - start + 1)
            
        return maxlen
        
# SOLUTION - 2: Using HashMap - O(N) Time and Space

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0:-1}
        count = 0
        res = 0
        for i, num in enumerate(nums):
            count = count + (1 if num == 1 else -1)
            if count in d:
                res = max(res, i - d[count])
            else:
                d[count] = i
        return res
'''       
 # Complexity Analysis
  * Time complexity : O(N). The entire array is traversed only once.
  * Space complexity : O(N). Maximum size of the HashMap map will be n, if all the elements are either 1 or 0.
'''
