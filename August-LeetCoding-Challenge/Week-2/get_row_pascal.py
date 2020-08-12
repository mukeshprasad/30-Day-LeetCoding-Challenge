'''
# Pascal's Triangle II

# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

# Note that the row index starts from 0.

# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

  Input: 3
  Output: [1,3,3,1]

# Follow up:
    Could you optimize your algorithm to use only O(k) extra space?
'''
# SOLUTION:
class Solution:
    def getRowFromPascalTriangle(self, rowIndex: int) -> self:
        # Time -> O(k) <- Space k: rowIndex
        '''
        For example, rowIndex = 6. row items are as follows:
        1st: 1=1
        2nd: 6= 6 / 1
        3rd: 15=6x5 / (1x2)
        4th: 20=6x5x4 / (1x2x3)
        5th: 15=6x5x4x3 / (1x2x3x4)
        6th: 6 =6x5x4x3x2 / (1x2x3x4x5)
        7th: 1 =6x5x4x3x2x1 / (1x2x3x4x5x6)
        '''        
        row = [1]
        t, b = k, 1
        curr = 1
        for i in range(1, k+1):
            curr = curr * t
            curr = curr // b
            row.append(curr)
            t -= 1; b += 1
        return row
        
        # O(k) Space
        row = [1] * (k+1)
        for i in range(2, k+1):
            for j in range(1, i):
                row[i-j] += row[i-j-1]
        return row
        
        # O(k^2) Space
        pascal = [[0 for i in range(k+1)] for i in range(k+1)]
        pascal[0][0] = 1
        for i in range(1, k+1):
            pascal[i][0] = 1
            for j in range(1, k+1):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal[k]
