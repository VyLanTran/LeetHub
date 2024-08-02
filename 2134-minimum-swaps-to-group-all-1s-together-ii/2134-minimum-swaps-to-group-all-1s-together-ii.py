class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        '''
        0,1,2,3,4,5,6,7,8
        0,1,1,1,0,0,1,1,0
        i         j
        numOnes = 5
        i = 1
        j = 5
        numZeros = 1
        res = 2
        '''
        def countOne(nums):
            res = 0
            for num in nums:
                res += 0 if num != 1 else 1
            return res
        
        numOnes = countOne(nums)
        i, j, numZeros, res = 0, 0, 0, len(nums)
        while j < numOnes:
            numZeros += 1 if nums[j] == 0 else 0
            j += 1
        j -= 1
        res = min(res, numZeros)
        for i in range(1, len(nums)):
            numZeros -= 1 if nums[i - 1] == 0 else 0
            j = (j + 1) % len(nums)
            numZeros += 1 if nums[j] == 0 else 0
            res = min(res, numZeros)
        return res
            
        
        
        