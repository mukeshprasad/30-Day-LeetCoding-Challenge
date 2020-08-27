'''
# Sum of Left Leaves

# Find the sum of all left leaves in a given binary tree.

# Example:

    3
   / \
  9  20
    /  \
   15   7

# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''
# SOLUTION:
class Solution:
    def sum_of_left_leaves(self, root: TreeNode) -> int:
        # 1.
        if not root: return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sum_of_left_leaves(root.right)
        return self.sum_of_left_leaves(root.left) + self.sum_of_left_leaves(root.right)
        
        # 2.
        if not root: return 0
        ans = 0
        if root.left:
            if not root.left.left and not root.left.right:
                ans += root.left.val
            else:
                ans += self.sum_of_left_leaves(root.left)
        ans += self.sum_of_left_leaves(root.right)
        return ans
    
        # Easy Understanding
        self.ans = 0
        def dfs(root):
            if root:
                if root.left and not root.left.left and not root.left.right:
                    self.ans += root.left.val
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return self.ans
