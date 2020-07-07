'''
# Island Perimeter

# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally).
  The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
  One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

# Example:

# Input:
    [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]

# Output: 16

'''
# SOLUTION:
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 1. Pythonic Way - Since there are no lakes,
        #   every pair of neighbour cells with different values is part of the perimeter (more precisely, the edge between them is).
        #   So just count the differing pairs, both horizontally and vertically (for the latter I simply transpose the grid).
          
        return sum(sum(map(operator.ne, [0] + row, row + [0])) for row in grid + list(map(list, zip(*grid))))
        
        # Little Expansion of the above:
        c = 0
        t_grid = list(map(list, zip(*grid)))    # transpose of the thr grid
        for row in grid + t_grid:
            c += sum(map(operator.ne, [0] + row, row + [0]))
        return c
        
        # 2.
        '''
        the description of this problem implies there may be an "pattern" in calculating the perimeter of the islands.
        and the pattern is islands * 4 - neighbours * 2, since every adjacent islands made two sides disappeared(as picture below).

          +--+     +--+                   +--+--+
          |  |  +  |  |          ->       |     |
          +--+     +--+                   +--+--+
          4 + 4 - ? = 6  -> ? = 2
        '''
        m, n = len(grid), len(grid[0])
        islands, neigh = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    islands += 1
                    if i < m - 1 and grid[i+1][j] == 1: neigh += 1
                    if j < n - 1 and grid[i][j+1] == 1: neigh += 1
        return islands * 4 - neigh * 2
        
        # 3. Simple Approach
        m, n = len(grid), len(grid[0])
        p = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] == 0: p += 1
                    if i == m-1 or grid[i+1][j] == 0: p += 1
                    if j == 0 or grid[i][j-1] == 0: p += 1
                    if j == n-1 or grid[i][j+1] == 0: p += 1
        return p
