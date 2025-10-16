class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        '''
        k = number of strings in strs
        N = total number of char in all strings

        Top-down:
            Time: O(N + kmn)
            Space: O(kmn)
        Bottom-up:
            Time: O(N + kmn)
            Space: O(mn)
        '''

        """
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

        # Top-down
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
        """

        strs_len = len(strs)
        # freq = []
        rows, cols = m + 1, n + 1
        # prev = [[0 for _ in range(cols)] for _ in range(rows)]
        # cur = [[0 for _ in range(cols)] for _ in range(rows)]
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        def count_zeroes_ones(s):
            zeroes, ones = 0, 0
            for char in s:
                if char == '0':
                    zeroes += 1
                else:
                    ones += 1
            return (zeroes, ones)

        # for s in strs:
        #     freq.append(count_zeroes_ones(s))

        # Bottom-up (2 dp, very slow because of deepcopy)
        # for i in range(1, strs_len + 1):
        #     actual_index = i - 1
        #     zeroes, ones = freq[actual_index]
        #     for r in range(0, rows):
        #         for c in range(0, cols):
        #             if zeroes > r or ones > c:
        #                 cur[r][c] = prev[r][c]
        #             else:
        #                 cur[r][c] = max(1 + prev[r - zeroes][c - ones], prev[r][c])
        #     prev = copy.deepcopy(cur)

        for s in strs:
            zeroes, ones = count_zeroes_ones(s)
            # if we want to use a single dp, we must go backward (rows - 1 back) and (cols - 1) back
            # because otherwise dp[r - zeroes][c - ones] is overwritten with the res of current layer
            for r in range(rows - 1, zeroes - 1, -1):
                for c in range(cols - 1, ones - 1, -1):
                    dp[r][c] = max(dp[r][c], 1 + dp[r - zeroes][c - ones])

        return dp[-1][-1]

      