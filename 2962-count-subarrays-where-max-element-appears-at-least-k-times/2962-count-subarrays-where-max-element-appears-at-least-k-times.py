class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        '''
        Time: O(n)
        Space: O(1)
        '''

        max_num = max(nums)
        res = 0
        left = 0
        nums_len = len(nums)
        freq = 0

        for right in range(nums_len):
            if nums[right] == max_num:
                freq += 1
            while freq == k:
                res += nums_len - right
                removed_num = nums[left]
                left += 1
                if removed_num == max_num:
                    freq -= 1

        return res
