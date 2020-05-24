'''
# Construct Binary Search Tree from Preorder Traversal

# Return the root node of a binary search tree that matches the given preorder traversal.
 
# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val,
  and any descendant of node.right has a value > node.val.
  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

# It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

# Example 1:
  Input: [8,5,1,7,10,12]
  Output: [8,5,10,1,7,null,12]
  
         8
        / \
       5  10
      / \   \ 
     1   7   12

# Constraints:
  * 1 <= preorder.length <= 100
  * 1 <= preorder[i] <= 10^8
  * The values of preorder are distinct.
'''

# SOLUTION - 1: O(N) Time - The Best You can get!!
'''
  EXPLANATION : 
      * Give the function a bound the maximum number it will handle.
      * The left recursion will take the elements smaller than node.val
      * The right recursion will take the remaining elements smaller than bound

  # Complexity
      * bstFromPreorder is called exactly N times.
      * It's same as a preorder traversal.
      * Time: O(N)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 343998511 submission
    i = 0
    def bstFromPreorder(self, preorder: List[int], bound=float('inf')) -> TreeNode:
        if self.i == len(preorder) or preorder[self.i] > bound:
            return None
        root = TreeNode(preorder[self.i])
        self.i += 1
        root.left = self.bstFromPreorder(preorder, root.val)
        root.right = self.bstFromPreorder(preorder, bound)
        return root

'''
# INTUITION for 2nd and 3rd Solution:
    * Find the left part and right part,
    * then recursively construct the tree.
'''

# SOLUTION - 2: O(NlogN) Time - Binary Search

def bstFromPreorder(self, A):
        def helper(i, j):
            if i == j: return None
            root = TreeNode(A[i])
            mid = bisect.bisect(A, A[i], i + 1, j)
            root.left = helper(i + 1, mid)
            root.right = helper(mid, j)
            return root
        return helper(0, len(A))
        
# SOLUTION - 3: O(N^2) Time

def bstFromPreorder(self, A):
        if not A: return None
        root = TreeNode(A[0])
        i = bisect.bisect(A, A[0])
        root.left = self.bstFromPreorder(A[1:i])
        root.right = self.bstFromPreorder(A[i:])
        return root
