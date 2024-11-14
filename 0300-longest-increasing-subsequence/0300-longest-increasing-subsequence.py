class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        0 ,1,2,3,4,5,6  ,7
        10,9,2,5,3,7,101,18
        1. 1 1 2 2 3. 4. 4
        '''
        
        n = len(nums)
        dp = [1] * n
        res = 1
        for i in range(n):
            maxLen = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    maxLen = max(maxLen, 1 + dp[j])
            dp[i] = maxLen
            res = max(res, maxLen)
        return res
        