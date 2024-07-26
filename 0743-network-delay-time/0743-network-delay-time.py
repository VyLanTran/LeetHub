class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        def buildAdjList(times):
            adj = dict()
            for time in times:
                u, v, w = time[0] - 1, time[1] - 1, time[2]
                arr = adj.get(u, [])
                arr.append((v, w))
                adj[u] = arr
            return adj
        
        adj = buildAdjList(times)
        
        dist = [float('inf') for _ in range(n)]
        dist[k - 1] = 0
        queue = [(0, k - 1)]
        
        while queue:
            pair = heappop(queue)
            d, u = pair[0], pair[1]
            if u not in adj:
                continue
            for (v, w) in adj[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    queue.append((dist[v], v))
                    
        res = max(dist)
        return res if res != float('inf') else -1
        
        
            