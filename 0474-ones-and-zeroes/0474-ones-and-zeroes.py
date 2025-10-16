class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        '''
        k = number of strings in strs
        N = total number of char in all strings
        Time: O(N + kmn)
        Space: O(kmn)
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


