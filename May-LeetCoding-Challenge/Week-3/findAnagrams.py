'''
# Find All Anagrams in a String

# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
  Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
  
#The order of output does not matter.

# Example 1:

  Input:
  s: "cbaebabacd" p: "abc"

  Output:
  [0, 6]

  *Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

  Input:
  s: "abab" p: "ab"

  Output:
  [0, 1, 2]

  *Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

# SOLUTION : SLIDING WINDOW TECHNIQUE - O(N)

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lst = []
        p_counter = Counter(p)
        s_counter = Counter(s[: len(p)-1])
        #print(s_counter)
        for i in range(len(p)-1, len(s)):
            s_counter[s[i]] += 1
            if s_counter == p_counter:
                lst.append(i - len(p) + 1)   
            s_counter[s[i-len(p)+1]] -= 1
            
            if s_counter[s[i-len(p)+1]] == 0:
                del s_counter[s[i-len(p)+1]]
                
        return lst
        
# SOLUTION : O(N) Time and O(1) Space:  

'''
  # Define hash(s) := sum(hash(ch) for ch in s)
  # Since hash(s) equals hash(Anagram(s)),
  # return index i which hash(s[i:i+len(p)]) equals hash(p).
  # p.s. hash(s[i+1:i+1+len(p)]) equals hash(s[i:i+len(p)]) - hash(s[i]) + hash(s[i+len(p)])
'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 340762043
        hashp = sum(hash(ch) for ch in p)
        hashi = sum(hash(ch) for ch in s[:len(p)])
        
        ret = []
        if hashi == hashp:
            ret.append(0)
            
        for idx, (ch_out, ch_in) in enumerate(zip(s, s[len(p):]), 1):
            hashi += hash(ch_in) - hash(ch_out)
            if hashi == hashp:
                ret.append(idx)
                
        return ret
