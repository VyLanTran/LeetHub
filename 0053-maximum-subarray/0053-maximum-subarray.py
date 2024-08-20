class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxLocal, maxGlobal = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            maxLocal = max(nums[i], nums[i] + maxLocal)
            maxGlobal = max(maxGlobal, maxLocal)
        
        return maxGlobal