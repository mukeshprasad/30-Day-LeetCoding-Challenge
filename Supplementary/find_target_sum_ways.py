'''
# Target Sum

# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S.
  Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

# Find out how many ways to assign symbols to make sum of integers equal to target S.

# Example 1:
  Input: nums is [1, 1, 1, 1, 1], S is 3. 
  Output: 5
  * Explanation: 

    -1+1+1+1+1 = 3
    +1-1+1+1+1 = 3
    +1+1-1+1+1 = 3
    +1+1+1-1+1 = 3
    +1+1+1+1-1 = 3

  * There are 5 ways to assign symbols to make the sum of nums be target 3.
'''

# SOLUTION - 1: DP

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for x in nums:
            step = defaultdict(int)
            for y in dp:
                step[y + x] += dp[y]
                step[y - x] += dp[y]
            dp = step
        #print(dp,step)
        return dp[S]

# SOLUTION - 2: Memoization

class Solution:
    def findTargetSumWays(self, nums, S):
        index = len(nums) - 1
        curr_sum = 0
        self.memo = {}
        return self.dp(nums, S, index, curr_sum)
        
    def dp(self, nums, target, index, curr_sum):
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]
        
        if index < 0 and curr_sum == target:
            return 1
        if index < 0:
            return 0 
        
        positive = self.dp(nums, target, index-1, curr_sum + nums[index])
        negative = self.dp(nums, target, index-1, curr_sum + -nums[index])
        
        self.memo[(index, curr_sum)] = positive + negative
        return self.memo[(index, curr_sum)]
