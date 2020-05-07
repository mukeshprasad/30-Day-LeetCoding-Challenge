'''
# Cousins in Binary Tree

# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
  Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

# Return true if and only if the nodes corresponding to the values x and y are cousins.

# Example:  
            1
           / \
          2   3
         /
        4
  Input: root = [1,2,3,4], x = 4, y = 3
  Output: false
  
'''
# SOLUTION - 1:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # 335726391 submission
        def helper(node, i, p, num):
            if node:
                if node.val == num:
                    return i, p
                return helper(node.left, i+1, node.val, num) or helper(node.right, i+1, node.val, num)

        dx, px, dy, py = helper(root, 0, None, x) + helper(root, 0, None, y)
        return dx == dy and px != py
        
# SOLUTION - 2:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        dct = {}
        def helper(node, i=0, parent_node=None):
            if node == None:
                return
            dct[node.val] = (i, parent_node)
            helper(node.left, i+1, node.val)
            helper(node.right, i+1, node.val)
        
        helper(root)
        return dct[x][0] == dct[y][0] and dct[x][1] != dct[y][1]
