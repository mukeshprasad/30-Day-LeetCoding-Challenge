'''
# Word Break II

# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

# Note:
    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.

# Example 1:

# Input:
  s = "catsanddog"
  wordDict = ["cat", "cats", "and", "sand", "dog"]
  Output:
  [
    "cats and dog",
    "cat sand dog"
  ]

# Example 2:

  Input:
  s = "pineapplepenapple"
  wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
  Output:
  [
    "pine apple pen apple",
    "pineapple pen apple",
    "pine applepen apple"
  ]
  Explanation: Note that you are allowed to reuse a dictionary word.

# Example 3:

  Input:
  s = "catsandog"
  wordDict = ["cats", "dog", "sand", "and", "cat"]
  Output:
  []
'''
# SOLUTION: - DFS - Backtracking - Memoization
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # 1.
        # sentences(i) returns a list of all sentences that can be built from the suffix s[i:].
        memo = {len(s): ''}
        def sentences(i):
            if i not in memo:
                memo[i] = [s[i: j] + (tail and ' ' + tail)
                           for j in range(i+1, len(s)+1)
                           if s[i: j] in wordDict
                           for tail in sentences(j)]
            return memo[i]
        return sentences(0)
        
        # 2. My implementation
        def recur(s, hold, output):
            if not s:
                output.append(hold.strip())
                return
            w = ''
            for i, ch in enumerate(s):
                w += ch
                if w in wordDict:
                    recur(s[i+1:], hold+' '+w, output)
            return output
        
        set_s = set(s)
        set_wd = set(list(itertools.chain(*wordDict)))
        for i in set_s:
            if i not in set_wd:
                return []
        return recur(s, '', [])
        
        # 3. Optimization to 1.
        memo, words = {len(s): ['']}, set(wordDict)
        ss = set(len(x) for x in words)
        def sentences(i):
            if i not in memo:
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                           for j in [i + x for x in ss]
                           if s[i:j] in words
                           for tail in sentences(j)]
            return memo[i]
        return sentences(0)        
