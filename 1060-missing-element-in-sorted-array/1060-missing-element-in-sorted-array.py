class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        '''
        1,2,3
        i i i
        
        k = 3
        cur = 2
        next = 3
        betwen = 0
        
        '''
        
        i, n = 0, len(nums)
        while i < n:
            if i == n - 1:
                return nums[i] + k
            curNum, nextNum = nums[i], nums[i + 1]
            numBetween = nextNum - curNum - 1
            if numBetween >= k:
                return curNum + k
            k -= numBetween
            i += 1
    