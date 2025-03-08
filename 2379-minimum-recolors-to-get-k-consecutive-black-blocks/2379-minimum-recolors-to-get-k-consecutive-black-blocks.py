class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        '''
        0123456789
        WBBWWBBWBW

        1, 2, 5, 6, 8
    0                    9

     

        0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        W, B, B, W, W, B, B, W, B, W
        j. j. j  j. j  j. j. j. j
        i. i. i
        minOperations = inf, 3, 
        numBlacks: 4, 5, 4
        numOperations = k - numBlacks = 3
        when j >= k, start to slide from left

        WBWBBBW
        jjjj
        i

        left = 0
        minOps = inf
        numBlacks = 0
        for right in range(n):
            numBlacks += 1 if blocks[right] == 'B' else 0
            if right >= k:
                numBlacks -= 1 if blocks[left] == 'B' else 0
                left += 1
            if right >= k - 1:
                res = min(res, k - numBlacks)
        '''

        left = 0
        minOps = float('inf')
        numBlacks = 0

        for right in range(len(blocks)):
            numBlacks += 1 if blocks[right] == 'B' else 0
            if right >= k:
                numBlacks -= 1 if blocks[left] == 'B' else 0
                left += 1
            if right >= k - 1:
                minOps = min(minOps, k - numBlacks)

        return minOps