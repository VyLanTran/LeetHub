class Solution:
    def numTrees(self, n: int) -> int:
        memo = [0] * (n + 1)

        def rec(n):
            if n <= 1:
                return 1
            if memo[n] != 0:
                return memo[n]
            res = 0
            for leftSize in range(n):
                rightSize = n - 1 - leftSize
                res += rec(leftSize) * rec(rightSize)
            memo[n] = res
            return res

        return rec(n)