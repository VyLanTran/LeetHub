class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        res = []
        
        for i in range(n):
            if i + 1 < n:
                left[i + 1] = left[i] * nums[i]
            j = n - i - 1
            if j - 1 >= 0: 
                right[j - 1] = right[j] * nums[j]
                
        for i in range(n):
            res.append(left[i] * right[i])
            
        return res