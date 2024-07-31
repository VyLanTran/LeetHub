class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def buildAdj():
            adj = dict()
            for i in range(n):
                adj[i] = []
            for edge in edges:
                u, v = edge[0], edge[1]
                adj[u].append(v)
                adj[v].append(u)
            return adj
        
        adj = buildAdj()
        visited = set()
        
        def dfs(u):
            visited.add(u)
            for v in adj[u]:
                if v not in visited:
                    dfs(v)
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res
            