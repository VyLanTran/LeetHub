class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        '''
        totalsum = 16
        
        if totalSum % p == 0 => return 0
        
        0, 1, 2, 3
        6, 3, 5, 2      p = 9

        => want totalSum - (sum - prefixSum) % 9 == 0
        
        if size of subarray == n => don't choose
     
        '''
    
        
        minLen = -1
        dp = {0: -1}
        totalSum, sum = 0, 0
        
        for num in nums:
            totalSum += num
        if totalSum % p == 0:
            return 0
        for i in range(len(nums)):
            sum += nums[i]
            val = (totalSum - sum) % p
            mod = (p - val) % p
            if mod in dp:
                removedSize = i - dp[mod]
                if removedSize != len(nums):
                    minLen = min(minLen, removedSize) if minLen >= 0 else removedSize
            dp[sum % p] = i
        
        
        return minLen if minLen >= 0 else -1