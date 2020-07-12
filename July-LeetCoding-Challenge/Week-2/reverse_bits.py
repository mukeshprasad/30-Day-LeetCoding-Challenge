'''
# Reverse Bits

# Reverse bits of a given 32 bits unsigned integer.

Example 1:
  Input: 00000010100101000001111010011100
  Output: 00111001011110000010100101000000
  Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
                so return 964176192 which its binary representation is 00111001011110000010100101000000.
'''
# SOLUTION:
class Solution:
    # 1. Bit by Bit: Time -> O(1) <- Space : Since 32 bits are fixed as given.
    def reverseBits(self, n: int) -> int:
        rev, power = 0, 31
        while n:
            rev += (n & 1) << power
            n >>= 1
            power -= 1
        return rev
        
    # 2. Byte by Byte with Memoization: Time -> O(1) <- Space
    def reverseBits(self, n: int) -> int:    
        rev, power = 0, 24
        while n:
            rev += self.reverseByte(n & 0xff) << power
            n >>= 8
            power -= 8
        return rev
    @functools.lru_cache(maxsize=256)
    def reverseByte(self, byte):
        return (byte * 0x0202020202 & 0x010884422010) % 1023
     
    # 3. Shift and Mask: Time -> O(1) <- Space
    def reverseBits(self, n: int) -> int:
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
    return n
    
    # 4. Other Shift ans Mask
    def reverseBits(self, n: int) -> int:
        for _ in range(32):
            res <<= 1
            res |= n & mask
            n >>= 1
        return res
