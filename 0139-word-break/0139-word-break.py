class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        0 1 2 3 4 5 6 7
        l e e t c o d e
      T F F F T _ _ _ _ 
dp    0 1 2 3 4 5 6 7 8
        i i   i
      j 
        '''
        
        wordLen = len(s)
        dp = [False for _ in range(wordLen + 1)]
        dp[0] = True
        wordDict = set(wordDict)
        
        for i in range(1, len(dp)):
            for j in range(i):
                suffix = s[j:i]
                if suffix in wordDict and dp[j]:
                    # print(i, j, suffix)
                    dp[i] = True
                    break
            if not dp[i]:
                dp[i] = False
        # print(dp)
        return dp[-1]
        