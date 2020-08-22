'''
# Random Point in Non-overlapping Rectangles

# Given a list of non-overlapping axis-aligned rectangles rects,
  write a function pick which randomly and uniformily picks an integer point in the space covered by the rectangles.

# Note:
 * An integer point is a point that has integer coordinates. 
 * A point on the perimeter of a rectangle is included in the space covered by the rectangles. 
 * ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner,
    and [x2, y2] are the integer coordinates of the top-right corner.
 * length and width of each rectangle does not exceed 2000.
 * 1 <= rects.length <= 100
 * pick return a point as an array of integer coordinates [p_x, p_y]
 * pick is called at most 10000 times.
 
# Example 1:
  Input: 
  ["Solution","pick","pick","pick"]
  [[[[1,1,5,5]]],[],[],[]]
  Output: 
  [null,[4,1],[4,1],[3,3]]

# Example 2:
  Input: 
  ["Solution","pick","pick","pick","pick","pick"]
  [[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
  Output: 
  [null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
  Explanation of Input Syntax:

# The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array of rectangles rects.
  pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.
'''
# SOLUTION:
# 1.
class Solution:

    def __init__(self, rects):
        self.rects, self.ranges, sm = rects, [0], 0
        for x1, y1, x2, y2 in rects:
            sm += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.ranges.append(sm)

    def pick(self):
        n = random.randint(0, self.ranges[-1] - 1)
        i = bisect.bisect(self.ranges, n)
        x1, y1, x2, y2 = self.rects[i - 1]
        n -= self.ranges[i - 1]
        return [x1 + n % (x2 - x1 + 1), y1 + n // (x2 - x1 + 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()


# 2.
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects

        # I am more of a list comprehensions guy, but if you prefer to
        # put more effort with the keyboard, here's an unrolled version.
        
        # self.weights = []
        # for rect in rects:
        #     x1, y1, x2, y2 = rect
        #     area = (x2-x1+1)*(y2-y1+1)
        #     self.weights.append(area)
        
        self.weights = [(x2-x1+1)*(y2-y1+1) for x1, y1, x2, y2 in rects]
        
            
        # library functions are always faster
        # it beats the runtime of using an extra variable 
        # to calculate sum_of_weights in the loop above
        # even if that means, we have to iterate once more.
        # Such is the world of python :D
        sum_of_weights = sum(self.weights)
        
        self.weights = [x/sum_of_weights for x in self.weights]
            

    def pick(self) -> List[int]:
        rect = random.choices(
            population=self.rects,
            weights=self.weights,
            k=1
        )[0]  # random.choices returns a list, we extract the first (and only) element.

        x1, y1, x2, y2 = rect  # tuple unpacking
        
        rnd_x = random.randint(x1, x2)
        rnd_y = random.randint(y1, y2)
        return [rnd_x, rnd_y]
