'''
# Sum Root to Leaf Numbers

# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers.

# Note: A leaf is a node with no children.

# Example:

  Input: [1,2,3]
      1
     / \
    2   3
  
  Output: 25
  # Explanation:
    The root-to-leaf path 1->2 represents the number 12.
    The root-to-leaf path 1->3 represents the number 13.
    Therefore, sum = 12 + 13 = 25.

# Example 2:

  Input: [4,9,0,5,1]
      4
     / \
    9   0
   / \
  5   1
  
  Output: 1026
  # Explanation:
    The root-to-leaf path 4->9->5 represents the number 495.
    The root-to-leaf path 4->9->1 represents the number 491.
    The root-to-leaf path 4->0 represents the number 40.
    Therefore, sum = 495 + 491 + 40 = 1026.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #1. 358581152
    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root, 0)
    def dfs(self, root, s):
        if not root: return 0
        if not root.left and not root.right: return s*10 + root.val
        return self.dfs(root.left, s*10 + root.val) + self.dfs(root.right, s*10 + root.val)
    
    # 2.
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return int(root.val)
        
        if root.left: root.left.val = 10*root.val + root.left.val
        
        if root.right: root.right.val = 10*root.val + root.right.val
        
        
        return self.sumNumbers(root.left) + self.sumNumbers(root.right)

#     4
#    / \
#   9   0
#  / \
# 5   1
    
    # 3.
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack, res = [(root, root.val)], 0
        while stack:
            node, val = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += val
                if node.right:
                    stack.append((node.right, val*10 + node.right.val))
                if node.left:
                    stack.append((node.left, val*10 + node.left.val))
        return res
    
    # 4.
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, 0)
        return self.res
    def dfs(self, root, c):
        if root:
            print(c)
            self.dfs(root.left, c*10 + root.val)
            self.dfs(root.right, c*10 + root.val)
            if not root.left and not root.right:
                self.res += c*10 + root.val
