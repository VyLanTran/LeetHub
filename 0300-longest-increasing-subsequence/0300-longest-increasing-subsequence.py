class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        count = [1] * len(nums)
        maxLen = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    count[i] = max(count[i], 1 + count[j])
            maxLen = max(maxLen, count[i])
                    
        return maxLen
                    
        