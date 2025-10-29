class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        dp[i] = max(dp[i - 1], num + dp[i - 2])
        a -> i - 2
        b -> i - 1

        a = nums[0]
        b = max(first 2 houses) only if n >= 2
        i from 2 to n - 1
        '''

        n = len(nums)
        a = nums[0]
        if n == 1:
            return a
        b = max(a, nums[1])

        for i in range(2, n):
            temp = max(b, a + nums[i])
            a, b = b, temp
        
        return b