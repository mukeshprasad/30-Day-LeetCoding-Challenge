'''
# Course Schedule II

# There are a total of n courses you have to take, labeled from 0 to n-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

# Example 1:

  Input: 2, [[1,0]] 
  Output: [0,1]
  Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
# Example 2:

  Input: 4, [[1,0],[2,0],[3,1],[3,2]]
  Output: [0,1,2,3] or [0,2,1,3]
  Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
'''
# SOLUTION: 1. https://en.wikipedia.org/wiki/Topological_sorting#Algorithms
            Kahn's Algorithm  

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1.
        indegree = [0] * numCourses
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            indegree[i] += 1
            neigh[j].add(i)
        stack = [i for i in range(numCourses) if indegree[i] == 0]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for i in neigh[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    stack.append(i)
        if sum(indegree) == 0: return []
        else: return res
        
        # 2.
        pre, suc = defaultdict(int), defaultdict(list)
        for a, b in prerequisites:
            pre[a] += 1
            suc[b].append(a)
        free = set(range(numCourses)) - set(pre)
        out = []
        while free:
            a = free.pop()
            out.append(a)
            for b in suc[a]:
                pre[b] -= 1
                pre[b] or free.add(b)
        return out * (len(out) == numCourses)            
