'''
# Best Time to Buy and Sell Stock with Cooldown

# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit.
  You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
  After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

# Example:

  Input: [1,2,3,0,2]
  Output: 3 
  Explanation: transactions = [buy, sell, cooldown, buy, sell]

'''
# SOLUTION: - O(N) time and O(1) space
class Solution:
    def maxProfit(self, prices: int) -> int:
        free = 0
        have = cool = float('-inf')
        for p in prices:
            free, have, cool = max(free, cool), max(have, free - p), have + p
        return max(free, cool)
        '''
        free is the maximum profit I can have while being free to buy.
        have is the maximum profit I can have while having stock.
        cool is the maximum profit I can have while cooling down.
        '''
