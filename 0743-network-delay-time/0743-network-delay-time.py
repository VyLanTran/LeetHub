class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        '''
        1, 2, 3, 4
        1, 0, 1 i

        min_heap = (1, 1), (1, 3)

        '''


        adj_list = defaultdict(list)
        min_times = {i: float('inf') for i in range(1, n + 1)}
        min_times[k] = 0
        min_heap = [(0, k)]

        for u, v, w in times:
            adj_list[u].append((v, w))

        while min_heap:
            time, u = heappop(min_heap)
           
            for v, travel_time in adj_list[u]:
                expected_time = time + travel_time
                if expected_time < min_times[v]:
                    min_times[v] = expected_time
                    heappush(min_heap, (expected_time, v))

        max_time = max(min_times.values())
        return -1 if max_time == float('inf') else max_time