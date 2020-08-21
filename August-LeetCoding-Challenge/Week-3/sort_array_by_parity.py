'''
# Sort Array By Parity

# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
  You may return any answer array that satisfies this condition.

# Example 1:
  Input: [3,1,2,4]
  Output: [2,4,3,1]
  The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# Note:
  * 1 <= A.length <= 5000
  * 0 <= A[i] <= 5000
'''
# SOLUTION:
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # 1. O(NlogN) Time and O(N) Space
        return sorted(A, key=lambda x: x % 2)
        
        # 2. O(N) Time (2-Pass) and O(N) Space
        return ([x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1])
        
        # 3. O(N) Time and O(1) Space
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0: i += 1
            if A[j] % 2 == 1: j -= 1
            
        return A
