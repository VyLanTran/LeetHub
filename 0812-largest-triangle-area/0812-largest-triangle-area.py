class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def find_side_length(a, b):
            x1, y1 = a
            x2, y2 = b
            return sqrt((x1-x2)**2 + (y1-y2)**2)

        n = len(points)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    p1, p2, p3 = points[i], points[j], points[k]
                    a = find_side_length(p1, p2)
                    b = find_side_length(p1, p3)
                    c = find_side_length(p2, p3)
                    s = (a + b + c) / 2
                    m = s * (s-a) * (s-b) * (s-c)
                    # res = max(res, sqrt(s * (s-a) * (s-b) * (s-c)))
                    # print(m)
                    # if m < 0:
                    #     print(a, b, c, s, m)
                    if m >= 0:
                        res = max(res, sqrt(m))
        return res