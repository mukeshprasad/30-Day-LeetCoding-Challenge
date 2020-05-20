'''
# Kth Smallest Element in a BST

# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# Note:
  You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Example 1:
  Input: root = [3,1,4,null,2], k = 1
       3
      / \
     1   4
      \
       2
  Output: 1

# Example 2:
  Input: root = [5,3,6,2,4,null,null,1], k = 3
         5
        / \
       3   6
      / \
     2   4
    /
   1
  Output: 3
# Follow up:
  What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
  How would you optimize the kthSmallest routine?
'''

# SOLUTION - 1: Iteration - O(H+k) Time and O(H+k) Space - where H: Height of BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int: 
        # 342205250 submission
        lst = []
        while True:
            while root:
                lst.append(root)
                root = root.left
            root = lst.pop()    
            k -= 1
            if not k:
                return root.val
            root = root.right
            
 
# SOLUTION - 2: Recursion - O(N) Time and O(N) Space 

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int: 
        lst = []
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            lst.append(root.val)
            dfs(root.right)
        dfs(root)
        return lst[k-1] or 0
