# Number of Islands

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

'''
## Example 1:
    Input:
    11110
    11010
    11000
    00000

    Output: 1


## Example 2:

    Input:
    11000
    11000
    00100
    00011

  Output: 3
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) < 1:
            return 0

        def dfs(r, c):
            if r<0 or c<0 or r>rows-1 or c>cols-1 or grid[r][c]=='0':
                return
            grid[r][c] = '0'


            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0

        for r in range(rows):
            for c in range(cols):
                cell = grid[r][c]

                if cell == '0':
                    continue

                if cell == '1':
                    num_islands += 1
                    dfs(r, c)

        return num_islands