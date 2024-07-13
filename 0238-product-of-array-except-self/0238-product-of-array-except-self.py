class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        for i in range(n - 1):
            res[i + 1] = nums[i] * res[i]
        right = 1
        for i in range(n - 1, 0, -1):
            right *= nums[i]
            res[i - 1] *= right
        
        return res