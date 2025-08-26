class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        '''
        len = m
        dominant = x
        x occurs > m//2 times

        when do we return -1?


        
        - scan left -> right to know dominant + its freq
        - scan left -> right, at any time we have
            (cur_len, cur_freq), (m - cur_len, dom_freq - cur_freq)
            if cur_freq * 2 > cur_len 
                if (dom_freq - cur_freq) * 2 > m - cur_len:
                    return i
                else:
                    return -1
            elif


        k dominant
        m- k non-dom
        len = m
        k > m//2

        2, 3, 2, 7, 3, 3, 3 => total = 1
        
        cur_len = 4
        rem_len = 
        val = -2

        balance (+ 1 if see dominant) (-1 else)
        total must be > 0
        scan to find total

        if we realize that cur_sum always <= 0 until the last element => return -1

        if total == 1 ==> only 1 more dom than non-dom
            if dom first or last => invalid

        >= 1 | >= 1
        => only if  >= 2  then valid

        >= 2 | 0

        1 1 1 1 0 0 | 
        
        scan, keep track of value
        if value > 0
            if total - value > 0:
                return i
            else
                return -1
        
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