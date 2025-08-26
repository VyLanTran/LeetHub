class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(n/2) = O(n)
        '''

        dom_outcomes = [0, 0]
        num_freq = defaultdict(int)
        nums_len = len(nums)

        for num in nums:
            num_freq[num] += 1
            if num_freq[num] > dom_outcomes[-1]:
                dom_outcomes[0], dom_outcomes[1] = num, num_freq[num]
        
        if dom_outcomes[1] - (nums_len - dom_outcomes[1]) == 1:
            return -1
        
        balance = 0
        for i, num in enumerate(nums):
            balance += 1 if num == dom_outcomes[0] else -1
            if balance > 0:
                return i