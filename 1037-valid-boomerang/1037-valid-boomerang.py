class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        
        def find_slope(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            return x2 - x1, y2 - y1

        num1, denom1 = find_slope(points[0], points[1])
        num2, denom2 = find_slope(points[0], points[2])

        return not num1 * denom2 == num2 * denom1

        