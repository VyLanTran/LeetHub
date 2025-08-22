class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        '''
        Time: O(n^2)
        Space: O(1)
        '''

        # nums_len = len(nums)
        # j = nums_len - 1

        # while j > 0:
        #     for i in range(j):
        #         nums[i] = (nums[i] + nums[i + 1]) % 10
        #     j -= 1

        # return nums[0]

        '''
        1 4 6 4 1 
         1 3 3 1
          1 2 1
           1 1
            1

        Time: O(n)
        Space: O(1)
        '''

        n = len(nums)
        res = 0

        for k in range(n):
            res += comb(n - 1, k) * nums[k]
        
        return res % 10

      
