class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(1)
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


            

            