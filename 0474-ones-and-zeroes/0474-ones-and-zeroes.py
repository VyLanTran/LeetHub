class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        '''
            0       1       2       3       4
        [(1, 1), (3, 1), (2, 4), (0, 1), (1, 0)]

        may sort the data in ascending order

        f(i, m, n) = max size of subset if you can use any of s between [0, i]
            if i < 0:
                return 0
            a, b = freq[i]
            # can we skip early if know that the result can't beat max_size
            if a > m or b > n:
                # must skip
                res = f(i - 1, m, n)
                put into cache
            # use substring i
            res = max(1 + f(i - 1, m - a, n - b), f(i - 1, m, n))
            put into cache
        '''

        strs_len = len(strs)
        freq = []
        dp = {}

        def count_zeroes_ones(s):
            zeroes, ones = 0, 0
            for char in s:
                if char == '0':
                    zeroes += 1
                else:
                    ones += 1
            return (zeroes, ones)

        for s in strs:
            freq.append(count_zeroes_ones(s))

        def f(i, m, n):
            if i < 0:
                return 0
            if (i, m, n) in dp:
                return dp[(i, m, n)]
            zeroes, ones = freq[i]
            if zeroes > m or ones > n:
                res = f(i - 1, m, n)
                dp[(i, m, n)] = res
                return res
            res = max(1 + f(i - 1, m - zeroes, n - ones), f(i - 1, m, n))
            dp[(i, m, n)] = res
            return res

        return f(strs_len - 1, m, n)


