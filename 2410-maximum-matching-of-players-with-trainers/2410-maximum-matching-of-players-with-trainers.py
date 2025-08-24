class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        '''

        players = [4, 7, 9]
                    0  1. 2. 3
        trainers = [2, 5, 8, 8]
                       m
                    l
                    r
        start = 0, 2
        find(4, start = 0) = 1
        res = 0, 1
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