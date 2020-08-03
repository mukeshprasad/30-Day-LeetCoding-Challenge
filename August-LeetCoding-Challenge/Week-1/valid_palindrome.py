'''
# Valid Palindrome

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

  Input: "A man, a plan, a canal: Panama"
  Output: true
  
# Example 2:

  Input: "race a car"
  Output: false

# Constraints:
    * s consists only of printable ASCII characters.
'''
# SOLUTION:
class Solution:
    def ValidPalindrome(self, s: str) -> bool:
        # 1.
        p = '' 
        for c in s.lower():
             if c.isalnum():
                p += c
        return p == p[::-1]
        
        # 2. REGEX
        s = re.sub(r'[\W+_]', s.lower())
        return s == s[::-1]
