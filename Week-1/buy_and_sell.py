class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        i = 0
        valley = 0
        peak = 0
        maxprofit = 0
        while (i < size - 1):
            while (i < size - 1 and prices[i] >= prices[i + 1]):
                i+=1
            valley = prices[i];
            while (i < size - 1 and prices[i] <= prices[i + 1]):
                i+=1
            peak = prices[i]
            maxprofit += peak - valley

        return maxprofit
