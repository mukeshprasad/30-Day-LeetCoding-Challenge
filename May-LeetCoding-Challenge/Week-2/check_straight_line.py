'''
# Check If It Is a Straight Line

# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
  Check if these points make a straight line in the XY plane.
  
# Example 1:
    Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    Output: true
    
# Example 2 :
    Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    Output: false
    
# Constraints:
  * 2 <= coordinates.length <= 1000
  * coordinates[i].length == 2
  * -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
  * coordinates contains no duplicate point.
'''

# SOLUTION - O(N) time and O(1) space:

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # 336224394 submission
        # SOlUTION - 1:
        if len(coordinates) == 2:
            return True
        for i in coordinates[2:]:
            a = (i[1] - coordinates[0][1]) * (coordinates[1][0] - coordinates[0][0])
            b = (i[0] - coordinates[0][0]) * (coordinates[1][1] - coordinates[0][1])
            if a != b:
                return False
        return True
        
        # SOLUTION - 2:
        # (x1, y1), (x2, y2) = coordinates[:2]
        # for x, y in coordinates[2:]:
        #     if (y - y1) * (x2 - x1) != (x - x1) * (y2 - y1):
        #         return False
        # return True
        
        # SOLUTION - 3:
        # (x1, y1), (x2, y2) = coordinates[: 2]
        # return all((x2 - x1) * (y - y1) == (x - x1) * (y2 - y1) for x, y in coordinates[2:])
