'''
# Maximum Width of Binary Tree

# Given a binary tree, write a function to get the maximum width of the given tree.
  The width of a tree is the maximum width among all levels.
  The binary tree has the same structure as a full binary tree, but some nodes are null.

# The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level,
  where the null nodes between the end-nodes are also counted into the length calculation.

# Example 1:

  Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

  Output: 4
  Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

# Example 2:

  Input: 

          1
         / \
        3   2 
       /        
      5      

  Output: 2
  Explanation: The maximum width existing in the second level with the length 2 (3,2).

# SOLUTION:
class  Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        '''
        That's numbering nodes (and nulls) like this:

                  1
          2               3
      4       5       6       7
    8   9   ...
        '''
        # 1.
        width = 0
        level = [(1, root)]
        while level:
            width = max(width, level[-1][0] - level[0][0] + 1)
            new_level = []
            for l, node in level:
                if node.left: new_level.append((2*l, node.left))
                if node.right: new_level.append((2*l+1, node.right))
            level = new_level
        return width
        
        # 2.
        que = [(root, 0, 0)]
        curr_depth = left = ans = 0
        for node, depth, pos in que:
            if node:
                que.append((node.left, depth+1, pos*2))
                que.append((node.right, depth+1, pos*2))
                if curr_depth != depth:
                    curr_depth = depth
                    left = pos
                ans = max(ans, pos - left + 1)
        return ans
