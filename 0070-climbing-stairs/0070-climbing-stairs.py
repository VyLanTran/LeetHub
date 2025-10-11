class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        Why dp[i] = dp[i - 1] + dp[i - 2]
        To reach dp[i], there are 2 ways
            1. Take dp[i - 2] ways + the last time is a 2-step
            2. Take dp[i - 1] ways + the last time is a 1-step
        => Finbonacci
        '''

        if n == 1:
            return 1
        if n == 2:
            return 2
        prev1, prev2 = 1, 2

        for i in range(n - 2):
            prev1, prev2 = prev2, prev1 + prev2

        return prev2