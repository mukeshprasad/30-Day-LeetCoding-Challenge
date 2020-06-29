'''
# Unique Paths

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time.
  The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

    start * * * * * * 
    *     * * * * * * 
    *     * * * * * end

# Above is a 7 x 3 grid. How many possible unique paths are there?

 
# Example 1:

  Input: m = 3, n = 2 
  Output: 3
  Explanation:
  From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
  1. Right -> Right -> Down
  2. Right -> Down -> Right
  3. Down -> Right -> Right

# Example 2:

  Input: m = 7, n = 3
  Output: 28
 

# Constraints:
  * 1 <= m, n <= 100
  * It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
'''

# SOLUTION: DP - 2D, 1D and O(1) Space 

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 2D - list
        dp = [[1 for i in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
    
        # since we are looking for only two values(right and down),
        # 2D is redudant, 1D is enough for that.
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j-1] + dp[j]
        return dp[-1]
    
        # O(1) Space - (m+n)! / (m! * n!) 
        res = 1
        j = 1
        for i in range(n, n + m - 1):
            res *= i
            res //= j
            j += 1
        return res
          
        # OR  
        if 1 in [n, m]: return 1
        return reduce(lambda x, y: x*y, range(n, n + m - 1)) // reduce(lambda x, y: x*y, range(1, m)) 
