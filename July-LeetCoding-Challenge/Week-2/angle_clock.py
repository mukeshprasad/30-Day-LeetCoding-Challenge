'''
# Angle Between Hands of a Clock

# Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

# Example 1:
  Input: hour = 12, minutes = 30
  Output: 165
'''
# SOLUTION:
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        a = abs((hour * 30 + minutes * 0.5) - (minutes * 6))
        return min(a, 360 - a)
