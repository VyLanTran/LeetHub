class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        
        def buildGraph():
            for i in range(len(edges)):
                u, v = edges[i]
                w = succProb[i]
                graph[u].append((v, w))
                graph[v].append((u, w))
                
        buildGraph()
        
        maxHeap = [(-1, start_node)]
        succ = [0 for _ in range(n)]
        succ[start_node] = 1
        
        while maxHeap:
            pair = heappop(maxHeap)
            prob, u = -pair[0], pair[1]
            for v, w in graph[u]:
                if succ[v] < prob * w:
                    succ[v] = prob * w
                    heappush(maxHeap, (-succ[v], v))
                    
        return succ[end_node]
        
    