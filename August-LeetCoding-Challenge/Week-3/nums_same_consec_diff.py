'''
# Numbers With Same Consecutive Differences

# Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

# Note that every number in the answer must not have leading zeros except for the number 0 itself.
  For example, 01 has one leading zero and is invalid, but 0 is valid.

# You may return the answer in any order.
 
# Example 1:
  Input: N = 3, K = 7
  Output: [181,292,707,818,929]
  Explanation: Note that 070 is not a valid number, because it has leading zeroes.

# Example 2:
  Input: N = 2, K = 1
  Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 
# Note:
  * 1 <= N <= 9
  * 0 <= K <= 9
'''
# SOLUTION:
class Solution:
    def nums_same_consec_diff(self, N: int, K: int) -> List[int]:
        # BFS
        ans = range(10) # [0, 1, 2, ... , 9]
        for _ in range(N - 1):
            tmp = set() # to avoid duplicates
            for x in curr:
                y = x % 10 # find last digit of x
                if x > 0 and y + K < 10:
                    tmp.add(x * 10 + y + K)
                if x > 0 and y - K >= 0:
                    tmp.add(x * 10 + y - K)
            ans = tmp
        return ans
        
        # More Pythonic
        cur = range(10)
        for i in range(N - 1):
            cur = {x * 10 + y for x in cur for y in [x % 10 + K, x % 10 - K] if x and 0 <= y < 10}
        return list(cur)

        # DFS
        if N == 1:
            return [i for i in range(10)]

        ans = []
        def DFS(N, num):
            # base case
            if N == 0:
                return ans.append(num)

            tail_digit = num % 10
            # using set() to avoid duplicates when K == 0
            next_digits = set([tail_digit + K, tail_digit - K])

            for next_digit in next_digits:
                if 0 <= next_digit < 10: 
                    new_num = num * 10 + next_digit
                    DFS(N-1, new_num)

        for num in range(1, 10):
            DFS(N-1, num)

        return list(ans)        
