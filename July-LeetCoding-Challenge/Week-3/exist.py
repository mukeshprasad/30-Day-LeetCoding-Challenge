'''
# Word Search

# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example:

  board =
  [
   ['A','B','C','E'],
   ['S','F','C','S'],
   ['A','D','E','E']
  ]

  Given word = "ABCCED", return true.
  Given word = "SEE", return true.
  Given word = "ABCB", return false.

# Constraints:
    * board and word consists only of lowercase and uppercase English letters.
    * 1 <= board.length <= 200
    * 1 <= board[i].length <= 200
    * 1 <= word.length <= 10^3
'''
# SOLUTION:
class Solution:
    def exist(self, board: List[List[int]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(board, i, j, pos):
            if pos == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[pos]:
                return False
            tmp = board[i][j]
            board[i][j] = '#'
            res = dfs(board, i, j-1, pos+1) or \
                  dfs(board, i, j+1, pos+1) or \
                  dfs(board, i-1, j, pos+1) or \
                  dfs(board, i+1, j, pos+1)
            board[i][j] = tmp
            return res
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(board, i, j, 0):
                    return True
        return False
        
        ## 2
#         def exist(self, board, word):
#             if not board:
#                 return False
#             for i in range(len(board)):
#                 for j in range(len(board[0])):
#                     if self.dfs(board, i, j, word):
#                         return True
#             return False

          # check whether can find word, start at (i,j) position    
#         def dfs(self, board, i, j, word):
#             if len(word) == 0: # all the characters are checked
#                 return True
#             if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
#                 return False
#             tmp = board[i][j]  # first character is found, check the remaining part
#             board[i][j] = "#"  # avoid visit agian 
#             # check whether can find "word" along one direction
#             res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
#             or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
#             board[i][j] = tmp
#             return res                
