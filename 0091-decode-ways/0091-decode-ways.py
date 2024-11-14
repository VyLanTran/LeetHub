class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        012
        226
        f(s=0)
            2, f(s = 1)=2
                2, f(s = 2) = 1
                    6, f(s = 3) = 1
                26, f(s = 3) = 1
            22, f(s = 2)=1
            
        start with 0 => return 0
        '''
        
        n = len(s)
        memo = {}
        
        def rec(i):
            if i >= n:
                return 1
            if s[i] == "0":
                return 0
            if i in memo:
                return memo[i]
            res = 0
            res += rec(i + 1)
            if s[i] == "1" and i + 1 < n:
                res += rec(i + 2)
            elif s[i] == "2" and i + 1 < n and int(s[i + 1]) <= 6:
                res += rec(i + 2)
            else:
                pass
            memo[i] = res
            return res
        
        return rec(0)
                