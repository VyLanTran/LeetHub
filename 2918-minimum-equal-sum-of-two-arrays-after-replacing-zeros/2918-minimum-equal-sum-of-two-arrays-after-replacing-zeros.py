class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        Time: O(m + n)
        Space: O(1)
        '''

        def arr_pattern(nums):
            cur_sum, num_zeroes = 0, 0
            for num in nums:
                if num == 0:
                    num_zeroes += 1
                cur_sum += num

            return cur_sum, num_zeroes

        sum1, count1 = arr_pattern(nums1)
        sum2, count2 = arr_pattern(nums2)

        if count1 == 0 and count2 == 0:
            return sum1 if sum1 == sum2 else -1
        elif count1 == 0:
            return sum1 if sum2 + count2 <= sum1 else -1
        elif count2 == 0:
            return sum2 if sum1 + count1 <= sum2 else -1
        return max(sum1 + count1, sum2 + count2)
