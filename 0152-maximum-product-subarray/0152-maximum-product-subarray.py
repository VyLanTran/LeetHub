class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(1)
        '''
        
        res = float('-inf')
        local_max, local_min = 1, 1

        for num in nums:
            local_max, local_min = max(num, num * local_max, num * local_min), min(num, num * local_max, num * local_min)
            res = max(res, local_max)

        return res