class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def find_squared_sum(n):
            res = 0
            while n > 0:
                res += (n % 10) ** 2
                n //= 10
            return res

        while True:
            if n == 1:
                return True
            if n in visited:
                return False
            visited.add(n)
            n = find_squared_sum(n)

            
