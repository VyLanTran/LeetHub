class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_global = float('-inf')
        max_local = 0

        for num in nums:
            max_local = max(num, num + max_local)
            max_global = max(max_global, max_local)
        
        return max_global