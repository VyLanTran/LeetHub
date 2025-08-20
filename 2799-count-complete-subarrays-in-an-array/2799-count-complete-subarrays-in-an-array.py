class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(n)
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
