class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        '''
        0, 1,  2
        2, 3, -5
        i  i    i
        
        boundary = 0, 2
        
        cur = 2, 5, 0 
        '''
        n = len(nums)
        cur, res = 0, 0
        for num in nums:
            cur += num
            if cur == 0:
                res += 1
        return res
                