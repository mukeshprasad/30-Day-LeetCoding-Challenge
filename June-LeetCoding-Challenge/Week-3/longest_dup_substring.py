'''
# Longest Duplicate Substring

# Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

# Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)


# Example 1:

  Input: "banana"
  Output: "ana"

# Example 2:
  Input: "abcd"
  Output: "" 

# Note:

  * 2 <= S.length <= 10^5
  * S consists of lowercase English letters.
'''

# SOLUTION 1:
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        low, high = 2, len(s) - 1
        best = ''

        while low <= high:
            mid = low + (high - low) // 2
            v = self.find_duplicate_substr_of_len_k(s, mid)

            if v != '':
                best = v
                low = mid + 1
            else:
                high = mid - 1

        return best


    def find_duplicate_substr_of_len_k(self, s, k):
        MOD = (1 << 61) - 1
        BASE = 26
        D = pow(BASE, k - 1, MOD)
        chash = 0
        seen = collections.defaultdict(list)

        for i in range(len(s)):
            if i >= k:
                l_chval = ord(s[i - k]) - ord('a')
                chash = (chash - l_chval * D) % MOD

            chval = ord(s[i]) - ord('a')
            chash = (chash * BASE + chval) % MOD

            if i >= k - 1:
                if chash in seen:
                    substr_i = s[i - k + 1:i + 1]
                    for j in seen[chash]:
                        substr_j = s[j - k + 1:j + 1]
                        if substr_i == substr_j:
                            return substr_i

                seen[chash].append(i)

        return ''


# SOLUTION - 2:

class Solution:
    def longestDupSubstring(self, S):
        
        A = [ord(c) - ord('a') for c in S]
        mod = 2**63 - 1

        def test(L):
            p = pow(26, L, mod)
            cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
            seen = {cur}
            for i in range(L, len(S)):
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
                
                if cur in seen: return i - L + 1
                seen.add(cur)
        res, lo, hi = 0, 0, len(S)
        while lo < hi:
            mi = (lo + hi + 1) // 2
            pos = test(mi)
            if pos:
                lo = mi
                res = pos
            else:
                hi = mi - 1
        return S[res:res + lo]
