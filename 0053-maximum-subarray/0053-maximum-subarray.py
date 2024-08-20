class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        -2,1,-3,4,-1,2,1,-5,4
           i  i i  i i  i i i
        
        maxLocal = 5
        maxGlobal = 6
        '''
        
        maxLocal, maxGlobal = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            maxLocal = max(nums[i], nums[i] + maxLocal)
            maxGlobal = max(maxGlobal, maxLocal)
        
        return maxGlobal