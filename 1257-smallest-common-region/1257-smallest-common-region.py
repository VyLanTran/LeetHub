class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        def buildGraph():
            graph = dict()
            for region in regions:
                parent = region[0]
                for i in range(1, len(region)):
                    graph[region[i]] = parent
            return graph
        
        graph = buildGraph()
        parent1 = set()
        cur = region1
        while cur:
            parent1.add(cur)
            cur = graph[cur] if cur in graph else None
        cur = region2
        while cur:
            if cur in parent1:
                return cur
            cur = graph[cur] if cur in graph else None
        
            