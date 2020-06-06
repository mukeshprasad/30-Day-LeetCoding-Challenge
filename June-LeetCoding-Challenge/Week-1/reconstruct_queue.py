'''
# Queue Reconstruction by Height

# Suppose you have a random list of people standing in a queue.
  - Each person is described by a pair of integers (h, k), where h is the height of the person
    and k is the number of people in front of this person who have a height greater than or equal to h.
  - Write an algorithm to reconstruct the queue.

# Note:
  The number of people is less than 1,100.
 
# Example
    Input:
      [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

    Output:
      [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''

SOLUTION - 1: O(NlogN) - Time
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # O(NlogN) 349785007 submission
        people.sort(key=lambda x: (x[0], -x[1]))
        tmp = [i for i in range(len(people))]
        ans = [[]] * len(people)
        
        for i, (h, k) in enumerate(people):
            x = tmp.pop(k)
            ans[x] = people[i]
        
        return ans
        
# SOLUTION - 2: O(N**2) - Time
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda tmp: [-tmp[0], tmp[1]])
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue
        
        

Explanation:

Intuition: First, let's find the final position of data paire (h_min, k), in which h_min is the smallest height,
            k is the number of people in front of this data.
We can see that, all the other data pairs' height is not less than this one(since h_min is the smallest height).
So its final position should be k + 1-th.
if it's not in k + 1-th position, let's say k + 1 + 1-th position, the value should not be k (k + 1 + 1-th position,
the data pair should be (h_min, k + 1)).

Then, let's the the second minimum data pair.
Since all the minimum value are well positioned, and those minimum data pairs are meanless to the second minimum values' k.
So what we should do? We just need to put the k value to the k + 1-th positions which are empty.
And do the same procedure to the rest data.

For example,

Input: [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Sorted: [[4, 4], [5, 0], [5, 2], [6, 1], [7, 0], [7, 1]]

1. [None, None, None, None, [4, 4], None]
2. [[5, 0], None, None, None, [4, 4], None]
3. [[5, 0], None, [5, 2], None, [4, 4], None]
4. [[5, 0], None, [5, 2], [6, 1], [4, 4], None]
5. [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], None]
6. [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
