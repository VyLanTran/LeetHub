class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        '''
        0, 1,2, 3, 4,5, 6
        9,12,5,10,14,3,10
        
        0, 1, 2, 3, 4, 5, 6
        6, 5, 4, 3, 2, 1, 0

        9,_, _,_, _, _,_

        '''

        numsLen = len(nums)
        res = [0] * numsLen

        newI, newJ = 0, numsLen - 1

        for i, j in zip(range(numsLen), range(numsLen - 1, -1, -1)):
            if nums[i] < pivot:
                res[newI] = nums[i]
                newI += 1
            if nums[j] > pivot:
                res[newJ] = nums[j]
                newJ -= 1

        while newI <= newJ:
            res[newI] = pivot
            newI += 1
 
        return res