class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        '''
        1 | 3, 5, 1
        => 2 + 4 = 6
        1, 3 | 5, 1
        => 4 + 6 = 10
        1, 3, 5 | 1
        => 6 + 2 = 8

        what makes min score?

        after putting borders, let say the borders occur at
        a1  a2 | a3 a4 | a5 ... | a{n-1}    an
        => score = a1 + an + (a2 + a3 + ... + a{n-1})
        a1 + an is the same for all ways
        min or max is decided by borders in between

        k bags => k-1 borders

        1,|3,5,1
        4,8,6,_

        score = first num + last num + sum(consec pairs of weight we selected)
        '''

        '''
        n = number of marbles

        Time: O(nlog(n))
        Space: O(n) - Python's sorting takes O(n) extra space
        '''

        if k == 1:
            return 0
        
        consec_pair_sums = [weights[i] + weights[i + 1] for i in range(len(weights) - 1)]
        
        # for max score, choose the k-1 max val in consec_pair_sums 
        # opposite for min score 
        consec_pair_sums.sort()

        n = len(consec_pair_sums)

        # return sum([consec_pair_sums[i] for i in range(n - 1, n - (k-1) - 1, -1)]) - sum([consec_pair_sums[i] for i in range(k-1)])
        # a better way to calculate difference of max and min sums

        res = 0
        for i in range(k - 1):
            res += consec_pair_sums[n - 1 - i] - consec_pair_sums[i]

        return res

