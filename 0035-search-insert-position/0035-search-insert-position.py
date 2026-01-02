class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        0, 1, 2, 3
        1, 3, 5, 6
        l  m     r
        lr
        r  l=res

        0, 1, 2, 3
        1, 3, 5, 6  res = 0

        '''

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l