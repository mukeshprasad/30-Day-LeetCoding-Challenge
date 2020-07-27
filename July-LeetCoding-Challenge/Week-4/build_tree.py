'''
# Construct Binary Tree from Inorder and Postorder Traversal

# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note:
  You may assume that duplicates do not exist in the tree.

# For example, given

  inorder = [9,3,15,20,7]
  postorder = [9,15,7,20,3]

  Return the following binary tree:

      3
     / \
    9  20
      /  \
     15   7

'''
# SOLUTION:
# Definition of a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#           self.val = val
#           self.left = left
#           self.right = right
          
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 0. O(N^2) Time
        if not inorder or not postorder:
            return
        node = TreeNode(postorder.pop())
        idx = inorder.index(node.val)
        node.right = self.buildTree(inorder[idx+1:], postorder)
        node.left = self.buildTree(inorder[:idx], postorder)
        return node
        
        # 1. O(N) Time and O(N) Space
        mp = {v: i for i, v in enumerate(inorder)}
        def build(low, high, p):
            if low > high: return
            node = TreeNode(postorder[p[0]])
            idx = mp[node.val]
            node.right = build(idx+1, high, p)
            node.left = build(low, idx-1, p)
            return node
        return build(0, len(inorder)-1, [len(inorder) - 1])
        
        # 2. O(N) Time and O(N) Space
        d = {v: i for i, v in enumerate(inorder)}
        def build(low, high):
            if low > high: return
            node = TreeNode(postorder.pop())
            mid = d[node.val]
            node.right = build(mid+1, high)
            node.left = build(low, mid-1)
            return node
        return build(0, len(inorder)-1)
