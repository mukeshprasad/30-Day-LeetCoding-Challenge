'''
# Count Square Submatrices with All Ones

# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

# Example 1:
  Input: matrix =
  [
    [0,1,1,1],
    [1,1,1,1],
    [0,1,1,1]
  ]
  Output: 15
  Explanation: 
    There are 10 squares of side 1.
    There are 4 squares of side 2.
    There is  1 square of side 3.
    Total number of squares = 10 + 4 + 1 = 15.

# Example 2:
  Input: matrix = 
  [
    [1,0,1],
    [1,1,0],
    [1,1,0]
  ]
  Output: 7
  Explanation: 
    * There are 6 squares of side 1.  
    * There is 1 square of side 2. 
    * Total number of squares = 6 + 1 = 7.
'''

# SOLUTION - 1: DP Solution - O(m*n) Time and O(1) Solution

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        total = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i and j and matrix[i][j]:
                    matrix[i][j] = min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]) + 1
                total += matrix[i][j]
                
        return total

# SOLUTION - 2: Similar to above - Pythonic way!

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        total = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] *= min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]) + 1
        return sum(map(sum, matrix))
