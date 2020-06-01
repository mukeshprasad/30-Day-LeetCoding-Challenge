'''
# Invert Binary Tree

# Invert a binary tree.

# Example:
  Input:

         4
       /   \
      2     7
     / \   / \
    1   3 6   9
  Output:

         4
       /   \
      7     2
     / \   / \
    9   6 3   1

# Trivia:
  * This problem was inspired by this original tweet by Max Howell:
    - Google: 90% of our engineers use the software you wrote (Homebrew),
              but you can’t invert a binary tree on a whiteboard so f*** off.
'''

# SOLUTION - 1: Recursive - O(N) Time and Space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
    '''         
    # making it readable
        if root:
            temp=root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(temp)
            return root        
    ''' 
 
# SOLUTION - 2: Iterative - DFS - O(N) Time and Space

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = [root]
        while stack:
            node = stack.pop()
            print(node)
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.left, node.right])         
        return root
        
# SOLUTION - 3: Iterative - BFS - O(N) Time and Space

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # BFS - Iterative
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root
