class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        '''
        m = num players
        n = num trainers
        Time: O(mlog(m) + nlog(n) + mlog(n)) = O(klog(k)), where k = max(m, n)
        Space: O(m + n) (due to sorting)
        '''

        num_players, num_trainers = len(players), len(trainers)
        num_matchings = 0
        start = 0
        players.sort()
        trainers.sort()

        def find_min_index(player, start):
            left, right = start, num_trainers - 1
            min_index = num_trainers 

            while left <= right:
                mid = left + (right - left) // 2
                if trainers[mid] >= player:
                    min_index = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            return min_index

        for player in players:
            min_index = find_min_index(player, start)
            if min_index == num_trainers:
                return num_matchings
            num_matchings += 1
            start = min_index + 1

        return num_matchings