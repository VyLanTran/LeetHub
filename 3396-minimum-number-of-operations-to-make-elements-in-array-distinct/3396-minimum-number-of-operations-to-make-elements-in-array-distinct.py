class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        '''
        0,1,2,3,4,5,6,7,8
        1,2,3,4,2,3|,3,5,7

        have to remove all elements from 0 to 5 (inclusively)
        6 numbers -> 6/3 = 2 operations (round up)
        scan right to left, determining the first position 
        where duplication happens

        0,1,2,3,4
        4,5,6,4,4

        set = 4
        i = 4, 3

        Time: O(n)
        Space: O(n)
        '''

        appearedNums = set()
        i = len(nums) - 1

        while i >= 0:
            if nums[i] in appearedNums:
                return ceil((i + 1) / 3)
            appearedNums.add(nums[i])
            i -= 1
        
        return 0