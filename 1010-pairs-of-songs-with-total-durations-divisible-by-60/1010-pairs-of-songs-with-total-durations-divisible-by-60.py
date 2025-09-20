class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        '''
        {
            0: 1, 2
        }
        + 1 + 2
        '''

        song_mod = defaultdict(int)
        res = 0

        for t in time:
            target = (60 - t % 60) % 60
            res += song_mod[target]
            song_mod[t % 60] += 1

        return res