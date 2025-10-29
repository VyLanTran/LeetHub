class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        10,9,2,5,3,7,101,18
         1,1,1

        for i from 0 to n - 1:
            for j from 0 to i - 1:
                if nums[j] < nums[i]:
                    len = 1 + dp[j]
                    update max val so far for dp[i]
        '''

        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)