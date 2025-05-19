class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums
        if not(a + b > c and a + c > b and b + c > a):
            return "none"
        if a == b and a == c:
            return "equilateral"
        if a == b or a == c or b == c:
            return "isosceles"
        return "scalene"