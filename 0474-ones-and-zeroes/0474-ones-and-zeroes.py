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
        freq = []
        rows, cols = m + 1, n + 1
        prev = [[0 for _ in range(cols)] for _ in range(rows)]
        cur = [[0 for _ in range(cols)] for _ in range(rows)]

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

        # Bottom-up
        for i in range(1, strs_len + 1):
            actual_index = i - 1
            zeroes, ones = freq[actual_index]
            for r in range(0, rows):
                for c in range(0, cols):
                    if zeroes > r or ones > c:
                        cur[r][c] = prev[r][c]
                    else:
                        cur[r][c] = max(1 + prev[r - zeroes][c - ones], prev[r][c])
            prev = copy.deepcopy(cur)

        return cur[-1][-1]

      