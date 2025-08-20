class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        '''
        5,7,3,9,4,9,8,3,1
        '''

        '''
        Approach 1
        Time: O(n)
        Space: O(n)
        '''

        # freq = defaultdict(int)
        # max_num = -1

        # for num in nums:
        #     freq[num] += 1

        # for key, val in freq.items():
        #     if val == 1:
        #         max_num = max(max_num, key)

        # return max_num

        '''
        Cleaner version
        '''
        # num_freq = Counter(nums)

        # return max((num for num, freq in num_freq.items() if freq == 1), default=-1)

        '''
        Cleanest version
        '''

        return max([-1] + [num for num, freq in Counter(nums).items() if freq == 1])
