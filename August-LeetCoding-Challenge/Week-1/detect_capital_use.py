'''
# Detect Capital

# Given a word, you need to judge whether the usage of capitals in it is right or not.

# We define the usage of capitals in a word to be right when one of the following cases holds:
     * All letters in this word are capitals, like "USA".
     * All letters in this word are not capitals, like "leetcode".
     * Only the first letter in this word is capital, like "Google".

# Otherwise, we define that this word doesn't use capitals in a right way.

# Example 1:

  Input: "USA"
  Output: True 

# Example 2:

  Input: "FlaG"
  Output: False

# Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

'''
# SOLUTION: O(N) Time and O(1) Space
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # 1.
        return word.isupper() or word.islower() or word.istitle()
        
        # 2.
        return word[1:] == word.lower() or word == word.upper()
        
        # 3. regex implementation
        return re.fullmatch(r'[A-Z]*|.[a-z]*')
        
        # 4.
        if (word.isupper() or word.islower()) or (word[0].isupper() and not(any(s.isupper() for s in word[1:]))):
            return True
        return False        
