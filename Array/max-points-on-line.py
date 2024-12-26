# Max Points on a Line
# Link - https://leetcode.com/problems/max-points-on-a-line/description/

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
points = [[1,1],[2,2],[3,3]]
# Output: 3

points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4


# Approcah - using hashing and mathematics

from collections import defaultdict

def maxPoints(points):
    n = len(points)

    if n < 2:
        return n

    def get_slope(p1,p2):
        x1,y1 = p1
        x2,y2 = p2

        if x1-x2 == 0:
            return (float('inf'),0)
        return (y2-y1)/(x2-x1)
        
    ans = 1

    for i,p1 in enumerate(points):
        slopes = defaultdict(int)
        for j,p2 in enumerate(points[i + 1:]):
            slope = get_slope(p1,p2)
            slopes[slope] += 1
            ans = max(ans,slopes[slope]+1)        
    return ans

result = maxPoints(points)
print(result)