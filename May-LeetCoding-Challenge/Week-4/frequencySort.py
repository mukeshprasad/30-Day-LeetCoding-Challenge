'''
# Sort Characters By Frequency

# Given a string, sort it in decreasing order based on the frequency of characters.

# Example 1:
  Input:
    "tree"
  Output:
    "eert"

  Explanation:
    * 'e' appears twice while 'r' and 't' both appear once.
    * So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

# Example 2:
  # Input:
    "cccaaa"

  # Output:
    "cccaaa"

  Explanation:
    * Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
    * Note that "cacaca" is incorrect, as the same characters must be together.
'''

# SOLUTION - 1: O(N) Time - Actually Bucket Sort - Refer Solution - 3

class Solution:
    def frequencySort(self, s: str) -> str:
        # return ''.join(ch*count for ch, count in Counter(s).most_common()) # One-liner Pythonic Way 
        ans = ''
        for ch, count in Counter(s).most_common():
            ans += ch*count
        return ans
        
# SOLUTION - 2: Using heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        h = [(v,k) for k,v in Counter(s).items()]
        return ''.join(v*k for v,k in heapq.nlargest(len(h),h))

# SOLUTION - 3: Bucket Sort - Similar to 1st Solution

class Solution:
    def frequencySort(self, s: str) -> str:
        buckets, res = [[]]*len(s), ""
        counter = collections.Counter(s)
        for ch, cnt in counter.items():
            buckets[cnt-1] = buckets[cnt-1]+[ch]

        for i in range(len(buckets)-1, -1, -1):
            if buckets[i]:
                res += "".join([c*(i+1) for c in buckets[i]])
        return res
