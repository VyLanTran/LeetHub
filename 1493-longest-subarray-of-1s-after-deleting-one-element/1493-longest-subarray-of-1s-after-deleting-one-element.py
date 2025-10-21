class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        Test cases

        [1] -> 0
        [0, 0, 1] -> 1

        num_deletes = 1, 0, -1, 0, -1, 0
        res = 0, 1, 2, 3, 4, 5
        num_ones = 0, 1, 2, 3, 4, 5, 4, 3, 2
        has_deleted = False, T

        0,1,2,3,4,5,6,7,8
        0,1,1,1,0,1,1,0,1
        r r r r r r r r r
        l l l l l l

        num_ones = 0
        while r < n:
            if num == 0:
                num_deletes -= 1
                has_deleted = True
                while num_deletes < 0:
                    removed_num = nums[l]
                    if removed_num == 0:
                        num_deletes += 1
                    else:
                        num_ones -= 1
                    l += 1
            else:
                num_ones += 1
            res = max(res, num_ones)
            r += 1

        if not has_deleted:
            return max(res - 1, 0)
        '''
        n = len(nums)
        num_ones = 0
        res = 0
        num_deletes = 1
        has_deleted = False
        l = 0

        for num in nums:
            if num == 0:
                num_deletes -= 1
                has_deleted = True
                while num_deletes < 0:
                    removed_num = nums[l]
                    if removed_num == 0:
                        num_deletes += 1
                    else:
                        num_ones -= 1
                    l += 1
            else:
                num_ones += 1
            res = max(res, num_ones)

        if not has_deleted:
            return max(res - 1, 0)
        return res