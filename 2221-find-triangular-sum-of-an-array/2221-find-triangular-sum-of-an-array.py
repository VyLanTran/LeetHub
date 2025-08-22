class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        '''
        0, 1, 2, 3, 4
        x, x, x, x, 5
        0, 8, 6, 9, 5

        i = 0 to 3
        i = 0 to 2
        i = 0 to 1

        index
        0+1 1+2 2+3 3+4
        0+1+1+2 1+2+2+3
        '''

        nums_len = len(nums)
        j = nums_len - 1

        while j > 0:
            for i in range(j):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            j -= 1

        return nums[0]
