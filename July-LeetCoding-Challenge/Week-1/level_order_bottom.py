'''
# Binary Tree Level Order Traversal II

# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
   
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
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
    #1. BFS + queue
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        que, res = collections.deque([(root, 0)]), []
        while que:
            node, level = que.popleft()
            if node:
                if len(res) == level:
                    res.append([])
                res[level].append(node.val)
                que.append((node.left, level+1))
                que.append((node.right, level+1))
                
        return res[::-1]
    
        # @lee215
        queue, res = [root], []
        while queue:
            res.append([node.val for node in queue if node])
            queue = [child for node in queue if node for child in (node.left, node.right)]
            
        return res[-2::-1]
        
    #2. DFS + stack
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        stack = [(root, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) == level:
                    res.append([])
                res[level].append(node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))     
        return res[::-1]
        
        
        
    #2. BFS + Queue              
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.dfs(root, 0, res)
        return res[::-1]
    
    def dfs(self, root, level, res):
        if root:
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            self.dfs(root.left, level+1, res)
            self.dfs(root.right, level+1, res)      
