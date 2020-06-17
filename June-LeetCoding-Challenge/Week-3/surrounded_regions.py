'''
# Surrounded Regions

# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example:

  X X X X
  X O O X
  X X O X
  X O X X

After running your function, the board should be:

  X X X X
  X X X X
  X X X X
  X O X X

Explanation:
    Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'.
    Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
    Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''

# SOLUTION - Faster

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == []: return
        m, n = len(board), len(board[0])
        sv = [ij for k in range(max(m, n)) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))]
        
        while sv:
            i, j = sv.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                sv += (i, j-1), (i, j+1), (i-1, j), (i+1, j)
        
        board[:] = [['XO'[x == 'S'] for x in row] for row in board]
        
        
# SOLUTION - 2: BFS
    def solve(self, board: List[List[str]]) -> None:
        queue = collections.deque([])
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r in [0, len(board)-1] or c in [0, len(board[0])-1]) and board[r][c] == "O":
                    queue.append((r, c))
                    
        while queue:
            r, c = queue.popleft()
            if 0 <= r< len(board) and 0 <= c <len(board[0]) and board[r][c] == "O":
                board[r][c] = "D"
                queue.append((r-1, c)); queue.append((r+1, c))
                queue.append((r, c-1)); queue.append((r, c+1))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "D":
                    board[r][c] = "O"
