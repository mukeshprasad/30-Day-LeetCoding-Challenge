'''
# Flood Fill

# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor,
  "flood fill" the image.

# To perform a "flood fill", consider the starting pixel,
  plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel,
  plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on.
  Replace the color of all of the aforementioned pixels with the newColor.

# At the end, return the modified image.

# Example 1:
  * Input: 
        image = [[1,1,1],[1,1,0],[1,0,1]]
        sr = 1, sc = 1, newColor = 2
  * Output: 
        [[2,2,2],[2,2,0],[2,0,1]]
  * Explanation: 
        From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
        by a path of the same color as the starting pixel are colored with the new color.
        Note the bottom corner is not colored 2, because it is not 4-directionally connected
        to the starting pixel.
'''
'''
Implementation:
  # Simply perform a DFS on the source cell. Continue the DFS if:
    * Next cell is within bounds.
    * Next cell is the same color as source cell.
  
  # There is a tricky case where the new color is the same as the original color and if the DFS is done on it,
    there will be an infinite loop.
  # If new color is same as original color, there is nothing to be done and we can simply return the image.
'''

# SOLUTION : O(N) time and O(N) space

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        source_color = image[sr][sc]
        # [i][j], [i-1][j] up, [i][j+1] right, [i+1][j] down, [i][j-1]
        # 337817431 submission
        def helper(i, j):
            if not((0 <= i < rows and 0 <= j < cols)) or image[i][j] != source_color:
                return
            
            image[i][j] = newColor
            [helper(i + x, j + y) for (x, y) in ((0, 1), (1, 0), (0, -1), (-1, 0))]   # A little pythonic way
            # General:
            # helper(i+1,j)
            # helper(i-1,j)
            # helper(i,j+1)
            # helper(i,j-1)
            
        if source_color != newColor:      
            helper(sr,sc)
        return image
