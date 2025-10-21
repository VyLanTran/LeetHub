class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        Test cases

        [1] -> 0
        [0, 0, 1] -> 1

        Time: O(n)
        Space: O(1)
        '''
        # n = len(nums)
        # num_ones = 0
        # res = 0
        # num_deletes = 1
        # has_deleted = False
        # l = 0

        # for num in nums:
        #     if num == 0:
        #         num_deletes -= 1
        #         has_deleted = True
        #         while num_deletes < 0:
        #             removed_num = nums[l]
        #             if removed_num == 0:
        #                 num_deletes += 1
        #             else:
        #                 num_ones -= 1
        #             l += 1
        #     else:
        #         num_ones += 1
        #     res = max(res, num_ones)

        # if not has_deleted:
        #     return max(res - 1, 0)
        # return res

        n = len(nums)
        res = 0
        num_zeroes = 0
        l = 0

        for r, num in enumerate(nums):
            if num == 0:
                num_zeroes += 1
            while num_zeroes > 1:
                removed_num = nums[l]
                if removed_num == 0:
                    num_zeroes -= 1
                l += 1
            res = max(res, r - l)

        return res

     