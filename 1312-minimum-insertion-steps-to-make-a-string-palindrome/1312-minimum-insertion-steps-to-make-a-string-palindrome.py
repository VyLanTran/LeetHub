class Solution:
    def minInsertions(self, s: str) -> int:
        '''
        f(i, j)
            if i >= j: return 0
            if left == right: f(i + 1, j - 1)
            else:
                add to the left: f(i + 1, j)
                add to the right: f(i, j - 1)
        '''
        dp = {}
        
        def rec(i, j):
            if i >= j:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            res = 0
            if s[i] == s[j]:
                res = rec(i+1, j-1)
            else:
                res = 1 + min(rec(i + 1, j), rec(i, j - 1))
            dp[(i, j)] = res
            return res
        
        return rec(0, len(s) - 1)
            