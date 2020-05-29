'''
# Course Schedule

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

# Some courses may have prerequisites,
  for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# Example 1:
  Input: numCourses = 2, prerequisites = [[1,0]]
  Output: true
  Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

# Example 2:
  Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
  Output: false
  Explanation: There are a total of 2 courses to take. 
                To take course 1 you should have finished course 0, and to take course 0 you should
                also have finished course 1. So it is impossible.
 

# Constraints:
  * The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
  * You may assume that there are no duplicate edges in the input prerequisites.
  * 1 <= numCourses <= 10^5
'''
class Solution:
    # 346253255 submission
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        degree = [0]*numCourses 
        for j, i in prerequisites:
            graph[i].append(j)
            degree[j] += 1
        bfs = [i for i in range(numCourses) if degree[i] == 0]
        #print(bfs)
        for i in bfs:
            for j in graph[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        return len(bfs) == numCourses
