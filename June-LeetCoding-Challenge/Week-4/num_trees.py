'''
# Unique Binary Search Trees

# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

# Example:

  Input: 3
  Output: 5

# Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

# SOLUTION: DP
class Solution:
    def numTrees(self, n: int) -> int:
        # return math.factorial(2*n)//(math.factorial(n+1) * math.factorial(n))
        
        # dp
        t = [0] * (n+1)
        t[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                t[i] += t[j] * t[i-j-1]
        return t[n]
     
# SOLUTION: Catalan Number - O(N) Time
class Solution:
    def numTrees(self, n: int) -> int:
        return math.factorial(2*n)//(math.factorial(n+1) * math.factorial(n))
