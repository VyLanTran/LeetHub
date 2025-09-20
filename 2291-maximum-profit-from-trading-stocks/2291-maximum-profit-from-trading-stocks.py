class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:

        dp = [0 for _ in range(budget + 1)]

        for p, f in zip(present, future):
            for b in range(budget, p - 1, -1):
                dp[b] = max(dp[b], f - p + dp[b - p])
        
        return dp[-1]
        # m = len(present)
        # n = budget + 1
       
        # profits = [future[i] - present[i] for i in range(m)]
        # cache = [[0 for _ in range(n)] for _ in range(m)]

        # for i in range(m):
        #     if present[i] <= 0:
        #         cache[i][0] = max(0, profits[i]) + cache[i-1][0] if i >= 1 else 0
        # print(cache)

        # for j in range(n):
        #     if j >= present[0]:
        #         cache[0][j] = max(cache[0][j], profits[0])
        
        # for i in range(1, m):
        #     for j in range(1, n):
        #         cache[i][j] = max(cache[i][j], cache[i - 1][j])
        #         if j >= present[i] and profits[i] > 0:
        #             cache[i][j] = max(cache[i][j], profits[i] + cache[i - 1][j - present[i]])
        
        # print(cache)
        # return cache[-1][-1]

        

        '''
        m x n
        i: 0 -> len(present) - 1
        j: 0 -> budget

        cache[i][j] = max profit gained when you have a budget of
                        <j> and have the options to buy any stock
                        from i -> last stock
        cache[i][0] = 0 for any i
        cache[i][j] = max(cache[i+1][j], profits[i] + cache[i+1][j-profits[i]] if budget >= present[i])

        ----

        cache[i][j] = profits gained if you have budget <j> and the options to buy any stock from 0 -> i
        
        (5, 5), (2, 2), (1, 2),   budget = 6

            (budget left)
        i   0 
        0   2 
        1   0
      
   
        cache[i][j] = max{
            cache[i-1][j] ==> skip this stock
            cache[i-1][j - present[i]] + profits[i], only if j >= presents[i]
        }
        
        '''