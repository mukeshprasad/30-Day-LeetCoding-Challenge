'''
# Count Complete Tree Nodes

# Given a complete binary tree, count the number of nodes.

# Note:

  * Definition of a complete binary tree from Wikipedia:
        In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
        It can have between 1 and 2h nodes inclusive at the last level h.

# Example:

  Input: 
      1
     / \
    2   3
   / \  /
  4  5 6

  Output: 6
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# SOLUTION: Time - O((logN)^2)

# O((logN)^2)
class Solution:
    def height(self, root):
            return -1 if root == None else 1 + self.height(root.left) 
        
    def countNodes(self, root: TreeNode) -> int:
        h = self.height(root)
        return 0 if h < 0 else \
                            (1 << h) + self.countNodes(root.right) if self.height(root.right) == (h-1) else \
                            (1 << h-1) + self.countNodes(root.left)
                            
# SOLUTION: O(N)
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # O(N) - Linear Recursive
        if root == None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
'''
# Explanation:

# The height of a tree can be found by just going left. Let a single node tree have height 0. Find the height h of the whole tree.
  If the whole tree is empty, i.e., has height -1, there are 0 nodes.

# Otherwise check whether the height of the right subtree is just one less than that of the whole tree, meaning left and right subtree have the same height.

# If yes, then the last node on the last tree row is in the right subtree and the left subtree is a full tree of height h-1.
  So we take the 2^h-1 nodes of the left subtree plus the 1 root node plus recursively the number of nodes in the right subtree.
  
# If no, then the last node on the last tree row is in the left subtree and the right subtree is a full tree of height h-2.
  So we take the 2^(h-1)-1 nodes of the right subtree plus the 1 root node plus recursively the number of nodes in the left subtree.
  
# Since I halve the tree in every recursive step, I have O(log(n)) steps. Finding a height costs O(log(n)). So overall O(log(n)^2).

Check This:

class Solution {
    int height(TreeNode root) {
        return root == null ? -1 : 1 + height(root.left);
    }
    public int countNodes(TreeNode root) {
        int h = height(root);
        return h < 0 ? 0 :
               height(root.right) == h-1 ? (1 << h) + countNodes(root.right)
                                         : (1 << h-1) + countNodes(root.left);
    }
}
'''
