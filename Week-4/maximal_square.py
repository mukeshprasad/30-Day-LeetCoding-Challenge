'''
# Maximal Square

# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

## Example:

# Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

# Output: 4
'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 330946702 submission
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        dp = [[0 for j in range(len(matrix[0]) + 1)]
              for i in range(len(matrix) + 1)]
        size = 0

        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                if matrix[row - 1][col - 1] == '1':
                    dp[row][col] = min(
                        dp[row][col - 1], dp[row - 1][col], dp[row-1][col-1]) + 1

                if size < dp[row][col]:
                    size = dp[row][col]
        return size * size
