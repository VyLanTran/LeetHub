class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        '''
        
        wwwzfvedwfvhsww
        
        w|ww|z|f|v|e|d|wf|vh|s|
        www|z|f|v|e|d|w|fv|h|s|ww
        
        cur = b
        res = 1
        seen = {a}
        '''
        
        seen = set()
        n = len(s)
        def dfs(i):
            if i >= n:
                return 0
            cur = ""
            maxNum = 0
            for j in range(i, n):
                cur += s[j]
                if cur not in seen:
                    seen.add(cur)
                    maxNum = max(maxNum, 1 + dfs(j + 1))
                    seen.remove(cur)
            return maxNum
        
        return dfs(0)