'''
# Longest Palindrome

# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Note:
  Assume the length of given string will not exceed 1,010.

# Example:

  Input:
  "abccccdd"

  Output:
  7

# Explanation:
  One longest palindrome that can be built is "dccaccd", whose length is 7.
'''
# SOLUTION:
class Solution:
    def longestPalindrome(self, s:str) -> int:
        # 1.
        odds = sum(value & 1 for value in Counter(s).values())
        return len(s) - odds + bool(odds)
        
        # 2.
        ans = odd = 0
        for value in Counter(s).values():
            if value % 2 == 0:
                ans += value
            else:
                ans += value - 1
                odd = 1
        return ans + odd
