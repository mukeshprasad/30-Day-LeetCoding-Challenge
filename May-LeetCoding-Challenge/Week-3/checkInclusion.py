'''
# Permutation in String

# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
  In other words, one of the first string's permutations is the substring of the second string.

# Example 1:
  Input: s1 = "ab" s2 = "eidbaooo"
  Output: True
  Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
  Input:s1= "ab" s2 = "eidboaoo"
  Output: False
 
# Note:
  The input strings only contain lower case letters.
  The length of both given strings is in range [1, 10,000].
'''

# SOLUTION - 1: SLIDING WINDOW OPTIMIZED 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 341252585 submission
        a = [ord(x) - ord('a') for x in s1]
        b = [ord(x) - ord('a') for x in s2]
        
        target = [0] * 26
        for i in a:
            target[i] += 1
        window = [0] * 26
        
        for i in range(len(b)):
            window[b[i]] += 1
            if i >= len(a):
                window[b[i - len(a)]] -= 1
            if target == window:
                return True
        return False
        
# SOLUTION - 2: Using hash - O(N) Time and O(1) Space
'''
# The Python hash function will convert each character in s1 to a value (defined by a seed).
# This value will be different on each function call, but the same within a call. Based on this logic, the algorihm does as follows:

# Get the sum of the hash of each char in s1
  Get a sum of each char in s2 up to len(s1)-1

# Iterate over remaining chars of s2, getting one char to take out of the sum (ch_out),
  and one to add to the sum (ch_in). This is similar to the sliding window approach
# If the sum in 1 and the sum in 2 ever match, return True, otherwise return False
# Analysis: Worst case scenario the pattern is not in s2, meaning that the sums will never match.
  This algorithm will have to go over all chars in s2, making it O(n) in time complexity.
  Since we are just updating one sum on every iteration, it is O(1) in space.
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 341264991 Fastest
        hashS1 = sum(hash(ch) for ch in s1)
        hashS2 = sum(hash(ch) for ch in s2[:len(s1)-1])
        
        for ch_out, ch_in in zip([''] + list(s2), s2[len(s1)-1:]):
            hashS2 += hash(ch_in) - hash(ch_out)
            if hashS1 == hashS2:
                return True
        return False
