class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        '''
        T(i) = min{
            for j between i + 1 and n - 1
                if height(i) + height(j) <= shelfWidth:
                    max(height of i to j) + T(j + 1)
            height(i) + T(i + 1) ==> book i on new level
            
        }
        
        T(n - 1) = (height(n - 1), width(n - 1))
        
        0       1     2     3     4     5     6
        [1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
     
        '''
        
        n = len(books)
        dp = [None for _ in range(n)]
        
        def rec(i):
            if i >= n:
                return 0
            if i == n - 1:
                return books[i][1]
            if dp[i]:
                return dp[i]
            res = float('inf')
            curWidth = books[i][0]
            curHeight = books[i][1]
            for j in range(i + 1, n):
                if curWidth + books[j][0] <= shelfWidth:
                    curWidth += books[j][0]
                    curHeight = max(curHeight, books[j][1])
                    res = min(res, curHeight + rec(j + 1))
                else:
                    break
            res = min(res, books[i][1] + rec(i + 1))
            dp[i] = res
            return res
        
        return rec(0)
                