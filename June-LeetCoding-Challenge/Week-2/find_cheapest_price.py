'''
# Cheapest Flights Within K Stops

# There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

# Now given all the cities and flights, together with starting city src and the destination dst,
  your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

# Example 1:
  Input: 
    n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0, dst = 2, k = 1
  Output: 200
  
# Example 2:
  Input: 
    n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0, dst = 2, k = 0
  Output: 500

# Constraints:

  * The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
  * The size of flights will be in range [0, n * (n - 1) / 2].
  * The format of each flight will be (src, dst, price).
  * The price of each flight will be in the range [1, 10000].
  * k is in the range of [0, n - 1].
  * There will not be any duplicated flights or self cycles.

'''
# SOLUTION - 1: Dijkstra's Algorithm - O(N**2 * K) Time

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        route = collections.defaultdict(dict)
        
        for a, b, p in flights:
            route[a][b] = p
        heap = [(0, src, K + 1)]
        
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in route[i]:
                    heapq.heappush(heap, (p + route[i][j], j, k - 1))
        return -1

# SOLUTION - 2: Bellman Ford - Algorithm 

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        price_table = [ float('inf') for _ in range(n) ]
        
        # price of source must be 0
        price_table[ src ] = 0
		
        # initialization with 0 transfer
        for source, destination, ticket_price in flights:
            if source == src:
                price_table[destination] = ticket_price
        
        
        # tranfer k times to update price table
        for trasfer in range(0, K):
            current_price = [*price_table]
            
            for source, destination, ticket_price in flights:
                current_price[destination] = min(current_price[destination], price_table[source] + ticket_price )
            
            # update current price back to price table    
            price_table = current_price
        
        if price_table[dst] == float('inf'):
            return -1
        else:
            return price_table[dst]


NOTE: 
  # Dijkstra’s algorithm is a Greedy algorithm and time complexity is O(VLogV).
  # Dijkstra doesn’t work for Graphs with negative weight edges, Bellman-Ford works for such graphs.
  # Bellman-Ford is also simpler than Dijkstra and suites well for distributed systems.
  # But time complexity of Bellman-Ford is O(VE), which is more than Dijkstra.
