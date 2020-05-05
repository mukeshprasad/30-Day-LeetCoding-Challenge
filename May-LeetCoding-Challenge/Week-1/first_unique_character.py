'''
# First Unique Character in a String

# Given a string, find the first non-repeating character in it and return it's index.
  If it doesn't exist, return -1.

# Examples:
  s = "leetcode"
  return 0.

  s = "loveleetcode",
  return 2.
# Note: 
  You may assume the string contain only lowercase letters.
 
'''

# SOLUTION: O(N)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 334805699 submission
        dct = Counter(s)
        for x in dct:
            if dct[x] == 1:
                return s.index(x)
        return -1
