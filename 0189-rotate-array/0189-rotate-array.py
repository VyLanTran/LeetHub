class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        '''
        [1,2,3,4,5,6,7]
        [5,6,7,1,2,3,4]
        # [7,6,5,4,3,2,1]

        [1,2,3,4,5,6,7]
        [7,6,5,4,3,2,1]
        [6,7,1,2,3,4,5]
        '''

        n = len(nums)
        k %= n

        def flip(start, end):
            i, j = start, end
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        flip(0, n - 1)
        flip(0, k - 1)
        flip(k, n - 1)
         