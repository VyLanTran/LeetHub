class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(n/2) = O(n)

        This is a better solution
        This solution is based on the following fact/observation:
            if freq(dominant) - freq(non_dominant) == 1:
                return -1 (cannot divide)
            else:
                # guaranteed that can divide
                # remaining job is to find the first index where balance > 0
        Fact: 
        '''

        # dom_outcomes = [0, 0]
        # num_freq = defaultdict(int)
        # nums_len = len(nums)

        # for num in nums:
        #     num_freq[num] += 1
        #     if num_freq[num] > dom_outcomes[-1]:
        #         dom_outcomes[0], dom_outcomes[1] = num, num_freq[num]
        
        # if dom_outcomes[1] - (nums_len - dom_outcomes[1]) == 1:
        #     return -1
        
        # balance = 0
        # for i, num in enumerate(nums):
        #     balance += 1 if num == dom_outcomes[0] else -1
        #     if balance > 0:
        #         return i

        '''
        Boyer-Moore Majority Voting Algorithm
        '''

        def boyer_moore_majority_voting():
            candidate = -1
            count = 0

            for num in nums:
                if count == 0:
                    candidate = num
                    count = 1
                else:
                    count += 1 if num == candidate else -1
            
            return candidate

        dominant = boyer_moore_majority_voting()
        dominant_count = 0
        count = 0

        for num in nums:
            dominant_count += 1 if num == dominant else 0

        if dominant_count - (len(nums) - dominant_count) == 1:
            return -1

        for i, num in enumerate(nums):
            if num == dominant:
                count += 1
                if count * 2 > i + 1 and (dominant_count - count) * 2 > len(nums) - (i + 1):
                    return i

        