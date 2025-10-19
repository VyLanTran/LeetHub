class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        '''
        Time: O(n^3)
        Space: O(1)
        '''
        def find_side(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return sqrt((x1-x2)**2 + (y1-y2)**2)

        def find_squared_area(a, b, c):
            s = (a + b + c) / 2
            return s * (s - a) * (s - b) * (s - c)

        n = len(points)
        max_area = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a = find_side(points[i], points[j])
                    b = find_side(points[i], points[k])
                    c = find_side(points[j], points[k])
                    max_area = max(max_area, find_squared_area(a, b, c))

        return sqrt(max_area)