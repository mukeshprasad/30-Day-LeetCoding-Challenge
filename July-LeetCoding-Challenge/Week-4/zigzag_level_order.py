'''
# Binary Tree Zigzag Level Order Traversal

# Given a binary tree, return the zigzag level order traversal of its nodes' values. 
  (ie, from left to right, then right to left for the next level and alternate between).

# For example:
  Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

  return its zigzag level order traversal as:

  [
    [3],
    [20,9],
    [15,7]
  ]

'''
# SOLUTION:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        queue = collections.deque([root])
        order = False
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if order:
                    level = [node.val] + level # # level.insert(0, node.val)
                else:
                    level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            order = not(order)
            res.append(level)
        return res            
