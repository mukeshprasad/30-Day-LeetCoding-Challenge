'''
# Maximum Sum Circular Subarray

# Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

# Here, a circular array means the end of the array connects to the beginning of the array.
  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)
# Also, a subarray may only include each element of the fixed buffer A at most once.
  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

 
# Example 1:
  Input: [1,-2,3,-2]
  Output: 3
  Explanation: Subarray [3] has maximum sum 3

# Example 2:
  Input: [5,-3,5]
  Output: 10
  Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

# Example 3:
  Input: [3,-1,2,-1]
  Output: 4
  Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
'''

# SOLUTION - 1: Kadane's Algo (Min Variant) - O(N) Time and O(1) space

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # 339715510 submission
        max_sum = -float('inf')
        min_sum = float('inf')
        curr_max = 0
        curr_min = 0
        total = 0
        for num in A:
            curr_max = max(curr_max + num, num)
            max_sum = max(max_sum, curr_max)
            curr_min = min(curr_min + num, num)
            min_sum = min(min_sum, curr_min)
            total += num
            
        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum
  
 # SOLUTION - 2: Kadane's Algo (Sign Variant) - O(N) Time and O(1) Space
  
 class Solution(object):
    def maxSubarraySumCircular(self, A):
        def kadane(gen):
            # Maximum non-empty subarray sum
            ans = cur = None
            for x in gen:
                cur = x + max(cur, 0)
                ans = max(ans, cur)
            return ans

        S = sum(A)
        ans1 = kadane(iter(A))
        ans2 = S + kadane(-A[i] for i in range(1, len(A)))
        ans3 = S + kadane(-A[i] for i in range(len(A) - 1))
        return max(ans1, ans2, ans3)
  
  # SIMILAR TO 1: Easy to Understand
  
class Solution(object):
    def maxSubarraySumCircular(self, A):
        # ans1: answer for one-interval subarray
        ans1 = cur = -float('inf')
        for x in A:
            cur = x + max(cur, 0)
            ans1 = max(ans1, cur)

        # ans2: answer for two-interval subarray, interior in A[1:]
        ans2 = cur = float('inf')
        for i in range(1, len(A)):
            cur = A[i] + min(cur, 0)
            ans2 = min(ans2, cur)
        ans2 = sum(A) - ans2

        # ans3: answer for two-interval subarray, interior in A[:-1]
        ans3 = cur = float('inf')
        for i in range(len(A)-1):
            cur = A[i] + min(cur, 0)
            ans3 = min(ans3, cur)
        ans3 = sum(A) - ans3
        
        return max(ans1, ans2, ans3)
