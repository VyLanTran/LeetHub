class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        f(n = 1) = 1
        f(n = 2) 
            # take 1 step
            f(n - 1)
            # take 2 steps
            f(n - 2)
            retirm f(n - 2) + f(n - 1)

        a -> n - 2
        b -> n - 1

        for i from 3 to n, inclusively
            a, b = b, a + b

        a = 1
        b = 2
        '''
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a + b
        return b