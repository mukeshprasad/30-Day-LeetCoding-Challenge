'''
# Same Tree

# Given two binary trees, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# Example 1:

  Input:     1         1
            / \       / \
           2   3     2   3

          [1,2,3],   [1,2,3]

  Output: true
# Example 2:

  Input:     1         1
            /           \
           2             2

         [1,2],     [1,null,2]

  Output: false
'''
# SOLUTION:
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 1. Standard Recursive
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
        
        # 2. One - Liner
        return p and q and p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) or p is q
        OR
        return p and q and p.val == q.val and all(map(self.isSameTree, (p.left, p.right), (q.left, q.right))) or p is q
        
        # 3. Tupleify
        def  t(n):
            return n and (n.val, n.left, n.right)
        return t(p) == t(q)
        
        # 4. Iterative - deque
        deq = collections.deque([(p, q)],)
        while deq:
            x, y = deq.popleft()
            if not x and not y:
                continue
            if not x or not y:
                return False
            if x.val == y.val:
                deq.append((x.left, y.left))
                deq.append((x.right, y.right))
            else:
                return False
        return True
