class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        Time: O(mn)
        Space: O(mn)
        '''

        len1, len2 = len(word1), len(word2)
        cache = [[float('inf') for _ in range(len1 + 1)] for _ in range(len2 + 1)]

        for j in range(len(cache[0])):
            cache[0][j] = j
        for i in range(len(cache)):
            cache[i][0] = i
        
        for i in range(1, len(cache)):
            for j in range(len(cache[0])):
                if j == 0:
                    continue
                if word1[j - 1] == word2[i - 1]:
                    cache[i][j] = cache[i - 1][j - 1]
                else:
                    cache[i][j] = 1 + min(cache[i - 1][j], cache[i][j - 1], cache[i - 1][j - 1])

        return cache[-1][-1]


