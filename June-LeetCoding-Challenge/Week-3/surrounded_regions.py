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
        
# SOLUTION - 2: DFS - Easy Implementation - Explanation Below:
'''
Explanation:
    
  * In this problem we need to understand, what exactly surrouned by 'X' means.
  * It actually means that if we start from 'O' at the border, and we traverse only 'O', only those 'O' are not surrouned by 'X'.
  * So the plan is the following:
    1. Start dfs or bfs from all 'O', which are on the border.
    2. When we traverse them, let us color them as 'T', temporary color.
    3. Now, when we traverse all we wanted, all colors which are not 'T' need to renamed to 'X'
      and all colors which are 'T' need to be renamed to 'O', and that is all!
  * Compexity: time complextiy is O(mn), where m and n are sizes of our board.
            Additional space complexity can also go upto O(mn) to keep stack of recursion.
''' 
class Solution:
    def dfs(self, i, j):
      if i < 0 or j < 0 or i >= self.M or j >= self.N or self.board[i][j] != "O":
          return
      self.board[i][j] = 'T'
      neib_list = [[i+1, j],[i-1, j],[i, j-1],[i, j+1]]
      for x, y in neib_list:
        self.dfs(x, y)
    
    def solve(self, board):
        if not board: return 0
        self.board, self.M, self.N = board, len(board), len(board[0])
        
        for i in range(0, self.M):
            self.dfs(i,0)
            self.dfs(i, self.N-1)
            
        for j in range(0, self.N):
            self.dfs(0,j)
            self.dfs(self.M-1 ,j)
        
        for i, j in product(range(self.M), range(self.N)):
            board[i][j] = "X" if board[i][j] != "T" else "O"


# SOLUTION - 3: BFS
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
