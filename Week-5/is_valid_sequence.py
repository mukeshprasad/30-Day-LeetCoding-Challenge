'''
# Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree

# Given a binary tree where each path going from the root to any leaf form a valid sequence,
  check if a given string is a valid sequence in such binary tree.

# We get the given string from the concatenation of an array of integers arr and
  the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.

# Example 1:
               0
            /     \
           1       0
         /   \    /
        0     1   0
        \    / \
         1  0   0

    Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
    Output: true
    Explanation:
    The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure).
    Other valid sequences are:
    0 -> 1 -> 1 -> 0
    0 -> 0 -> 0
'''
# SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        # 332263725 submission
        def helper(root, arr, index):
            if (root == None) or (index == len(arr)):
                return False
            if (root.left == None) and (root.right == None) and \
                        (root.val == arr[index]) and (index == len(arr) - 1):
                return True

            return root.val == arr[index] and (helper(root.left, arr, index + 1) \
                                               or helper(root.right, arr, index + 1))

        return helper(root, arr ,0)