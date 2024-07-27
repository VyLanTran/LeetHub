# class Solution:
#     def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
#         def buildGraph():
#             adj = dict()
#             for i in range(len(original)):
#                 u, v, w = original[i], changed[i], cost[i]
#                 arr = adj.get(u, [])
#                 arr.append((v, w))
#                 adj[u] = arr
#             return adj
        
#         adj = buildGraph()
        
#         c = 'a'
#         dist = [float('inf') for _ in range(26)]
#         dist[c - ord('a')] = 0
        
#         def dfs(start, end):
#             if start == end:
#                 return 0
#             if start not in adj:
#                 return
#             for next in adj[start]:
                
            
            
class Solution:
    def minimumCostFrom(self, sourceChar):
        bests = {}
        seenCost = defaultdict(lambda: inf)
        seenCost[sourceChar] = 0
        frontier = [(0, sourceChar)]
        while len(frontier) > 0:
            reachCost, current = heappop(frontier)
            if current in bests:
                continue
            bests[current] = reachCost
            for d, edgeCost in self.edges[current].items():
                totalCost = reachCost + edgeCost
                if totalCost < seenCost[d]:
                    heappush(frontier, (totalCost, d))
                    seenCost[d] = totalCost
        return bests
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        self.edges = defaultdict(lambda: {})
        for i in range(len(original)):
            s = original[i]
            d = changed[i]
            c = cost[i]
            if d not in self.edges[s] or c < self.edges[s][d]:
                self.edges[s][d] = c

        bests = defaultdict(lambda: {})
        totalCost = 0
        for s, t in zip(source, target):
            if s != t:
                if t in bests[s]:
                    totalCost += bests[s][t]
                elif len(bests[s]) > 0:
                    return -1
                else:
                    best = self.minimumCostFrom(s)
                    bests[s] = best
                    if t in best:
                        totalCost += best[t]
                    else:
                        return -1
        return totalCost