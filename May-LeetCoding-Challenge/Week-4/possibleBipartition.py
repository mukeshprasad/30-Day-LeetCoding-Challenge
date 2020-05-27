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
