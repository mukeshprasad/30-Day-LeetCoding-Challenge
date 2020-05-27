'''
# Possible Bipartition
# Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
# Each person may dislike some other people, and they should not go into the same group. 
# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
# Return true if and only if it is possible to split everyone into two groups in this way.
# Example 1:
  Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
  Output: true
  Explanation: group1 [1,4], group2 [2,3]
# Example 2:
  Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
  Output: false
# Example 3:
  Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
  Output: false
'''
# Also Check the Solution(Explanation) at the Bottom
# SOLUTION - 1: Depth-First Search - Bipartition
'''
  Complexity Analysis:
  * Time Complexity: O(N + E), where EE is the length of dislikes.
  * Space Complexity: O(N + E).
'''
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        neighbor_list = [[] for _ in range(N)]
        for dislike in dislikes:
            
            neighbor_list[dislike[0] - 1].append(dislike[1] - 1)
            neighbor_list[dislike[1] - 1].append(dislike[0] - 1)
        
        def isOddCyclic(curr, parent, path, path_len, visited):
            visited[curr] = True
            
            path[curr] = path_len
            
            for neighbor in neighbor_list[curr]:
                if not visited[neighbor]:
                    if isOddCyclic(neighbor, curr, path, path_len + 1, visited):
                        return True
                    
                elif neighbor != parent:
                    if neighbor in path and (path_len - path[neighbor]) % 2 == 0:
                        return True
                    
            path.pop(curr)
            return False
            
        path = {}
        visited = [False] * N
        for i in range(N):
            if not visited[i] and isOddCyclic(i, -1, path, 0, visited):
                return False
            
        return True            

# A bit Pythonic Way:

class Solution(object):
    def possibleBipartition(self, N, dislikes):
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        print(graph)
        color = {}
        def dfs(node, c = 0):
            if node in color:
                return color[node] == c
            color[node] = c
            print(color)
            return all(dfs(nei, c ^ 1) for nei in graph[node])
        
        
        return all(dfs(node)
                   for node in range(1, N+1)
                   if node not in color)
      
      
'''  
# This is classical graph theory problem:
  you have graph,
      and you need to check if it can be bipartitioned:
        all nodes must be divided into two groups, such that there is not connections between nodes in each group.
# Classical way to solve this problem is any graph traversal algorithm, here I chose dfs.
# The variable self.adj_list is adjacency list of our graph, for example if we have connections
    [[1,2],[2,3],[3,4],[4,5],[1,5]], then it is equal to 1:{2,5}; 2:{1,3}, 3:{4,2}, 4:{3,5}, 5:{1,4}
    
# I also have self.found_loop variable to terminate early if we found loop with odd length,
  which is sufficient and necessary condition that graph can not be bipartitioned,
  for example in our case we have 1->2->3->4->5->1 the loop with size 5.
# When we traverse nodes, we evaluate their distances (in my code list self.dist) from the starting point,
  and if in some moment node is already visited and its parity is broken, than we found odd loop.
# Note also, that original graph is not necessarily connected,
  and we need to start our dfs from all nodes to make sure that we traverse all graph.
# Complexity We traverse every connection between nodes only once, so we have classical O(E+V) time complexity,
  where E is number of edges and V is number of vertices (V = N in our case and V = len(dislikes)).
  Space complexity is also O(E+V), because we keep adjacency list for all our nodes and colors
'''
class Solution:
    def dfs(self, start):
        if self.found_loop == 1: return        #early stop if we found odd cycle
    
        for neib in self.adj_list[start]:
            if self.dist[neib] > 0 and (self.dist[neib] - self.dist[start]) %2 == 0:
                self.found_loop = 1
            elif self.dist[neib] < 0:  #not visited yet
                self.dist[neib] = self.dist[start] + 1
                self.dfs(neib)
            
    def possibleBipartition(self, N, dislikes):
        self.adj_list = defaultdict(list)
        self.found_loop, self.dist = 0, [-1] *(N+1)
        
        for i,j in dislikes:
            self.adj_list[i].append(j)
            self.adj_list[j].append(i)
        
        for i in range(N):
            if self.found_loop: return False    #early stop if we found odd cycle
            
            if self.dist[i] == -1:    #not visited yet
                self.dist[i] = 0
                self.dfs(i)
        
        return True
