class Solution:
    def numSquares(self, n: int) -> int:
        '''
        f(n)
            if n is a perfect square:
                return 1
            try (sqrt(n))**2 to 1**2:
                1 + min(f(n - k**2))

        1, 4, 9, 16
        '''

        # dp = {}

        # def f(n):
        #     if int(sqrt(n)) ** 2 == n:
        #         return 1
        #     if n in dp:
        #         return dp[n]
        #     res = float('inf')
        #     for i in range(int(sqrt(n)), 0, -1):
        #         res = min(res, 1 + f(n - i**2))
        #     dp[n] = res
        #     return res

        # return f(n)

        if int(sqrt(n)) ** 2 == n:
            return 1

        queue = deque()
        count = 1

        for i in range(int(sqrt(n)), 0, -1):
            queue.append(i * i)
        squares = set(queue)

        while True:
            size = len(queue)
            count += 1
            for _ in range(size):
                val = queue.popleft()
                for s in squares:
                    if val + s == n:
                        return count
                    queue.append(val + s)

        '''
        9, 4, 1

        count = 0
        queue: 4, 1
        size = 3
        '''

        
