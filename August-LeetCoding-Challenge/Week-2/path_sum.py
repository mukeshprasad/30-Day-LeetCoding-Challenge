'''
# Path Sum III

# You are given a binary tree in which each node contains an integer value.

# Find the number of paths that sum to a given value.

# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

# Example:

  root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

        10
       /  \
      5   -3
     / \    \
    3   2   11
   / \   \
  3  -2   1

  Return 3. The paths that sum to 8 are:

  1.  5 -> 3
  2.  5 -> 2 -> 1
  3. -3 -> 11
'''
# SOLUTION:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. O(N) Time and O(N) Space
class Solution(object):
    def pathSum(self, root, target):
        # define global result and path
        self.result = 0
        cache = {0:1}
        
        # recursive to get result
        self.dfs(root, target, 0, cache)
        
        # return result
        return self.result
    
    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return  
        # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        
        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one. 
        cache[currPathSum] -= 1

# 2. O(NlogN) ~ O(N^2)
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        self.count = 0
        self.dfs(root, target)
        return self.count
    
    def dfs(self, node, target):
        if not node:
            return
        self.test(node, target)
        self.dfs(node.left, target)
        self.dfs(node.right, target)
            
    def test(self, node, target):
        if not node:
            return
        if node.val == target:
            self.count += 1
        self.test(node.left, target - node.val)
        self.test(node.right, target - node.val)
