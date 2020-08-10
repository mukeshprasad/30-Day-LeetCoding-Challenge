'''
# Vertical Order Traversal of a Binary Tree

# Given a binary tree, return the vertical order traversal of its nodes values.

# For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

# Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes,
  we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

# If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

# Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

 
# Example 1:
      3
     / \
    9  20
      /  \
     15   7

  Input: [3,9,20,null,null,15,7]
  Output: [[9],[3,15],[20],[7]]
  Explanation: 
    Without loss of generality, we can assume the root node is at position (0, 0):
    Then, the node with value 9 occurs at position (-1, -1);
    The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
    The node with value 20 occurs at position (1, -1);
    The node with value 7 occurs at position (2, -2).
'''
# SOLUTION:
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # ITERATIVE
        g = collections.defaultdict(list)
        queue = [(root, 0)]
        while queue:
            new = []
            d = collections.defaultdict(list)
            for node, s in queue:
                d[s].append(node.val)
                if node.left: new += (node.val, s-1),
                if node.right: new += (node.val, s+1),
            for i in d:
                g[i].extend(sorted(d[i))
            queue = new
          return [g[i] for i in sorted(g)]
          
        # Recursive
        dct = defaultdict(list)
        
        def traverse(node, x, y):
            if not node: 
                return      
            dct[x].append((y, node.val))
            traverse(node.left, x - 1, y + 1)
            traverse(node.right, x + 1, y + 1)
        
        traverse(root, 0, 0)
        heap, ans = [], []
        
        for x, lst in dct.items():
            heappush(heap, (x, sorted(lst)))
        
        while heap:
            ans.append([v for _, v in heappop(heap)[1]])
        
        return ans          
