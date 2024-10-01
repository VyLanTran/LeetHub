class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        f(i, j, sum)
            invalid if j out of bound
            if i >= numRows: return sum 
            min{f(i + 1, j - 1), f(i + 1, j + 1)}
        '''
        
        numRows = len(triangle)
        res = float('inf')
        dp = {}
        
        def rec(i, j):
            if i >= numRows:
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            res = triangle[i][j] + min(rec(i + 1, j), rec(i + 1, j + 1))
            dp[(i, j)] = res
            return res
        
        return rec(0, 0)
        
   