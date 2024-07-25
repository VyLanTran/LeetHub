class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, minVal, maxVal = max(nums), 1, 1
        for num in nums:
            if num == 0:
                res = max(res, num)
                minVal, maxVal = 1, 1
            else:
                minVal, maxVal = min(num, num * minVal, num * maxVal), max(num, num * minVal, num * maxVal)
                res = max(res, maxVal)
                
        return res
        
    
        