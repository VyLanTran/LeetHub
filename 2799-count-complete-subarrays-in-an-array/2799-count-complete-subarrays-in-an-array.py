class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        '''
        0,1,2,3,4
        1,3,1,2,2
        j j j j
        i i i

        target = 3
        num_dist = 0, 1, 2, 3, 2
        res = 0, 2, 4
        {
            1: 1, 2, 1
            3: 1, 0
            2: 1
        }

        i = 0, j = 3
            -> success
            -> every subarray starting with i = 0 and j: 3 -> n - 1 
            -> n - j = 5 - 3 = 2
        '''

        '''
        total_distinct = 3
        res = 0, 2, 4
        num_distinct = 0, 1, 2, 3, 2

        0,1,2,3,4
        1,3,1,2,2
        j j j j j
        i i i

        {
            1: 1, 2, 1
            3: 1, 0
            2: 1, 2
        }
        '''

        total_distinct = len(set(nums))
        res = 0
        num_distinct = 0
        num_freq = defaultdict(int)
        n = len(nums)
        i = 0

        for j in range(n):
            num = nums[j]
            num_freq[num] += 1
            
            if num_freq[num] == 1:
                num_distinct += 1
            
            while num_distinct == total_distinct:
                res += n - j
                removed_num = nums[i]
                i += 1
                num_freq[removed_num] -= 1
                if num_freq[removed_num] == 0:
                    num_distinct -= 1
        
        return res
