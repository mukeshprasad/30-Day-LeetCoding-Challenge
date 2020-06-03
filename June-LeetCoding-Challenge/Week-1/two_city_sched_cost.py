'''
# Two City Scheduling

# There are 2N people a company is planning to interview.
  The cost of flying the i-th person to city A is costs[i][0],
  and the cost of flying the i-th person to city B is costs[i][1].

# Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

# Example 1:

  Input: [[10,20],[30,200],[400,50],[30,20]]
  Output: 110
  - Explanation: 
      The first person goes to city A for a cost of 10.
      The second person goes to city A for a cost of 30.
      The third person goes to city B for a cost of 50.
      The fourth person goes to city B for a cost of 20.

  -- The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

Note:
  * 1 <= costs.length <= 100
  * It is guaranteed that costs.length is even.
  * 1 <= costs[i][0], costs[i][1] <= 1000
'''

# SOLUTION - 1: O(NlogN) Time and O(1) Space
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # 348467211 submission - 97%
        costs.sort(key=lambda x: x[0] - x[1])
        #print(costs)
        A_cost = sum([i[0] for i in costs[: len(costs)//2]])
        B_cost = sum([i[1] for i in costs[len(costs)//2: ]])
        return A_cost + B_cost
 
# SOLUTION - 2: One-liner Pythonic Way
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:   
        return sum([v[i // (len(costs)//2)] for i, v in enumerate(sorted(costs, key=lambda x: x[0] - x[1]))])


# SOLUTION - 3: Another Way to Understand the Problem
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        refund = []
        min_cost = 0
        for i,j in costs:
            refund.append(j - i)
            min_cost += i
        
        refund.sort()
        for i in range(len(costs)//2):
            min_cost += refund[i] 
        return min_cost
        
'''        
# NEAT EXPLANATION:

- Convincing ourselves that a greedy approach will work
  This problem is easier than it initially sounds (although the "easy" classification of it should be somewhat of a give away).
  For each person, we'll be paying a minimum cost regardless of which city they go to. The minimum cost is the smallest of the 2 values. So, we can then simplify by subtracting off those minimum costs. For the given example, we would subtract of 10 + 30 + 50 + 20 = 110 to change the array as follows:
  [(10, 20), (30, 200), (400, 50), (30, 20)] => [(0, 20), (0, 170), (350, 0), (10, 0)]

- So the answer will be at least 110, and then we need to work out who to send to which cities to minimise extra costs.
  For this particular example, the answer is very straightforward, as the first 2 people cost no extra to send to A,
  and the second 2 people cost no extra to send to B. So, the answer is simply 110.

-  If however we have more people who it is cheaper to send toA than to B (or vice versa),
   we need to choose which we'll pay the extra amount for. Let's say for example that we have the following array:
  [(10, 50), (50, 40), (30, 100), (10, 20), (50, 90), (40, 20)]

- To start off, with subtract the minimums, just like before.
  10 + 40 + 30 + 10 + 50 + 20 = 160

- Which leaves an array of:
  [(0, 40), (10, 0), (0, 70), (0, 10), (0, 40), (20, 0)]

- This time, we have the following 4 that are best sent to A:

  (0, 40)
  (0, 70)
  (0, 10)
  (0, 40)
  And 2 that are best sent to B:

  (10, 0)
  (20, 0)
  Because there are more in the first list though, we'll need to pick one to move into the second list,
  which will mean we have to pay the extra cost as well (the non-0 amount in the tuple).

- Hopefully it's fairly obvious that it's best to move the smallest amount, so that we have the smallest extra amount we have to pay.
  The smallest is (0, 10), so this is the one we should move.
  The total cost is therefore the minimum amount of 160 and the extra cost of 10, giving a total of 160 + 10 = 170.

- One way we could do this in code is to sort the "simplified" tuples by the first value,
  breaking any ties by sorting by the second value. This would put all of the tuples with 0 for A first,
  followed by the ones with the smallest value for non-zero value for A. Then we can send the first half to A,
  and the second half to B and we're done.
'''        
