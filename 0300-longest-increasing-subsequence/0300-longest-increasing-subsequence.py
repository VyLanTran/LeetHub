class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Time: O(n^2)
        Space: O(n)
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