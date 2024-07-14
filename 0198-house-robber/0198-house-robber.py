class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        res = [0] * n
        
        for i in range(n - 1, -1, -1):
            next1 = res[i + 1] if i + 1 < n else 0
            next2 = res[i + 2] if i + 2 < n else 0
            res[i] = max(nums[i] + next2, next1)
            
        return res[0]