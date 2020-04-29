'''
# Binary Tree Maximum Path Sum

# Given a non-empty binary tree, find the maximum path sum.

# For this problem:
# A path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
# The path must contain at least one node and does not need to go through the root.

## Example 1:

# Input: [1,2,3]

       1
      / \
     2   3

# Output: 6

## Example 2:

# Input: [-10,9,20,null,null,15,7]

     -10
     / \
    9  20
      /  \
     15   7

# Output: 42 (20 + 15 + 7)

'''
# SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 331822449 submission
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')

        def get_sum(root):
            if root is None:
                return 0
            else:
                ls = max(get_sum(root.left), 0)
                rs = max(get_sum(root.right), 0)
                self.max_sum = max(self.max_sum, ls + rs + root.val)
                return max(ls, rs, 0) + root.val

        get_sum(root)
        return self.max_sum
