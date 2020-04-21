'''
# Leftmost Column with at Least a One

(This problem is an interactive problem.)

# A binary matrix means that all elements are 0 or 1.
# For each individual row of the matrix, this row is sorted in non-decreasing order.

# Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it.
# If such index doesn't exist, return -1.

# You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

  # BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
  # BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
  
# Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.
# Also, any solutions that attempt to circumvent the judge will result in disqualification.



# Explanation to the solution:
  # Using the information that the rows are sorted, if we start searching from the right top corner(1st row, last column)
  # and every time when we get a 1, as the row is sorted in non-decreasing order,
  # there is a chance of getting 1 in the left column, so go to previous column in the same row.
  # And if we get 0, there is no chance that in that row we can find a 1, so go to next row. Here is the implementation:
  
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

'''

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        M, N = binaryMatrix.dimensions()

        r, c = 0, N - 1
        leftmost_col = -1
        while r < M and c >= 0:
            if binaryMatrix.get(r, c) == 1:
                leftmost_col = c
                c -= 1
            else:
                r += 1
        return leftmost_col

 
