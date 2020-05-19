'''
# Online Stock Span

# Write a class StockSpanner which collects daily price quotes for some stock,
  and returns the span of that stock's price for the current day.

# The span of the stock's price today is defined as the maximum number of consecutive days
  (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

# For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85],
  then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

# Example 1:

  Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
  Output: [null,1,1,1,2,1,4,6]
  Explanation: 
    First, S = StockSpanner() is initialized.  Then:
    S.next(100) is called and returns 1,
    S.next(80) is called and returns 1,
    S.next(60) is called and returns 1,
    S.next(70) is called and returns 2,
    S.next(60) is called and returns 1,
    S.next(75) is called and returns 4,
    S.next(85) is called and returns 6.

  # Note that (for example) S.next(75) returned 4, because the last 4 prices
    (including today's price of 75) were less than or equal to today's price.    
'''
 # SOLUTION - Monotonic Stack(either increasing or decreasing) - O(Q) Time - Q: No of queries to StockSpanner.next - O(Q) Space
 
 class StockSpanner:
    # 341726780 submission
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append([price, span])
        return span
        
        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

'''
# EXPLANATION:
1.Initialize a stack [ ].
2.Add or append every [price , span] to the stack.
3.Initialize a span variable to 1.
4.Loop: When price of the current price is equal or greater than that of the stack's last price, we add its span and then pop it .
5.Append the [price, span] to the stack
6.Return span variable.
  Time Complexity: O(q) - q is number of queries to call StockSpanner.next
  Similarly, O(q) Space
'''
