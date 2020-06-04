'''
# Reverse String

# Write a function that reverses a string. The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
  You may assume all the characters consist of printable ascii characters.

# Example 1:

  Input: ["h","e","l","l","o"]
  Output: ["o","l","l","e","h"]

# Example 2:

  Input: ["H","a","n","n","a","h"]
  Output: ["h","a","n","n","a","H"]
'''

# SOLUTION - 1: O(N) Time and O(N) Space - Recursion Stack
class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1


# SOLUTION - 2: O(N) Time and O(1) Space - Two Pointers
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        for i in range(len(s)//2):
            s[i], s[j] = s[j], s[i]
            j -= 1
        
        
        '''       (OR)
        Pythonic Way - One Liner
        '''
        s.reverse()
        
        '''(OR)
        '''
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
    '''        
    Complexity Analysis:
      Time complexity : O(N) to swap N/2 element.
      Space complexity : O(1), it's a constant space solution.
      '''
