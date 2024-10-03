class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        '''
         0,1,2,3,4,5
        [3,2,1,2,1,7]
               
        1, 1, 2, 2, 3, 7
           2, 3, 4, 5, 7
           
           
         1, 1, 1, 1, 
         1, 2, 3, 4
        '''
        res = 0
        nums.sort()
        prevNum = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            if num > prevNum:
                prevNum = num
            else:
                newVal = prevNum + 1
                res += newVal - num
                prevNum = newVal
                
        return res