'''
# Longest Common Subsequence

# Given two strings text1 and text2, return the length of their longest common subsequence.
# A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without
# changing the relative order of the remaining characters.
# (eg, "ace" is a subsequence of "abcde" while "aec" is not). 
# A common subsequence of two strings is a subsequence that is common to both strings.

# If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
'''

# Solution - 1
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        size_one = len(text1) + 1
        size_two = len(text2) + 1
        dp = [[0 for j in range(size_two)] for i in range(size_one)]

        for i, num1 in enumerate(text1):
            for j, num2 in enumerate(text2):
                if num1 == num2:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[i][j]
        
# Solution - 2
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        i, j = 0, 0

        def f(s1, s2, i, j, memo):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(s1) or j == len(s2):
                memo[(i, j)] = 0
                return 0

            if(s1[i] == s2[j]):
                memo[(i, j)] = 1 + f(s1, s2, i+1, j+1, memo)

            else:
                memo[(i, j)] = max(f(s1, s2, i+1, j, memo),
                                   f(s1, s2, i, j+1, memo))

            return memo[(i, j)]

        return f(text1, text2, i, j, {})
   
  # Solution - 3
  
  class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # This memoize the function calls with arguments and returned results
        # so that you can call again later on with same parameters without incurring additional computation.
        # Max_size specifies that our LRU cache can grow without bounds.

        @lru_cache(maxsize=None)
        def memo_solve(ptr1, ptr2):
            if ptr1 == len(text1) or ptr2 == len(text2):
                return 0

            # Case 1
            if text1[ptr1] == text2[ptr2]:
                return 1 + memo_solve(ptr1+1, ptr2+1)

            # Case 2
            else:
                return max(memo_solve(ptr1+1, ptr2), memo_solve(ptr1, ptr2+1))
                # ^ Case 2 - Option 1           ^ Case 2 - Option 2
        # Start the recursion stack from str1[0] and str2[0]
        return memo_solve(0, 0)
