class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj_list = defaultdict(list)
        min_neighbors = float('inf')
        res = 0

        for u, v, w in edges:
            adj_list[u].append((v, w))
            adj_list[v].append((u, w))

        def count_neighbors(src):
            min_dist = [float('inf')] * n
            min_dist[src] = 0
            min_heap = [(0, src)]
            
            while min_heap:
                dist, u = heappop(min_heap)
                for v, w in adj_list[u]:
                    expected_dist = dist + w
                    if expected_dist < min_dist[v]:
                        min_dist[v] = expected_dist
                        heappush(min_heap, (expected_dist, v))
            
            return sum([1 if d <= distanceThreshold else 0 for d in min_dist])

        
        for u in range(n):
            num_neighbors = count_neighbors(u)
            if num_neighbors < min_neighbors:
                min_neighbors = num_neighbors
                res = u
            elif num_neighbors == min_neighbors and u > res:
                res = u

        return res
