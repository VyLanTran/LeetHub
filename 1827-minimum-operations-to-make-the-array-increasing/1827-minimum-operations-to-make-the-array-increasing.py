class Solution:
    def minOperations(self, nums: List[int]) -> int:
        '''
        1, 5, 2, 4, 1
        1, 5, 6, 7, 8
        4 + 3 + 7
        '''

        res = 0
        curMax = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] <= curMax:
                res += curMax + 1 - nums[i]
            curMax = max(curMax + 1, nums[i])

        return res

        '''
        res = 0, 4, 7, 14
        curMax = 1, 5, 6, 7

        0, 1, 2, 3, 4
        1, 5, 2, 4, 1
           i. i. i. i
        '''