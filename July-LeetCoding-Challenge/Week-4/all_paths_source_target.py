'''
# All Paths From Source to Target

# Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

# Example:
  Input: [[1,2], [3], [3], []] 
  Output: [[0,1,3],[0,2,3]] 
  Explanation: The graph looks like this:
  0--->1
  |    |
  v    v
  2--->3
  There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

# Note:
   * The number of nodes in the graph will be in the range [2, 15].
   * You can print different paths in any order, but you should keep the order of nodes inside one path.

'''
# SOLUTION:
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # RECURSIVE
        def dfs(curr, path);
            if curr == n-1:
                paths.append(path)
            else:
                for v in graph[curr]:
                    dfs(v, path + [v])
                    
        n = len(graph)
        paths = []
        dfs(0, [0])
        return paths
        
        # ITERATIVE
        n = len(graph)
        path = [[0]]
        paths = []
        while path:
            curr_path = path.pop()
            for v in graph[curr_path[-1]]:
                if v == n-1:
                    paths.append(curr_path + [v])
                else:
                    path.append(curr_path + [v])
        return paths
