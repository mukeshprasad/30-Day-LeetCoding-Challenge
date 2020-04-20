# Construct Binary Search Tree from Preorder Traversal

# Return the root node of a binary search tree that matches the given preorder traversal.

# (Recall that a binary search tree is a binary tree where for every node,
# any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val. 
# Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

## Example 1:

# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]

'''
         8
        / \
       5  10
      / \   \ 
     1   7   12

'''

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return

        root = TreeNode(preorder[0])

        def insert(val, root):

            while True:

                if root.val > val:

                    if root.left == None:
                        root.left = TreeNode(val)
                        break

                    else:
                        root = root.left

                else:
                    if root.right == None:
                        root.right = TreeNode(val)
                        break
                    else:
                        root = root.right

        head = root
        for i in preorder[1:]:

            head = root
            insert(i, head)

        return head
