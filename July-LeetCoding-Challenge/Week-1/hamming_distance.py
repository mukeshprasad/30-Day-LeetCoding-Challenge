# SOLUTION:
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 1.
        return bin(x ^ y).count(1)
        
        # 2.
        x, y = x ^ y, 0
        while x:
            y += x % 2
            x >>= 1
        return y
        
        # 3.
        x, y = x ^ y, 0
        while x:
            y += 1
            x = x & (x - 1)
        return y
        
        '''
        * We are asked to find the number of positions, where x and y have equal bits. It is the same as finding number of 1 bits in number t = x^y.
        * There is efficient way to find number of 1 bits in any number, using t = t&(t-1) trick:
            -> this operation in fact removes the last 1 bit from t. So, we just apply this rule in loop and increment our counter Out.

        * Complexity is O(k), where k is Hamming distance between numbers x and y, memory is O(1).
          Note, that it works (twice?) faster than usual bit counts, which have always 32 iterations.
        '''
