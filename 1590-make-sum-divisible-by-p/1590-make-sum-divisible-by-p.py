class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        '''
        totalsum = 16
        
        if totalSum % p == 0 => return 0
        
        0, 1, 2, 3
        6, 3, 5, 2      p = 9
        i  i  i  i
        
        0, 1, 2, ..., i
        0, 1, 2, ..., i, i + 1, ..., j
        => substring = sum[j] - sum[i]
        
        sum = 16
        
        totalSum - subarraySum % 9 == 0
        => need subarray == totalSum = 7
        => want totalSum - (sum - prefixSum) % 9 == 0
        => 16 - 6 + prefixSum
        => 10 + prefixSum
        => 1 + prefixSum
        => 8
        
        16 - 9 + prefixSum = 7 + prefixSum
        16 - 14 + prefixSum = 2 + prefixSum => need 7
        16 - 16 + prefix = prefix ==> need 0 ==> 3 - 1 = 2
        
        if size of subarray == n => don't choose
        
        {
        0: [-1, 1]
        6: [0]
        5: [2]
        }
        '''
        
        '''
        totalSum = 10
        p=6
        0,1,2,3
        3,1,4,2
        i
        
        sum = 3
        
        {
        0: -1
        5: 0
        }
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
            # print(mod, dp)
            if mod in dp:
                removedSize = i - dp[mod]
                if removedSize != len(nums):
                    minLen = min(minLen, removedSize) if minLen >= 0 else removedSize
            dp[sum % p] = i
        
        
        return minLen if minLen >= 0 else -1