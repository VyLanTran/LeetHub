class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        dp = [[0 for _ in range(len1 + 1)] for _ in range(len2 + 1)]
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0:
                    dp[i][j] = j
                    continue
                if j == 0:
                    dp[i][j] = i
                    continue
                a, b = word1[j - 1], word2[i - 1]
                if a == b:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        # print(dp)
        return dp[len2][len1]
    
    '''
      i   n  t. e. n. t. i. o n
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
e [1, 2, 2, 2, 1, 2, 2, 2, 2, 2], 
x [1, 2, 3, 3, 2, 3, 3, 3, 3, 3], 
e [1, 2, 3, 4, 3, 4, 4, 4, 4, 4], 
c [1, 2, 3, 4, 4, 5, 5, 5, 5, 5], 
u [1, 2, 3, 4, 5, 6, 6, 6, 6, 6], 
t [1, 2, 3, 3, 4, 5, 6, 7, 7, 7], 
i [1, 1, 2, 3, 4, 5, 6, 6, 7, 8], 
o [1, 2, 3, 4, 5, 6, 7, 7, 6, 7], 
n [1, 2, 2, 3, 4, 5, 6, 7, 7, 6]
    
    '''