class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Time: O(n^2)
        Space: O(n)
        '''

        res = 1
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
            res = max(res, dp[i])

        return res
            