'''
# Word Search II

# Given a 2D board and a list of words from the dictionary, find all words in the board.

# Each word must be constructed from letters of sequentially adjacent cell,
  where "adjacent" cells are those horizontally or vertically neighboring.
  The same letter cell may not be used more than once in a word.

# Example:
   Input: 
    board = [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
  words = ["oath","pea","eat","rain"]

  Output: ["eat","oath"]
 
# Note:

  * All inputs are consist of lowercase letters a-z.
  * The values of words are distinct.
'''
# SOLUTION - 1: 
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:  
        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node[None] = True
            
        board = {i + 1j*j: c
                 for i, row in enumerate(board)
                 for j, c in enumerate(row)}
        
        found = []
        def search(node, z, word):
            if node.pop(None, None):
                found.append(word)
            c = board.get(z)
            if c in node:
                board[z] = None
                for k in range(4):
                    search(node[c], z + 1j**k, word + c)
                board[z] = c
                
        for z in board:
            search(root, z, '')

        return found


# SOLUTION - 2:

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
                
    def insert(self, word):
        current = self.root
        for ch in word:
            current = current.children[ch]
        current.is_word = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:  
        trie = Trie()   
        node = trie.root
        for i in words:
            trie.insert(i)
        
        res = []    
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, '', res)
        return res
    
    def dfs(self, board, node, i, j, path, res):
        if node.is_word:
            res.append(path)
            node.is_word = False
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = '#'
        self.dfs(board, node, i-1, j, path+tmp, res)
        self.dfs(board, node, i+1, j, path+tmp, res)
        self.dfs(board, node, i, j-1, path+tmp, res)        
        self.dfs(board, node, i, j+1, path+tmp, res)
        board[i][j] = tmp    
        
        
        
       
                  
