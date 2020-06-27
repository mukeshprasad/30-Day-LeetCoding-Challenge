'''
# Perfect Squares
# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
# Example 1:
   Input: n = 12
   Output: 3
  Explanation: 12 = 4 + 4 + 4.
# Example 2:
  Input: n = 13
  Output: 2
  Explanation: 13 = 4 + 9.
'''
# SOLUTION: 

class Solution:
    
    # 1.
    # here _dp is static, kind of cheating
    # because for every test case ran, it will be still be there

    _dp = [0]
    def numSquares(self, n: int) -> int:
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,    
        return dp[n]
        
        
    # 2.      
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')] * n
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if not (j*j <= i):
                    break
                dp[i] = min(dp[i], dp[i - j*j] + 1)
        return dp[-1]
    
   # 3. Mathematical Solution: Best of all
   
     // Based on Lagrange's Four Square theorem, there 
     // are only 4 possible results: 1, 2, 3, 4.
  
    def is_square(self, x):
        x_sq = int(math.sqrt(x))
        return x_sq * x_sq == x
        
    def numSquares(self, n: int) -> int:
        if self.is_square(n):
            return 1
            
        // The result is 4 if and only if n can be written in the 
        // form of 4^k*(8*m + 7). Please refer to 
        // Legendre's three-square theorem.
        
        while n & 3 == 0: # n%4 == 0  
            n >>= 2
            
        if n & 7 == 7:  # n%8 == 7
            return 4
        # check whether 2 is the result    
        sqrt_n = int(math.sqrt(n))
        for i in range(1, sqrt_n + 1):
            if self.is_square(n - i*i):
                return 2
        return 3
