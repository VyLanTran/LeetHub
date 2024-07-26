class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        def buildAdj():
            adj = dict()
            for [u, v, w] in edges:
                arr1, arr2 = adj.get(u, []), adj.get(v, [])
                arr1.append((v, w))
                arr2.append((u, w))
                adj[u] = arr1
                adj[v] = arr2
            return adj
                
        adj = buildAdj()
        
        def dijkstra(k):
            dist = [float('inf') for _ in range(n)]
            dist[k] = 0
            queue = [(0, k)]
            
            while queue:
                (d, u) = heappop(queue)
                if u not in adj:
                    continue
                for (v, w) in adj[u]:
                    if dist[v] > d + w:
                        dist[v] = d + w
                        queue.append((dist[v], v))
                        
            count = 0
            for val in dist:
                count += 1 if val <= distanceThreshold else 0
            return count
                    
        minCity, res = n, 0
        for u in range(n):
            count = dijkstra(u)
            if count < minCity:
                minCity = count
                res = u
            elif count == minCity and u > res:
                res = u
        return res
            
                