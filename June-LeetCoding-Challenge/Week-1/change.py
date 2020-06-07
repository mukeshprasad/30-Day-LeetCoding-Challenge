'''
# Coin Change 2

# You are given coins of different denominations and a total amount of money.
  Write a function to compute the number of combinations that make up that amount.
  You may assume that you have infinite number of each kind of coin.

# Example 1:

  Input: amount = 5, coins = [1, 2, 5]
  Output: 4
  Explanation: there are four ways to make up the amount:
      5=5
      5=2+2+1
      5=2+1+1+1
      5=1+1+1+1+1

# Example 2:

  Input: amount = 3, coins = [2]
  Output: 0
  Explanation: the amount of 3 cannot be made up just with coins of 2.
'''

# SOLUTION: KnapSack Problem - O(len(coins) * amount) Time and O(N) Space

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(i, amount+1):
                if j >= i:
                    dp[j] += dp[j - i]
        return dp[-1]
