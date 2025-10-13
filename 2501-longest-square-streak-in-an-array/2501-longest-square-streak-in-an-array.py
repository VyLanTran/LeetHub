class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        '''
        Time: O(n)

        4,3,6,16,8,2
        a,b,c, a,d,a
        
        2, 4, 16, 256

        4, 256, 2, 16

        a, a^2, a^4, a^8

        {
            4: 
            3: 1
            6: 1
            16: 
            8: 2
            2: 1
        }
        '''

        nums = set(nums)
        dp = {}
        max_len = 1

        def f(num):
            if sqrt(num) not in nums:
                dp[num] = 1
                return 1
            if num in dp:
                return dp[num]
            res = 1 + f(int(sqrt(num)))
            dp[num] = res
            return res

        for num in nums:
            max_len = max(max_len, f(num))
        
        return -1 if max_len == 1 else max_len