class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        '''
        0 1 2 3 4 5 6
        0 i 5 5 5 6 7
        1 _ 1 1 1 2 2

        
        '''

        min_heap = [(0, 0)]
        min_times = [float('inf')] * n
        min_times[0] = 0
        num_ways = [0] * n
        num_ways[0] = 1
        adj_list = defaultdict(list)
        MOD = 10**9 + 7

        for u, v, t in roads:
            adj_list[u].append((v, t))
            adj_list[v].append((u, t))
        
        while min_heap:
            time, u = heappop(min_heap)
            for v, t in adj_list[u]:
                expected_t = t + time
                if expected_t < min_times[v]:
                    min_times[v] = expected_t
                    num_ways[v] = num_ways[u] # reset to 0 then add num_ways[u], which is the number of ways to go to the prev point
                    heappush(min_heap, (expected_t, v))
                    num_ways[v] %= MOD
                elif expected_t == min_times[v]:
                    num_ways[v] += num_ways[u]
                    num_ways[v] %= MOD
        
        return num_ways[n - 1]