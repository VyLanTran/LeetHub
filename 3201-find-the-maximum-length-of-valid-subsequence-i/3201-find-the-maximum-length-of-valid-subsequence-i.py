class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        '''
        after choosing the first 2 numbers, we can decide the rest greedily
        o, o => the rest must be odd
        e, e => the rest must be even
        o, e => the rest alternating
        e, o => the rest alternating

        first 2 pairs must be 1 of 4 cases

        0,1,2,3,4,5,6
        1,2,1,1,2,1,2

        # f(i) = max len if a valid subsequence if we choose from [0:i] inclusively

        f(i, prev1, prev2):
            if i >= n:
                return 1
            
            if both prevs are not Null => we can decide whether to include i or not
            if we can add i:
                return 1 + f(i + 1, prev2, nums[i])
            else:
                return f(i + 1, prev1, prev2)
            
            if both are None:
                # if we choose current num
                return 1 + f(i + 1, nums[i], prev2)
                # if skip
                return f(i + 1, prev1, prev2)
            else: (ie, prev1 is not None but prev2 is None)
                # if select
                return 1 + f(i + 1, prev, nums[i])
                # if skip:
                return f(i + 1, prev1, prev2)

        '''
        n = len(nums)

        def expand_subsequence(first, sec):
            a, b = first, sec
            length = 2
            for i in range(b + 1, n):
                if (nums[a] + nums[b]) % 2 == (nums[b] + nums[i]) % 2:
                    a, b = b, i
                    length += 1
            return length

        # want first event => is_event1 = True
        # 0, 1, 2
        # 1, 2, 1
        def find_max_len(is_even1, is_even2):
            i = 0
            
            while i < n and (nums[i] % 2 == 0) is not is_even1:
                i += 1
            j = i + 1
            while j < n and (nums[j] % 2 == 0) is not is_even2:
                j += 1
            if i < n and j < n:
                return expand_subsequence(i, j)
            return 0

        max_len = 0
        for is_even1 in [True, False]:
            for is_even2 in [True, False]:
                max_len = max(max_len, find_max_len(is_even1, is_even2))

        return max_len


            

            