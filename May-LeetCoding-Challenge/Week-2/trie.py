'''
# Implement Trie (Prefix Tree)

# Implement a trie with insert, search, and startsWith methods.

# Example:

  Trie trie = new Trie();

  trie.insert("apple");
  trie.search("apple");   // returns true
  trie.search("app");     // returns false
  trie.startsWith("app"); // returns true
  trie.insert("app");   
  trie.search("app");     // returns true

# Note:
  * You may assume that all inputs are consist of lowercase letters a-z.
  * All inputs are guaranteed to be non-empty strings.
  
'''
# SOLUTION - 1:
 
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False
    
class Trie:

    def __init__(self):
        self.root = TrieNode()
    
        
    def insert(self, word: str) -> None:
        current = self.root
        for ch in word:
            current = current.children[ch]
        current.is_word = True
        
    def search(self, word: str) -> bool:
        current = self.root
        for ch in word:
            current = current.children.get(ch)
            if current == None:
                return False
        return current.is_word

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for ch in prefix:
            current = current.children.get(ch)
            if current == None:
                return False
        return True

# SOLUTION - 2:

class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t['#'] = '#'

    def search(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                return False
            t = t[w]
        if '#' in t:
            return True
        return False

    def startsWith(self, prefix):
        t = self.trie
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True

# SOLUTION - 3: Easy Understandable

class TrieNode:
    def __init__(self):
        self.word=False
        self.children={}
        
class Trie(object):
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self, word):
        runner=self.root
        for char in word:
            if char not in runner.children:
                runner.children[char]=TrieNode()
            runner=runner.children[char]
        runner.word=True
        
    def search(self, word):
        runner=self.root
        for char in word:
            if char not in runner.children:
                return False
            runner=runner.children[char]
        return runner.word
        
    def startsWith(self, prefix):
        runner=self.root
        for char in prefix:
            if char not in runner.children:
                return False
            runner=runner.children[char]
        return True
        
# SOLUTION - 4: Using Sets

class Trie:

    def __init__(self):
        self.set1 = set()
        self.set2 = set()
    """
    Initialize your data structure here.
    """
    

    def insert(self, word: str) -> None:
        self.set1.add(word)
        for i in range(len(word)):
            self.set2.add(word[:i+1])
    """
    Inserts a word into the trie.
    """
    

    def search(self, word: str) -> bool:
        if word in self.set1:
            return True
        else:
            return False
    """
    Returns if the word is in the trie.
    """
    

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.set2:
            return True
        else:
            return False
    """
    Returns if there is any word in the trie that starts with the given prefix.
    """
