class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
         0,1,2,3,4,5,  6, 7
        10,9,2,5,3,7,101,18
         1,1,1,2,2,3,  4,4

        '''
        nums_len = len(nums)
        count = [1 for _ in range(nums_len)]
        res = 1

        for i in range(1, nums_len):
            for j in range(i):
                if nums[j] < nums[i]:
                    count[i] = max(count[i], 1 + count[j])
            res = max(res, count[i])

        return res