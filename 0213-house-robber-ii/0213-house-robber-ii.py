class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        0 1 2 3 4 5 6 7
        |           |
          |           |
         0,1,2,3  
        [1,2,3,1]
           s.  e
           
        i= 3
        j = 1
        
        '''
        n = len(nums)
         
        def helper(start, end):
            m = end - start + 1
            dp = [0] * m
            if m == 1:
                return nums[start]
            if m == 2:
                return max(nums[start], nums[end])
            dp[0] = nums[start]
            dp[1] = max(nums[start], nums[start + 1])
            for i in range(start + 2, end + 1):
                j = i - start
                dp[j] = max(nums[i] + dp[j - 2], dp[j - 1])
            return dp[-1]
        
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp1 = helper(0, n - 2)
        dp2 = helper(1, n - 1)
        return max(dp1, dp2)
        
            