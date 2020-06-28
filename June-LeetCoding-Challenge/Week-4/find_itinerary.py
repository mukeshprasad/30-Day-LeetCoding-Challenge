'''
# Reconstruct Itinerary

# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order.
  All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

# Note:

# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.
For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
  All airports are represented by three capital letters (IATA code).
  You may assume all tickets form at least one valid itinerary.
  One must use all the tickets once and only once.
  
# Example 1:

  Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
  Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

# Example 2:

  Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
  Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
  Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
               But it is larger in lexical order.
'''

# SOLUTION: Eulerian Path + Greedy DFS
class Solution:
    # Eulerian Path. Greedy DFS, building the route backwards when retreating.
    '''
    Eulerian Path:   
              An Eulerian trail (or Eulerian path) is a trail in a finite graph
              that visits every edge exactly once (allowing for revisiting vertices)
    '''
    
    # Recursive
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = collections.defaultdict(int)
        for src, dst in sorted(tickets)[::-1]:
            targets[src].append(dst)
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]
        
    # Iterative    
    def findItinerary(self, tickets: List[List[str]]) -> List(str):
        targets = collections.defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            targets[src].append(dst)
        route, stack = [], ['JFK']
        while stack:
            while targets[stack[-1]]:
                x = targets[stack[-1]].pop()
                stack.append(x)
            route.append(stack.pop())
        return route[::-1]            
