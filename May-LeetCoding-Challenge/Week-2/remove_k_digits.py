'''
# Remove K Digits

# Given a non-negative integer num represented as a string,
  remove k digits from the number so that the new number is the smallest possible.

# Note:
  * The length of num is less than 10002 and will be ≥ k.
  * The given num does not contain any leading zero.

# Example 1:
  Input: num = "1432219", k = 3
  Output: "1219"
  Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

# Example 2:
  Input: num = "10200", k = 1
  Output: "200"
  Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
 
'''
# SOLUTION - 1: O(N) time
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # 338807143 submission
        lst = []
        for digit in num:
            while k and lst and lst[-1] > digit:
                k -= 1
                lst.pop()
            lst.append(digit)
            
        return ''.join(lst[:-k or None]).lstrip('0') or '0'

# SOLUTION Using REGEX:
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        sub = re.compile('1[0]|2[01]|3[0-2]|4[0-3]|5[0-4]|6[0-5]|7[0-6]|8[0-7]|9[0-8]|.$').sub
        for _ in range(k):
            num = sub(lambda m: m.group()[1:], num, 1)
        return num.lstrip('0') or '0'
