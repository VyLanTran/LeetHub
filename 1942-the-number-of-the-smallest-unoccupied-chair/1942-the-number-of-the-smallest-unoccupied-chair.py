class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        '''
        [1, 5], [2, 6], [3, 10]
        
        queue: (0, 5), (1, 6)
        '''
        numFriends = len(times)
        chairs = [i for i in range(numFriends)]
        times = [[times[i][0], times[i][1], i] for i in range(numFriends)]
        times.sort(key = lambda x:x[0])
        queue = []
        
        for i in range(numFriends):
            arrival, leaving, index = times[i]
            # print(f"arrival = {arrival}, leaving = {leaving}, index = {index}, queue: {queue}, chairs = {chairs}")
            while queue and queue[0][0] <= arrival:
                _, chairIndex = heappop(queue)
                heappush(chairs, chairIndex)
            if index == targetFriend:
                return chairs[0]
            smallestChair = heappop(chairs)
            heappush(queue, [leaving, smallestChair])
        return 0
        
        