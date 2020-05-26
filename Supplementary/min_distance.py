'''
# Edit Distance

# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
# You have the following 3 operations permitted on a word:
 * Insert a character
 * Delete a character
 * Replace a character

# Example 1:
  Input: word1 = "horse", word2 = "ros"
  Output: 3
  - Explanation: 
    * horse -> rorse (replace 'h' with 'r')
    * rorse -> rose (remove 'r')
    * rose -> ros (remove 'e')
'''

# TWO SOLUTIONS: SOL-1 O(N) Space and SOL-2 O(N^2) Space

#         ***** SOLUTION - 1 *****

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = i
            
        for i in range(1, m+1):
            pre = dp[0]
            dp[0] = i
            for j in range(1, n+1):
                temp = dp[j]
                if word1[i-1] == word2[j-1]:
                    dp[j] = pre
                else:
                    dp[j] = min(pre, dp[j-1], dp[j]) + 1
                pre = temp
        #print(dp)
        return dp[n]

'''
#         ***** SOLUTION - 2 *****

        m, n = len(word1), len(word2)
        dp = [[0 for j in range(m+1)] for i in range(n+1)]
        
        for i in range(1, n+1):
            dp[i][0] = 1 + dp[i-1][0]
        
        for j in range(1, m+1):
            dp[0][j] = 1 + dp[0][j-1]
            
        #print(dp)
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word2[i-1] == word1[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
        #print(dp)
        return(dp[n][m])
'''
'''
# Replace word1[i - 1] by word2[j - 1] (dp[i][j] = dp[i - 1][j - 1] + 1);
# If word1[0..i - 1) = word2[0..j) then delete word1[i - 1] (dp[i][j] = dp[i - 1][j] + 1);
# If word1[0..i) + word2[j - 1] = word2[0..j) then insert word2[j - 1] to word1[0..i) (dp[i][j] = dp[i][j - 1] + 1).
'''
